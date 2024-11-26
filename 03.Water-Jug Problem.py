jug1=int(input("Enter the Jug-1 Capacity:"))
jug2=int(input("Enter the Jug-2 Capacity:"))
target1,target2=int(input("Enter the Target1:")),int(input("Enter the Target2:"))
def water_jug():
    j1,j2=0,0
    while(True):
        if(j1==0):
            j1+=jug1
            print("Filled Jug1-State({0},{1})".format(j1,j2))
        elif(j2==jug2):
            j2=0
            print("Emptied Jug2-State({0},{1})".format(j1,j2))
        elif(j1>0):
            water=min(j1,jug2-j2)
            j1-=water
            j2+=water
            print("Poured Water From Jug1 to Jug2-State({0},{1})".format(j1,j2))
        if(target1==j1 and target2==j2):
            break
    if(j1==target1 or j2==target2):
        print("Target Reached-({0},{1})".format(j1,j2))
    else:
        print("No Solution")
water_jug()
