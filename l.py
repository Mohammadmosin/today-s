class vertex:
    def __init__(self,name):
        self.branches=[]
        self.name=name

class Search:
    def __init__(self):
        self.visited=[]
        self.c=0
    def dfs(self,vertex):
        c=1
        self.visited.append(vertex)
        for j in vertex.branches:
            if j not in self.visited:
                c+=self.dfs(j)
        return c
    def bfs(self,vertex):
        c=0
        l=[]
        print(vertex.name)
        self.visited.append(vertex)
        for j in vertex.branches:
            if j not in self.visited:
                c+=1
                l.append(j)
        for i in l:
            print(len(l))
            c=c+self.bfs(i)
        return c

A=vertex('A')
B=vertex('B')
C=vertex('C')
D=vertex('D')
E=vertex('E')
F=vertex('F')
G=vertex('g')
a = [B,E,C,G]
b = [A]
c = [D,A]
d = [C,F,G]
e = [A]
f = [D]
g=[A,D]
h=Search()
A.branches=a
B.branches=b
C.branches=c
D.branches=d
E.branches=e
F.branches=f
G.branches=g
print(h.dfs(A))
i=Search()
print(i.bfs(A))
#print(i.visited[0].name)




