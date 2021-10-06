# Hitesh Kumar Sharma
# 180876
# CP 5


class Solution:
    def activitySelection(self,n,start,end):
        event=[]
        
        for i in range(len(start)):
            event.append((start[i],end[i]))
        event.sort(key=lambda x:x[1])
       
        attend=event[0][1]
        cnt=1
        for i in range(1,len(event)):
            if event[i][0]>attend:
                attend=event[i][1]
                cnt+=1
        return cnt
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.activitySelection(n,start,end))
# } Driver Code Ends
