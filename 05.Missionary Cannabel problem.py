from collections import deque
def is_valid(state):
    lc,lm,b=state
    rc,rm=3-lc,3-lm
    if(lm<lc and lm>0) and (rm<rc and rm>0):
        return False
    return True
def successors(state):
    lc,lm,b=state
    s=[]
    moves=[(1,0),(2,0),(0,1),(0,2),(1,1)]
    if b==1:
        for c,m in moves:
            ns=(lc-c,lm-m,0)
            if 0<=ns[0]<=3 and 0<=ns[1]<=3 and is_valid(ns):
                s.append(ns)
    else:
        for c,m in moves:
            ns=(lc+c,lm+m,1)
            if 0<=ns[0]<=3 and 0<=ns[1]<=3 and is_valid(ns):
                s.append(ns)
    return s
def solve():
    i_s=(3,3,1)
    g_s=(0,0,0)
    queue=deque()
    queue.append((i_s,[]))
    s=set()
    while queue:
        c_s,path=queue.popleft()
        if(c_s==g_s):
            print("Solution Found")
            return path+[g_s]
        s.add(c_s)
        for i in successors(c_s):
            if i not in s:
                queue.append((i,path+[c_s]))
    return None

s=solve()
for i in s:
    print(i)
