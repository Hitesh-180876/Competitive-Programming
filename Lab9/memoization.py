# Lab 9
# Hitesh Kumar Sharma
# 180876

class Solution:
    def minSteps(self, N):
        dp = [-1 for i in range(N+1)]
        res = self.minStepsHelper(N, dp)
        
        return res
    
    def minStepsHelper(self, N, dp):
        
        if N == 1:
            return 0
        
        ans1 = sys.maxsize
        if N%3 == 0:
            if dp[N//3] == -1:
                ans1 = self.minStepsHelper(N//3, dp)
                dp[N//3] = ans1
            else:
                ans1 = dp[N//3]
        
        ans2 = sys.maxsize
            
        if N%2 == 0:
            if dp[N//2] == -1:
                ans2 = self.minStepsHelper(N//2, dp)
                dp[N//2] = ans2
            else:
                ans2 = dp[N//2]
        
        if dp[N-1] == - 1:
            ans3 = self.minStepsHelper(N-1, dp)
            dp[N-1] = ans3
        else:
            ans3 = dp[N-1]
            
        return 1+min(ans1, ans2, ans3)
                
                
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        ob = Solution()
        ans = ob.minSteps(N)
        print(ans)

# } Driver Code Ends
