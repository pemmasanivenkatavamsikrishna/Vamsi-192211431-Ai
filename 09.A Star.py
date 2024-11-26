from queue import PriorityQueue
def astar(start,goal):
    open_list=PriorityQueue()
    open_list.put((0,0,start,[start]))
    s=set()
    while open_list:
        f,g,node,path=open_list.get()
        if(node==goal):
            return path,f
        for neighbour,cost in graph[node]:
         if neighbour not in s:
            new_cost=g+cost
            f_cost=new_cost+heuristic[neighbour]
            open_list.put((f_cost,new_cost,neighbour,path+[neighbour]))
    return None,float('int')
graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('D', 2), ('E', 5)],
        'C': [('A', 4), ('F', 3)],
        'D': [('B', 2), ('E', 1)],
        'E': [('B', 5), ('D', 1), ('G', 2)],
        'F': [('C', 3), ('G', 6)],
        'G': [('E', 2), ('F', 6)]
        }
heuristic = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 5,
        'E': 1,
        'F': 2,
        'G': 0
        }
path,cost=astar('A','G')
print(path)
print(cost)
