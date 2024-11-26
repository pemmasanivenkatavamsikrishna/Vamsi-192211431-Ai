n=int(input("Enter the Board Size:"))
a=[[0 for i in range(n)] for j in range(n)]
def check(r,c):
    for i in range(c,-1,-1):
        if(a[r][i]=='Q'):
            return False
    i,j=r,c
    while(i>=0 and j>=0):
        if(a[i][j]=='Q'):
            return False
        i-=1
        j-=1
    i,j=r,c
    while(i<=n-1 and j>=0):
        if(a[i][j]=='Q'):
            return False
        i+=1
        j-=1
    return True
def board(c):
    if(c==n):
        return True
    for i in range(n):
        if(check(i,c)):
           a[i][c]='Q'
           if(board(c+1)):
               return True
           a[i][c]=0 
    return False
if(board(0)):
    for i in range(n):
        print(" ".join('Q' if(j=='Q') else '.' for j in a[i]))
else:
    print("No Solution")
           
        
