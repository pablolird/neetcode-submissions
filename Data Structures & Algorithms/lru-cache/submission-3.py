class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def append(self, node):
        n = self.tail.prev
        n.next = node
        node.prev = n
        node.next = self.tail
        self.tail.prev = node

    def pop(self):
        if (self.head.next != self.tail):
            n = self.head.next
            self.head.next = n.next
            n.next.prev = self.head
        return [n.key, n.val]

    def get(self, key: int) -> int:
        if (key not in self.map):
            return -1
        
        node = self.map[key]
        self.remove(node)
        self.append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if (key in self.map):
            self.map[key].val = value
            node = self.map[key]
            self.remove(node)

        else:
            if (self.size==self.capacity):
                [k, v] = self.pop()

                self.map.pop(k)
                self.size-=1
            
            self.map[key] = ListNode(key, value)
            self.size+=1
        
        node = self.map[key]
        self.append(node)
        

        


