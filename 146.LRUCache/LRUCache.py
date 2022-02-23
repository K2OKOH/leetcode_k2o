from os import remove
from typing import List

class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.MoveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 创建结点
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.AddToHead(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.RemoveTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.MoveToHead(node)

    def AddToHead(self, node: DLinkedNode):
        node.prev = self.head
        node.next = self.head.next
        # self.head.next = node
        # node.next.prev = node
        self.head.next.prev = node
        self.head.next = node

    def RemoveNode(self, node: DLinkedNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def MoveToHead(self, node: DLinkedNode):
        self.RemoveNode(node)
        self.AddToHead(node)
    
    def RemoveTail(self):
        node = self.tail.prev
        self.RemoveNode(node)
        return node

if __name__ == '__main__':
    edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]

    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)    # returns 1
    cache.put(3, 3) # evicts key 2
    cache.get(2)    # returns -1 (not found)
    cache.put(4, 4) # evicts key 1
    cache.get(1)    # returns -1 (not found)
    cache.get(3)    # returns 3
    cache.get(4)    # returns 4
