
# Hitesh Kumar Sharma
# 180876
# CP 6


class Solution:
    def JobScheduling(self,Jobs,n):
        count, profit = 0, 0
        Jobs = sorted(Jobs, key=lambda x:x.profit, reverse=True)
        slots = [False for i in range(n)]
        
        for i in range(n):
            for j in range(min(n, Jobs[i].deadline)-1, -1, -1):
                if not slots[j]:
                    profit += Jobs[i].profit
                    slots[j] = True
                    count+=1
                    break
        return count, profit

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends
