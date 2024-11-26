def minmax(depth,node_index,maximizing,values):
    if depth==0 or node_index>=len(values):
        return values[node_index]
    if maximizing:
        max_eval=float('-inf')
        for i in range(2):
            val=minmax(depth-1,node_index*2+i,False,values)
            max_eval=max(max_eval,val)
        return max_eval
    else:
        min_eval=float('inf')
        for i in range(2):
            val=minmax(depth-1,node_index*2+i,True,values)
            min_eval=min(min_eval,val)
        return min_eval
depth=3
values=[3,5,6,9,1,2,0,-1]
print("Optimal Value=",minmax(depth,0,True,values))
