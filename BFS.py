class vertix:
    def __init__(self,data,name):
        self.name=name
        self.data=data
        self.branches=[]
    def print(self):
        print("FDS")
class bfs:
    def __init__(self,matrix):
        self.matrix=matrix
        self.m=[]
        self.visted=[]
        self.ct=1
    def Graph(self):
        pass
        l=[]
        n=[]
        for i in range(0,len(self.matrix)):
            for j in range(0,len(self.matrix)):
                l.append(str(i)+str(j))
                k=l[len(l)-1]
                h=self.matrix[i][j]
                k=vertix(h,str(i)+str(j))
                n.append(str(i)+str(j)) #n contains name of all vertex
                self.m.append(k) #m contains all vertex
        c=0
        for i in range(0,len(self.matrix)):
            for j in range(0,len(self.matrix)):
                if self.matrix[i][j]==1:
                    h=n.index(str(i)+str(j))
                    if h==15:
                        print(self.matrix[i+1][j+1])
                        print(self.matrix[i][j])
                    if j+1<len(self.matrix):
                        if self.matrix[i][j+1]==1:
                            p = n.index(str(i) + str(j+1))
                            self.m[h].branches.append(self.m[p])
                    if j - 1 >= 0:
                        if self.matrix[i][j - 1] == 1:
                            #print(i, j)
                            p = n.index(str(i) + str(j - 1))
                            self.m[h].branches.append(self.m[p])
                            #print(self.m[p].name)
                    if i-1 >=0:
                        if self.matrix[i-1][j] == 1:
                            #print(i, j)
                            p = n.index(str(i-1) + str(j))
                            self.m[h].branches.append(self.m[p])
                            #print(self.m[p].name)
                    if i+1 < len(self.matrix):
                        if self.matrix[i+1][j] == 1 :
                            p = n.index(str(i+1) + str(j))
                            self.m[h].branches.append(self.m[p])
                    if j+1<len(self.matrix) and j-1>=0 and i-1>=0:
                        if self.matrix[i-1][j-1]==1:
                            p = n.index(str(i-1) + str(j-1))
                            self.m[h].branches.append(self.m[p])
                    if j+1<len(self.matrix)-1 and i+1<len(self.matrix)-1:
                        if self.matrix[i+1][j+1] == 1:
                            print(i, j)
                            p = n.index(str(i+1) + str(j+1))
                            self.m[h].branches.append(self.m[p])
                            #print(self.m[p].name)
                    if i-1 >=0 and j+1<len(self.matrix)-1:
                        if self.matrix[i-1][j+1] == 1:
                            #print(i, j)
                            p = n.index(str(i-1) + str(j+1))
                            self.m[h].branches.append(self.m[p])
                            #print(self.m[p].name)
                    if i+1 < len(self.matrix) and j-1>=0:
                        if self.matrix[i+1][j-1] == 1 :
                            p = n.index(str(i+1) + str(j-1))
                            self.m[h].branches.append(self.m[p])

    def bfs(self,i):
            c=1
            self.visted.append(i)
            for j in i.branches:
                    if j not in self.visted:
                        c+=self.bfs(j)


            return c





l = [[1, 1, 1, 0,0],
     [0, 1, 0,0,1],
     [0, 1, 1, 0,1],
     [1, 1, 1, 1,0],
     [1, 1, 0, 0,0]]
c=bfs(l)
c.Graph()

'''for k in c.m:
    print(k.name,len((k.branches)))'''

'''for i in c.m:
    k=c.bfs(i)'''
result=[]
for i in c.m:
    if i not in c.visted:
        result.append(c.bfs(i))
print(max(result))
g=c.m[12]
'''for v in g.branches:
    print(v.name)
print(len(g.branches))'''