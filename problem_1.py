from collections import OrderedDict

class LRU_Cache():
    # Begin Hash Map
    def __init__(self, capacity = 5):
        # Put default capacity of 5 in case it was not set first
        # Initialize class variables
        self.lru_cache = OrderedDict()
        self.capacity = capacity
        self.key_storage = []
        assert self.capacity != 0, "Lru_cache size must be greater than 0"

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        current_key = str(key)
        try:
            return self.lru_cache[current_key]
        except:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        key = str(key)
        #Check if it exists first
        if key in self.lru_cache:
            del self.lru_cache[key]
        self.lru_cache[key] = value
        self.key_storage.append(key)
        if len(self.lru_cache) > 5:
            self.lru_cache.popitem(last=False)
        return



our_cache = LRU_Cache()

#Test Case 1
our_cache.set(1, 2)
our_cache.set(2, 1)
our_cache.set(4, 4)
print("Test Case #1")
print(our_cache.get(1))  # returns 2
print(our_cache.get(2))  # returns 1
print(our_cache.get(3))  # return -1
#Expected Output = {2, 1, -1}

#Test Case 2
our_cache1 = LRU_Cache(5)
our_cache1.set(1, 10)
our_cache1.set(2, "I should not be here")
our_cache1.set(3, "But I'm here")
our_cache1.set(4, None)
our_cache1.set(5, 5)
our_cache1.set(6, 6)
our_cache1.set(7, 7)
print("Test Case #2")
print(our_cache1.get(1))
print(our_cache1.get(2))
print(our_cache1.get(3))
print(our_cache1.get(4))
print(our_cache1.get(5))
print(our_cache1.get("street"))
print(our_cache1.get(7))
#Expected output = {-1, -1, "But I'm Here", None, 5, -1, 7}
#This demonstrates that keys 1 and 2 should not print these values because the
#cache got overfilled as they are LRU.

#Test Case 3
our_cache2 = LRU_Cache(5)
our_cache2.set("apple", 1)
our_cache2.set("banana", 2)
our_cache2.set("carrot", 3)
our_cache2.set("tacos", 4)
our_cache2.set("eggplant", 5)
our_cache2.set("apple", 6)
our_cache2.set("gordo", 7)
print("Test Case #3")
print(our_cache2.get("apple"))
print(our_cache2.get("banana"))
print(our_cache2.get("carrot"))
print(our_cache2.get("tacos"))
print(our_cache2.get("eggplant"))
print(our_cache2.get("gordo"))
#Expected output = {6, -1, 3, 4, 5, 7}
#This demonstrates that previously discarded least recently used keys can come back
#In this case, the first value for key = "apple" was discarded but
#2nd instance is back as it was filled again unto here.

#For corner case, our_cache3 should error out and display message
our_cache3 = LRU_Cache(0)


