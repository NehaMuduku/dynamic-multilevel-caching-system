from cache_level import CacheLevel

class MultiLevelCache:
    def __init__(self):
        self.levels = []

    def add_cache_level(self, size, eviction_policy):
        self.levels.append(CacheLevel(size, eviction_policy))

    def remove_cache_level(self, index):
        if 0 <= index < len(self.levels):
            self.levels.pop(index)
        else:
            raise IndexError("Invalid cache level index")

    def get(self, key):
        for level in self.levels:
            value = level.get(key)
            if value:
                self.promote_to_higher_levels(key, value)
                return value
        return None

    def put(self, key, value):
        if not self.levels:
            raise RuntimeError("No cache levels available")
        self.levels[0].put(key, value)

    def promote_to_higher_levels(self, key, value):
        for i in range(len(self.levels) - 1, 0, -1):
            if self.levels[i].get(key) is not None:
                self.levels[i].put(key, value)
                break
        self.levels[0].put(key, value)

    def display_cache(self):
        for i, level in enumerate(self.levels):
            print(f"L{i + 1} Cache: {level}")

