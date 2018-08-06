class MinHeap:
    def __init__(self):
        pass



    # build a new heap from a list of keys
    def build_heap(self, keys):
        Heap=keys
        number=len(Heap)
        bash=1
        n=1
        while bash<number:
            bash=bash*2
            n+=1
        for i in range(0,n-2):
            if number//2==0:
                if Heap[number]<Heap[number//2]:
                    temp=Heap[number]
                    Heap[number]=Heap[number//2]
                    Heap[number//2]=temp

    
    # add a new item to the heap
    def insert(self, item):
        pass

    # return the item with the minimum key value, removing the item from the heap
    def del_min(self):
        pass
    
    # print the minimum heap on the screen
    def display(self):
        pass

heap = MinHeap()

heap.build_heap([9, 5, 6, 2, 3])
heap.display()

heap.insert(1)
heap.insert(7)
heap.display()

print(heap.del_min())
print(heap.del_min())
heap.display()