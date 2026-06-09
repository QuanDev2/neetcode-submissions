class LRUCache:
    class Node:
        def __init__(self, key: int, val: int = 0):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = {}
        self.head, self.tail = self.Node(0), self.Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # move node to tail
            mru = self.hashmap[key]
            self.remove(mru)
            self.insertAtTail(mru)
            return self.hashmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # if key exists, update val in hashmap
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.remove(node)
            self.insertAtTail(node)
        else:
        # key not exists, create node, add to hashmap
            node = self.Node(key, value)
            self.hashmap[key] = node
            self.insertAtTail(node)

        # check size, if exceed cap, remove from hashmap, cut off head
        if len(self.hashmap) > self.cap:
            lru = self.head.next
            self.hashmap.pop(lru.key)
            self.head.next = lru.next
            lru.next.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertAtTail(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

