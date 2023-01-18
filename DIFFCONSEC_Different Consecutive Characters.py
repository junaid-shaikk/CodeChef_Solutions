'''
Problem
Chef has a binary string 
�
S of length 
�
N. Chef can perform the following operation on 
�
S:

Insert any character (
0
0 or 
1
1) at any position in 
�
S.
Find the minimum number of operations Chef needs to perform so that no two consecutive characters are same in 
�
S.

'''

#code

withdraw_amount=int(input())
account_balance=float(1593)
if withdraw_amount%5!=0 or withdraw_amount+0.50>account_balance:
    print(account_balance)
else:
    if account_balance == (account_balance - 0.50) - withdraw_amount:
        print(float(account_balance))
