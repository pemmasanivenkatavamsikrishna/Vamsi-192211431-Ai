colors=[0 for i in range(7)]
c_dict={1:'RED',2:'BLUE',3:'GREEN'}
def check(r,c):
    for i in range(7):
        if graph[r][i]==1 and colors[i]==c:
            return False
    return True
def color_graph(node):
    if(node==7):
        return True
    for c in range(1,4):
        if(check(node,c)):
            colors[node]=c
            if(color_graph(node+1)):
                return True
            colors[node]=0
    return False
graph=[[0,1,1,0,0,0,0],[1,0,1,1,0,0,0],[1,1,0,1,1,1,0],[0,1,1,0,1,0,0],[0,0,1,1,0,1,0],[0,0,1,0,1,0,0],[0,0,0,0,0,0,0]]
color_graph(0)
for i in range(7):
    print(f"Node-{i+1}={c_dict[colors[i]]}")
