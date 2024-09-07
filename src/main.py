from cache_system import MultiLevelCache

def main():
    cache_system = MultiLevelCache()
    cache_system.add_cache_level(3, 'LRU')
    cache_system.add_cache_level(2, 'LFU')

    cache_system.put("A", "1")
    cache_system.put("B", "2")
    cache_system.put("C", "3")
    print("Get A:", cache_system.get("A"))  # Should return "1" from L1

    cache_system.put("D", "4")  # L1 is full, should evict least recently used
    print("Get C:", cache_system.get("C"))  # Should fetch from L2 and promote to L1

    cache_system.display_cache()

if __name__ == "__main__":
    main()

