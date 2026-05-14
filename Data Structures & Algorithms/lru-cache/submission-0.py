class Node:
    def __init__(self, val = 0, key = None, next = None, prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        next = self.head.next
        self.head.next = node
        node.next = next
        node.prev = self.head
        next.prev = node
    
    def remove(self, node):
        next, prev = node.next, node.prev
        next.prev = prev
        prev.next = next

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(value, key)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
