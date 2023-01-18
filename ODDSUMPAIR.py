'''
Chef has 
3
3 numbers 
�
,
�
A,B and 
�
C.

Chef wonders if it is possible to choose exactly two numbers out of the three numbers such that their sum is odd.
'''

#code

withdraw_amount=int(input())
account_balance=float(1593)
if withdraw_amount%5!=0 or withdraw_amount+0.50>account_balance:
    print(account_balance)
else:
    if account_balance == (account_balance - 0.50) - withdraw_amount:
        print(float(account_balance))
