# Lab 8
# competitive Programming
# Hitesh 180876

import heapq

t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(item) for item in input().strip().split(" ")]
    h = []
    for index, item in enumerate(arr):
        heapq.heappush(h, (-1 * item, -1 * (item+index+1), index+1)) 
    ans = [0]*n
    for i in range(n):
        ans[i] = heapq.heappop(h)[2]
    print(" ".join(map(str, ans)))
