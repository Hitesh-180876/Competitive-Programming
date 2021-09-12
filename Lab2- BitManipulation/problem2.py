# Hitesh Sharma
# 180876
# Assignment 1 
# Competitive Programming

from itertools import combinations

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    N, K = list(map(int, sys.stdin.readline().rstrip().split()))
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    a = combinations(arr, K)
    
    s = 0
    for i in list(a):
        s+=sum(list(i))
    print(s)
    
    #print(sum([sum(i) for i in a]))

