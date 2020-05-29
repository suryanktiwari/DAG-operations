'''
Assumptions:
    1. Node ids are integers
    2. Only DAGs are given input
'''

def makeGraph():
    n = int(input("Enter number of nodes in DAG\n"))
    print("Nodes are: ")
    network = dict()
    for i in range(n):
        network[i+1]=[]
        print(i+1, end = " ")
    e = int(input("Enter number of edges in the DAG\n"))
    print("Enter edge connections. Input format 'parent -> child' or 'child <- parent'\nNode id's are integers")
    for i in range(e):
        inp = input()
        nodes = inp.split(' ')
        if nodes[1]=="->":
            a = int(nodes[0])
            b = int(nodes[2])
        elif nodes[1]=="<-":
            a = int(nodes[2])
            b = int(nodes[0])
        else:
            print("Invalid Input")
            return None
        if not 0<a<=n or not 0<b<=n:
            print("Node ids are 1 to N only")
            return None
        if a in network:
            network[a].append(b)
        else:
            print("Node ids are 1 to N only")
            return None
    return network

def findAncestories(node):
    for n in graph[node]:
        if n not in temp:
            temp.add(n)
            findAncestories(n)        

def isTrailPath(graph, trail):
    if(len(trail)<2):
        print("Length of trail must be atleast 2")
        return False
    i = 0
    start = trail[i]
    nex = trail[i+1]
    while start in graph:
        i+=1
        if nex in graph[start]:
            start = nex
            if i+1 == len(trail):
                return True
            nex = trail[i+1]
        else:
            break
    return False

graph = makeGraph()
print("Graph is: ")
for node in graph:
    print(node, ": ", graph[node])

ancestors = dict()
descendents = []
temp = set()
for node in graph:
    temp.clear()
    findAncestories(node)
    temp2 = set()
    for x in temp:
        temp2.add(x)
    descendents.append((node, temp2))
for i in range(len(graph)):
    tmp = set()
    ancestors[i+1] = tmp
for ansc in descendents:
    for nod in ansc[1]:
        ancestors[nod].add(ansc[0])    
ancestors = [(tmp, ancestors[tmp]) for tmp in ancestors]
print("Ancestors are: ", ancestors)
print("Descendents are: ", descendents)

while(True and graph!=None):
    inp = input("Trail path check. Enter space separated node ids in the trail\n")
    if inp=="exit":
        break
    trail = inp.split(' ')
    trail = [int(ele) for ele in trail]
    print(isTrailPath(graph, trail))
