import threading
class node:
    def __init__(self,name,counter):
        self.name=name
        self.right=None
        self.left=None
        self.counter=counter
class BST:
    def __init__(self,root):
        self.root=root
    def add_node(self,node,rootnode):

        if node.counter<=rootnode.counter:
                if rootnode.left:
                    rootnode=self.add_node(node,rootnode.left)
                else:
                    rootnode.left=node
        else:
            if rootnode.right:
                    rootnode=self.add_node(node,rootnode.right)
            else:
                rootnode.right=node
    def minValueNode(self,node):
        current = node
        # loop down to find the leftmost leaf
        while (current.left is not None):
            current = current.left
        return current

    def deleteNode(self,root,name,key):

        # Base Case
        if root is None:
            return root
        # If the key to be deleted
        # is smaller than the root's
        # key then it lies in  left subtree
        if key <= root.counter and root.name!=name:
            root.left = self.deleteNode(root.left,name,key)

        # If the kye to be delete
        # is greater than the root's key
        # then it lies in right subtree
        elif (key > root.counter) and root.name!=name:
            root.right = self.deleteNode(root.right,name,key)

        # If key is same as root's key, then this is the node
        # to be deleted
        else:
            if name==root.name and root.counter==key:
            # Node with only one child or no child
                if root.left is None:
                    temp = root.right
                    root = None
                    return temp
                elif root.right is None:
                    temp = root.left
                    root = None
                    return temp
                # Node with two children:
                # Get the inorder successor
                # (smallest in the right subtree)
                temp = self.minValueNode(root.right)
                # Copy the inorder successor's
                # content to this node
                root.counter = temp.counter
                root.name=temp.name
                # Delete the inorder successor
                root.right = self.deleteNode(root.right,temp.name,temp.counter)

        return root

    def printPostorder(self,root):

        if root:
            # First recur on left child
            self.printPostorder(root.left)

            # the recur on right child
            self.printPostorder(root.right)

            # now print the data of node
            print(root.name,root.counter)

    def adjust_bst(self, name, counter):
        m=self.deleteNode(self.root, name, counter)
        node1 = node(name, counter+1)
        self.add_node(node1,m)
        self.printPostorder(m)
        return m


'''o=node("mosin",1)
oo=node("sha",2)
y=node("yasin",3)
yy=node("yasmeen",4)
s=node("sam",5)
m=BST(o)
m.add_node(oo,o)
m.add_node(y,o)
m.add_node(yy,o)
m.add_node(s,o)
#(m.printPostorder(o))
m.adjust_bst("sha",2)

m.adjust_bst("sha",3)
m.adjust_bst("sha",5)
m.adjust_bst("yasmeen",4)
m.adjust_bst("yasmeen",5)'''




#print(oo.counter)
#print(o.left.counter)
#print(o.right.counter)
#(m.printPostorder(o))



class hashtagclass():
    hashtagdict={}
    hashtag=[]
    root=None
    BSTnode=None
    def __init__(self,tags):
        self.tags=tags
        self.top10tags=[]
        self.keylock=threading.Lock()


    def find_toptags(self):
        self.tags = self.tags.split(" ")
        for i in self.tags:
            if i[0] == '#':
                tag = i[1:len(i)]
                try:
                    self.keylock.acquire()
                    if tag in hashtagclass.hashtagdict:
                        c = hashtagclass.hashtagdict[tag]
                        hashtagclass.hashtagdict[tag] = c + 1
                    else:
                        hashtagclass.hashtagdict[tag] = 1
                    if hashtagclass.root==None:
                        #print("yes")
                        hashtagclass.root = node(tag,1)
                        hashtagclass.BSTnode=BST(hashtagclass.root)
                        hashtagclass.hashtag.append(tag)
                    else:
                        hashtagclass.hashtag.append(tag)
                        if tag not in hashtagclass.hashtag:
                            n=node(tag,1)
                            hashtagclass.BSTnode.add_node(n,hashtagclass.root)

                        else:
                            hashtagclass.BSTnode.adjust_bst(tag,1)

                finally:
                    self.keylock.release()
        try:
            self.keylock.acquire()
            a = sorted(hashtagclass.hashtagdict.items(), key=lambda x: x[1])
        finally:
            self.keylock.release()
        a = a[::-1]
        c = 0
        for i in a:
            if c < 10:
                c += 1
                self.top10tags.append(i[0])
            else:
                break
def executionmain(text):
    obj = hashtagclass(text)
    obj.find_toptags()
    print(obj.top10tags)
#executionmain("#mosin #dhoni #yuvraj #a #b #c #d #e #f #j")
#t1=threading.Thread(target=executionmain,args=(input(), ))
#t2=threading.Thread(target=executionmain,args=(input(), ))
#t3=threading.Thread(target=executionmain,args=(input(), ))
#t1.start()
#t2.start()
#t3.start()
