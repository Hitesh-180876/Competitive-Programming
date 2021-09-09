# Hitesh Sharma
# 180876
# Assignment 1 
# Competitive Programming

import sys

def answer(curr, step, dest, countLeft):
    
    if countLeft == 0:
        if curr == dest:
            return True
        return False
        
        
    return answer(curr+step, step, dest, countLeft-1) or answer(curr-step, step, dest, countLeft-1)
    
    
    
T = int(sys.stdin.readline().rstrip())

for i in range(T):
    A, B, C, D = list(map(int, sys.stdin.readline().rstrip().split()))
    if answer(A, B, C, D):
        print('yes')
    else:
        print('no')
    
    
