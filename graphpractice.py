'''
Two classes Node and Graph: Node holds the name of the Nodes
Graph holds the connections and the methods such as addnodes and add edges.
DFS and BFS are included also in the graph.
'''
import random
from random import randint

class Node:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name

class Graph:
    def __init__(self):
        self.list_node = {}
        self.connections = []

    

    
    def addnodes(self,name):
        new_node = Node(name)
        if name in self.list_node:  #checks if node already exists: ensures we can only add 1 node
            return
        else:
            x= randint(1,20)
            self.list_node[name] = Node(name) #adds node to name in the Node class
            
            edges = self.list_node[name] = []

    def addEdge(self,name,connections):
            if (name in self.list_node) and (connections in self.list_node):#will not display if nodes connects to itself.
               #name = self.list_node[connections]
               #connections = self.list_node[name]
               edges = self.list_node[name].append(connections)
               

    def DFS (self,node):
        stack = []
        visited = []
        stack.append(node)
        while stack:
            u = stack.pop()
            #print(u)
            for i in self.list_node[u]:
                #print(i)
                if i not in visited:
                    stack.append(i)
            visited.append(u)
        print(visited, "nodes connected")

    def BFS(self,node):
        queue = []
        visited = []
        queue.append(node)
        while queue:
            temp = queue.pop(0)
            for n in self.list_node[temp]:
                if temp not in visited:
                    queue.append(n)
            visited.append(temp)
            print('visited',temp)
        print( visited)


nodes = Graph()

def ranrange():
    x = random.randrange(1,100)
    print ("hello",x)
#ranrange()

def ransample():
    x = random.sample(xrange(1, 10), 100)
    x.sort()
    print (x)

def ranint():
        x = randint(1,20)
        print(x)

#ransample()
ranint()
nodes.addnodes(1)
nodes.addnodes(2)
nodes.addnodes(3)
nodes.addnodes(4)
nodes.addnodes(5)
nodes.addnodes(6)

nodes.addEdge(1,3)
nodes.addEdge(3,1)
nodes.addEdge(3,5)
nodes.addEdge(5,3)
nodes.addEdge(2,5)
nodes.addEdge(5,2)



print(nodes.list_node)
nodes.DFS(6)
#nodes.BFS(1)
