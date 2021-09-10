# Hitesh Sharma
# 180876
# Assignment 1 
# Competitive Programming

import sys
sys.setrecursionlimit(10**5)
class sol():
    def f(self, i, j):
        global count, arr, n, m
        if (i<0 or j<0 or i>=n or j>=m or arr[i][j]==0 or arr[i][j]==2):
            return count
        elif arr[i][j] == 1:
            count+=1
            arr[i][j]=2
            self.f(i-1, j)
            self.f(i+1, j)
            self.f(i, j-1)
            self.f(i, j+1)
            self.f(i-1, j-1)
            self.f(i+1, j+1)
            self.f(i-1,j+1)
            self.f(i+1,j-1)
            
            return count
        
t = int(sys.stdin.readline().strip())
for num in range(t):
    maxcount = 0
    
    n, m = list(map(int, sys.stdin.readline().rstrip().split()))
    arr = [0]*n
    for i in range(n):
        s = str(input())
        arr[i] = [int(x) for x in s]
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                count = 0
                sol().f(i, j)
                maxcount = max(count, maxcount)
    print(maxcount)
