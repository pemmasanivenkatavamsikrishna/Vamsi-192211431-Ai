import itertools as i
op1='SEND'
op2='MORE'
res='MONEY'
letters=''
for j in op1+op2+res:
    if j not in letters:
        letters+=j
print(letters)
def cryptarithmetic():
    for p in i.permutations(range(10),len(letters)):
        d=dict(zip(letters,p))
        base,exp=10,len(op1)-1
        s1,s2,s3=0,0,0
        for j in op1:
            s1+=d[j]*pow(base,exp)
            exp-=1
        exp=len(op2)-1
        for j in op2:
            s2+=d[j]*pow(base,exp)
            exp-=1
        exp=len(res)-1
        for j in res:
            s3+=d[j]*pow(base,exp)
            exp-=1
        if(s1+s2==s3 and d[res[0]]!=0):
            print("Solution Found")
            print(op1,"=",s1)
            print(op2,"=",s2)
            print(res,"=",s3)
            print("LETTER VALUES=",d)
            break
    else:
        print("Solution Not Found")
cryptarithmetic()
