'''
Problem
Chef is currently standing at stair 
0
0 and he wants to reach stair numbered 
�
X.

Chef can climb either 
�
Y steps or 
1
1 step in one move.
Find the minimum number of moves required by him to reach exactly the stair numbered 
�
X.

'''

#code

for i in range(int(input())):
    a,b=map(int,input().split())
    c=(a//b)+(int(a%b))
    print(c)
