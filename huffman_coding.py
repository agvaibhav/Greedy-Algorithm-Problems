class huffmanNode:
    def __init__(self,data,c):
        self.c=c
        self.data=data
        self.left=None
        self.right=None

class huffman:

    def __init__(self):
        self.heap=[]

    def parent(self,i):
        return((i-1)//2)

    def heappush(self,node):
        self.heap.insert(0,node)
        self.heapify()

    def heappop(self):
        res=self.heap.pop(0)
        self.heapify()
        return(res)
        
    def heapify(self):
        for i in range(len(self.heap)):
            while(i!=0 and self.heap[self.parent(i)].data>self.heap[i].data):
                self.heap[i],self.heap[self.parent(i)] = self.heap[self.parent(i)],self.heap[i]



    def printCode(self,root,s):
        if root.left==None and root.right==None and root.c.isalpha():
            print(root.c + ':' +s)
            return

        self.printCode(root.left, s+'0')
        self.printCode(root.right, s+'1')

    def huffmanTree(self,n,chararr,freqarr):

        for i in range(n):
            hn = huffmanNode(freqarr[i], chararr[i])
            self.heappush(hn)

        while(len(self.heap)>1):
            x=self.heappop()
            y=self.heappop()

            f=huffmanNode(x.data+y.data, '-')

            f.left=x
            f.right=y

            root = f
            self.heappush(f)

        self.printCode(root, "")



chararr=['a','b','c','d','e','f']
freqarr=[5,9,12,13,16,45]
n=len(chararr)
hf=huffman()
hf.huffmanTree(n,chararr,freqarr)


