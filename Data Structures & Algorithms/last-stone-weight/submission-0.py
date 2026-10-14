class Heap:
    def __init__(self, array=None) -> None:
        self.heap = []
        if array:
            self.build(array)

    def build(self, array) -> None:
        self.heap = array
        # Start at the last node that has children and sift each one down.
        # Leaves (the second half of the array) are already valid heaps of size 1.
        for index in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapifyDown(index)
        

    def insert(self, item: int):
        self.heap.append(item)
        self.max_heapify_up()

    def get_heap(self):
        return self.heap

    def delete_max(self) -> None:
        if (not self.heap):
            return
        # swap first and last items
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_value = self.heap.pop()
        # max heapify down
        self.max_heapify_down()
        return max_value
    
    def get_max(self) -> int:
        if (self.heap):
            return self.heap[0]
        return None

    def max_heapify_up(self) -> None:
        if not self.heap:
            return

        index = len(self.heap)-1
        self.heapifyUp(index)
        
    def heapifyUp(self, index):
        parent_index = self.get_parent(index)
        if (parent_index==None or self.heap[parent_index]>=self.heap[index]):
            return
                
        aux = self.heap[parent_index]
        self.heap[parent_index] = self.heap[index]
        self.heap[index] = aux

        self.heapifyUp(parent_index)


    def max_heapify_down(self) -> None:
        if not self.heap:
            return
        
        index = 0
        self.heapifyDown(index)

    def heapifyDown(self, index):
        l_c = self.get_left_child(index)
        r_c = self.get_right_child(index)

        if not l_c and not r_c:
            return
        
        l_v = self.heap[l_c] if l_c else float('-inf')
        r_v = self.heap[r_c] if r_c else float('-inf')

        if (self.heap[index] >= l_v and self.heap[index]>= r_v):
            return
        
        aux = self.heap[index]
        self.heap[index] = max(l_v, r_v)
        if max(l_v, r_v)==l_v:
            self.heap[l_c] = aux
            self.heapifyDown(l_c)
        else:
            self.heap[r_c] = aux
            self.heapifyDown(r_c)

    def get_parent(self, index) -> int:
        if (index==0):
            return None
        
        return (index-1)//2

    def get_left_child(self, index) -> int:
        l_c = 2*index + 1
        if (l_c >= len(self.heap)):
            return None
        return l_c
    
    def get_right_child(self, index) -> int:
        r_c = 2*index + 2
        if (r_c >= len(self.heap)):
            return None
        return r_c

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.h = Heap(stones)
        
        while (len(self.h.get_heap())>1):
            v1 = self.h.delete_max()
            v2 = self.h.delete_max()
            s = abs(v1-v2)
            if (not s):
                continue
            self.h.insert(s)
        
        if (len(self.h.get_heap())):
            return self.h.get_max()
        
        return 0



        