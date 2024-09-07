import unittest
from cache_system import MultiLevelCache

class TestMultiLevelCache(unittest.TestCase):

    def setUp(self):
        self.cache_system = MultiLevelCache()
        self.cache_system.add_cache_level(3, 'LRU')
        self.cache_system.add_cache_level(2, 'LFU')

    def test_put_and_get(self):
        self.cache_system.put("A", "1")
        self.cache_system.put("B", "2")
        self.cache_system.put("C", "3")
        self.assertEqual(self.cache_system.get("A"), "1")
        self.cache_system.put("D", "4")
        self.assertEqual(self.cache_system.get("C"), "3")

    def test_evict_lru(self):
        self.cache_system.put("A", "1")
        self.cache_system.put("B", "2")
        self.cache_system.put("C", "3")
        self.cache_system.put("D", "4")
        self.assertIsNone(self.cache_system.get("B"))  # B should be evicted

    def test_add_remove_level(self):
        self.cache_system.add_cache_level(2, 'LRU')
        self.assertEqual(len(self.cache_system.levels), 3)
        self.cache_system.remove_cache_level(1)
        self.assertEqual(len(self.cache_system.levels), 2)

if __name__ == '__main__':
    unittest.main()

