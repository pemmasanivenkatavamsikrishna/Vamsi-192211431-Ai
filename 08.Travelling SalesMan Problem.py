from itertools import permutations
def cal_route_cost(route):
    cost=0
    for i in range(len(route)-1):
        cost+=dm[route[i]][route[i+1]]
    cost+=dm[route[i+1]][0]
    return cost
def tsp(s_n):
    path=()
    route=(i for i in range(len(dm)) if i!=s_n)
    min_cost=999
    for i in permutations(route):
        i=(s_n,)+i
        cost=cal_route_cost(i)
        if min_cost>cost:
            min_cost=cost
            path=i
    print(path)
    print(min_cost)
dm = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
tsp(0)
