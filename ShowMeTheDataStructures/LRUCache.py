class DoubleLinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, val):
        node = DoubleLinkedNode(val)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
        self.num_elements += 1
        return node
    
    def dequeue(self):
        if self.is_empty():
            return None

        node = self.head

        self.head = self.head.next
        if self.head == None:
            self.tail = None

        self.num_elements -= 1
        return node.value

class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.cache_map = dict()
        self.lru_queue = Queue()
        self.num_elements = 0
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key == None: # None key is invalid
            return -1

        node = self.cache_map.get(key)
        if node != None: #cache hit
            self.upgrade_node(node) #upgrade in cache
            return node.value

        return -1 #cache miss

    def upgrade_node(self, node): 
        #promotes node to right end (tail) of queue

        if self.num_elements == 1:
            return # no need to upgrade, there's only one node in the queue
        elif node == self.lru_queue.tail:
            return # no need to upgrade, it's already the most recently used element in the queue

        if node.previous != None:
            node.previous.next = node.next
        if node.next != None:
            node.next.previous = node.previous
            if node == self.lru_queue.head:
                self.lru_queue.head = node.next

        self.lru_queue.tail.next = node
        node.previous = self.lru_queue.tail
        self.lru_queue.tail = node
        self.lru_queue.tail.next = None

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key == None: # None key is invalid
            return

        if self.get(key) == -1: #key is not present in cache
            if self.num_elements == self.capacity: #is cache at capacity?
                self.remove_lru_element()
            
            node = self.lru_queue.enqueue(value)
            self.cache_map[key] = node
            self.num_elements += 1
        else: #override existing value
            self.cache_map[key].value = value
            # what to do with queue?

    def remove_lru_element(self):
        key_to_remove = self.lru_queue.dequeue()
        self.cache_map.pop(key_to_remove)
        self.num_elements -= 1

    def __repr__(self):
        s = 'elements: ' + str(self.num_elements) + '\n'
        head = self.lru_queue.head
        while head is not None:
            s += str(head.value) + '\n'
            head = head.next
        return s

our_cache = LRU_Cache(5)

print('*** Test LRU Cache ***')
print(our_cache.get(777))
assert our_cache.get(777) == -1, "There are no elements in cache yet. This should be cache miss."
our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))
assert our_cache.get(1) == 1, "Key not in LRU cache"
print(our_cache.get(2))
assert our_cache.get(2) == 2, "Key not in LRU cache"
print(our_cache.get(3))
assert our_cache.get(3) == -1, "Wrong return value, when key shouldn't be in LRU cache"
our_cache.set(9999999999999, 'value for large key')
print(our_cache.get(9999999999999))
assert our_cache.get(9999999999999) == 'value for large key', "There's a problem with storing large keys."
our_cache.set(7, 12)
our_cache.set(0, 815)
print(our_cache.get(1))
assert our_cache.get(1) == 1, "Key not longer in LRU cache, when capacity reached"
our_cache.set(5, 6)
print(our_cache.get(2))
assert our_cache.get(2) == -1, "Least recently used element should be removed from cache."
print(our_cache.get(None))
assert our_cache.get(None) == -1, "None key must be invalid!"
print('*** Success ***')
