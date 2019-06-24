class Double_Node:
    # Begin Double Node
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Double_Linked_List:
    # Begin Double Linked List Node
    def __init__(self):
        self.head = None
        self.tail = None
        self.list_length_limit_value = 1  # default of 1

    def list_limit(self, value):
        self.list_length_limit_value = int(value)
        return self.list_length_limit_value

    def list_length(self):
        length = 0
        node = self.head
        if self.head is None:
            return 0
        else:
            while node:
                length += 1
                node = node.next
            return length

    def delete(self, value):
        node = self.head
        if node is not None:
            while node:
                if node.value == value:
                    connect_me = node.next
                    prev = node.prev
                    prev.next = connect_me
                    return
                else:
                    node = node.next

    def search(self, value):
        node = self.head
        if node is None:
            return -1
        else:
            while node:
                if node.value == value:
                    return value
            return -1

    def insert(self, value):
        new_element = Double_Node(value)
        new_element.next = self.head
        new_element.prev = None
        if self.head is not None:
            self.head.prev = new_element
        self.head = new_element
        node = self.head
        counter = 0
        limit = self.list_length_limit_value
        while node:
            self.tail = node
            counter += 1
            if counter != limit:
                node = node.next
            else:
                self.tail.next = None
                break
        return


class LRU_Cache(Double_Linked_List):
    # Begin Hash Map
    def __init__(self, capacity = 5):
        # Put default capacity of 5 in case it was not set first
        # Initialize class variables
        self.lru_cache = dict()
        self.capacity = capacity
        self.cache_storage = Double_Linked_List()
        self.cache_storage.list_limit(capacity)
        self.key_storage = []

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        current_key = str(key)
        try:
            node = self.lru_cache[current_key]
            return node.value
        except:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        key = str(key)
        self.cache_storage.insert(value)
        node = self.cache_storage.head
        # Remove tail key if dict exceeds limit size
        if len(self.key_storage) == self.capacity:
            self.lru_cache.pop(self.key_storage[0])
            self.key_storage.pop(0)
        self.lru_cache[key] = node
        self.key_storage.append(key)


our_cache = LRU_Cache()

#Test Case 1
our_cache.set(1, 2)
our_cache.set(2, 1)
our_cache.set(4, 4)
print("Test Case #1")
print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(3))  # return -1
#Expected Output = {2, 1, 4}
#Also, if LRU_Cache input is blank then 5 is the default size, as instructed in project.

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
#Expected output = {"But I'm Here", None, 5, -1, 7}
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
