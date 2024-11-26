def alphabeta(depth,node_index,values,maximizer,alpha,beta):
    if depth==0 or node_index>=len(values):
        return values[node_index]
    if maximizer:
        max_val=float('-inf')
        for i in range(2):
            val=alphabeta(depth-1,node_index*2+i,values,False,alpha,beta)
            max_val=max(max_val,val)
            alpha=max(val,alpha)
            if beta<=alpha:
                break
        return max_val
    else:
        min_val=float('inf')
        for i in range(2):
            val=alphabeta(depth-1,node_index*2+i,values,True,alpha,beta)
            min_val=min(min_val,val)
            beta=min(val,beta)
            if beta<=alpha:
                break
        return min_val
depth=3
values=[3,5,6,9,1,2,0,-1]
print("Optimal Solution=",alphabeta(depth,0,values,True,float('-inf'),float('inf')))
            
