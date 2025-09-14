class heap:
    def __init__(self, size):
        self.customlist = [None] * (size + 1) 
        self.heapsize = 0
        self.maxsize = size + 1
def peekofheap(rootnode):
        if not rootnode:
            return
        else: return rootnode.customlist[1]
def sizeofheap(rootnode):
        if not rootnode:
            return 
        else:
            return rootnode.heapsize
def levelordertraversal(rootnode):
        if not rootnode:
            return
        else:
            for i in range(1, rootnode.heapsize + 1):
                print(rootnode.customlist[i])
def heapifytreeinsert(rootnode, index, heaptype):
    parentindex = int(index/2)
    if index <= 1:
         return
    if heaptype == "Min":
        if rootnode.customlist[index] < rootnode.customlist[parentindex]:
              temp = rootnode.customlist[index]
              rootnode.customlist[index] == rootnode.customlist[parentindex]
              rootnode.customlist[parentindex] = temp
              heapifytreeinsert(rootnode, parentindex, heaptype)
    elif heaptype == "Max":
        if rootnode.customlist[index] > rootnode.customlist[parentindex]:
            temp = rootnode.customlist[index]
            rootnode.customlist[index] == rootnode.customlist[parentindex]
            rootnode.customlist[parentindex] = temp
            heapifytreeinsert(rootnode, parentindex, heaptype)
def insertnode(rootnode, nodevalue, heaptype):
    if rootnode.heapsize + 1 == rootnode.maxsize:
          return " heap is full"
    rootnode.customlist[rootnode.heapsize + 1] = nodevalue
    rootnode.heapsize += 1
    heapifytreeinsert(rootnode, rootnode.heapsize, heaptype)
    return "value is added"
def heapifytreeextract(rootnode, index, heaptype):

    leftindex = index * 2
    rightindex = index *2 + 1
    swapchild = 0

    if rootnode.heapsize < leftindex:
         return
    elif rootnode.heapsize == leftindex:
         if heaptype == "Min":
              if rootnode.customlist[index] > rootnode.customlist[leftindex]:
                   temp = rootnode.customlist[index]
                   rootnode.customlist[index] = rootnode.customlist[leftindex]
                   rootnode.customlist[leftindex] = temp
              return
         else:
              if rootnode.customlist[index] < rootnode.customlist[leftindex]:
                   temp = rootnode.customlist[index]
                   rootnode.customlist[index] = rootnode.customlist[leftindex]
                   rootnode.customlist[index] = temp
              return
    else:
         if heaptype == "Min":
              if rootnode.customlist[leftindex] < rootnode.customlist[rightindex]:
                   swapchild = leftindex
              else:
                   swapchild = rightindex
              if rootnode.customlist[index] > rootnode.customlist[swapchild]:
                   temp = rootnode.customlist[index]
                   rootnode.customlist[index] = rootnode.customlist[swapchild]
                   rootnode.customlist[swapchild] = temp
         else:
              if rootnode.customlist[leftindex] > rootnode.customlist[rightindex]:
                   swapchild = leftindex
              else:
                   swapchild = rightindex
              if rootnode.customlist[index] < rootnode.customlist[swapchild]:
                   temp = rootnode.customlist[index]
                   rootnode.customlist[index] = rootnode.customlist[swapchild]
                   rootnode.customlist[swapchild] = temp
    heapifytreeextract(rootnode,swapchild, heaptype)
def extractnode(rootnode, heaptype):
     if rootnode.heapsize == 0:
          return
     else:
          extractnode = rootnode.customlist[1]
          rootnode.customlist[1] = rootnode.customlist[rootnode.heapsize]
          rootnode.customlist[rootnode.heapsize] = None
          rootnode.heapsize -= 1
          heapifytreeextract(rootnode, 1, heaptype)
          return extractnode
def deleteentirebh(rootnode):
     rootnode.customlist = None

# Create a Heap of size 10
myHeap = heap(10)

# Insert values into a Max Heap
insertnode(myHeap, 20, "Max")
insertnode(myHeap, 10, "Max")
insertnode(myHeap, 30, "Max")
insertnode(myHeap, 5, "Max")

print("Level order traversal after insertions:")
levelordertraversal(myHeap)   # prints heap array in level order

# Peek (get root element)
print("Peek of heap:", peekofheap(myHeap))   # should be 30 for Max heap

# Extract the root
print("Extracted:", extractnode(myHeap, "Max"))   # removes 30
print("After extraction:")
levelordertraversal(myHeap)

# Size of heap
print("Heap size:", sizeofheap(myHeap))

# Delete entire heap
deleteentirebh(myHeap)
print("Heap deleted:", myHeap.customlist)   # should be None
