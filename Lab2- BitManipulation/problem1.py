# Hitesh Sharma
# 180876
# Assignment 2 
# Competitive Programming

import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    N = int(input())  
    count = 0  
    while N>0:
        if N&1 == 1:
        count+=1
        N = N>>1
        
    print(count)
    
        
