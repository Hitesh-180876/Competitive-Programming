# Lab 10
# Competitive Programming
# Hitesh Sharma
# 180876

import math as mt
MAX=100001

prime = [0 for i in range(MAX + 1)]
 
# Simple sieve to find smallest prime
# factors of numbers smaller than MAX
def SOE():
 
    for i in range(2, mt.ceil(mt.sqrt(MAX + 1))):
     
        if (prime[i] == 0):
            for j in range(i * 2, MAX + 1, i):
                prime[j] = i
     
    # Prime number will have same divisor
    for i in range(1, MAX):
        if (prime[i] == 0):
            prime[i] = i


def lgcds(lis,n):
    
    ans=0
    countdiv = [0 for i in range(MAX + 1)]

    for i in range(n):
        element = lis[i]
        #get other prime divisors
        while element>1:
            div = prime[element] #eg for prime[6]==3 and 6/3==2
            
            countdiv[div]+=1 #counts the number of prime numbers greater then 1
            
            ans = max(ans,countdiv[div])
            #print(element)
            while(element%div==0):
                element = element//div
        #print(countdiv,"--")    
    return ans
            

SOE()

t = int(input())

for _ in range(t):
    n = int(input())
    lis = [int(x) for x in input().split()]
    print(lgcds(lis,n))
    
