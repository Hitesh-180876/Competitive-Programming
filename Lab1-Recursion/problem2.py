# 180876
# Assignment 1 
# Competitive Programming

import sys

def answer(a, b, c, n):
    if n == 1:
        return a
    if n == 2:
        return b
    if n == 3:
        return c
        
    return answer(a, b, c, n-1)+answer(a, b, c, n-2)+answer(a, b, c, n-3)
    

T = int(sys.stdin.readline().strip())

for i in range(T):
    A, B, C, N = list(map(int, sys.stdin.readline().rstrip().split()))
    print(answer(A, B, C, N))
    
