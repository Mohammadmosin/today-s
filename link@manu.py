class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked:
    def __init__(self,head):
        self.head=head
    def add_beg(self,data):
        c=node(data)
        c.next=self.head
        self.head=c
    def add_end(self,data):
        pass
        d=node(data)
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=d
    def add_middle(self,data,i):
        pass
        z=node(data)
        itr=self.head
        f=0
        while f!=i:
            f=f+1
            itr=itr.next
        z.next=itr.next.next
        itr.next=z
    def print(self):
        itr = self.head
        while itr is not None:
            print(itr.data)
            #print(itr)
            itr = itr.next









a=node(1)
b=node(2)
d=linked(a)
#print (d.head.data)
#d.add_beg(3)
#print(d.head.data)
d.add_end(5)
d.add_end(11)
d.add_end(15)
#(d.print())
d.add_middle(17,2)
#d.print()
d.reverse_link()
#d.print()

'''def maximumSum(a, m):
    best_sum = 0  # or: float('-inf')
    current_sum = 0
    l=[]
    for x in a:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
        l.append(best_sum%m)
    return best_sum
numbers=[1,5,-9,12,-3,6,9,-12,7]
print(maximumSum(numbers,5))

print()'''
a={'mosin':5,'dhoni':6,'dravid':3,'a':0}
b=sorted(a.items(), key=lambda x:x[1])
print(b)