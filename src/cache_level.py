from collections import OrderedDict, defaultdict
import threading

class CacheLevel:
    def __init__(self, size, eviction_policy):
        self.size = size
        self.eviction_policy = eviction_policy
        self.cache = OrderedDict() if eviction_policy == 'LRU' else {}
        self.access_freq = defaultdict(int) if eviction_policy == 'LFU' else None
        self.lock = threading.Lock()

    def get(self, key):
        with self.lock:
            if key in self.cache:
                if self.eviction_policy == 'LFU':
                    self.access_freq[key] += 1
                if self.eviction_policy == 'LRU':
                    value = self.cache.pop(key)
                    self.cache[key] = value
                return self.cache[key]
            return None

    def put(self, key, value):
        with self.lock:
            if key in self.cache:
                if self.eviction_policy == 'LFU':
                    self.access_freq[key] += 1
                self.cache.pop(key)
            elif len(self.cache) >= self.size:
                self.evict()
            self.cache[key] = value
            if self.eviction_policy == 'LFU':
                self.access_freq[key] = 1

    def evict(self):
        if self.eviction_policy == 'LRU':
            self.cache.popitem(last=False)
        elif self.eviction_policy == 'LFU':
            least_frequent = min(self.access_freq.items(), key=lambda x: x[1])[0]
            self.cache.pop(least_frequent)
            del self.access_freq[least_frequent]

    def __repr__(self):
        return str(self.cache)

