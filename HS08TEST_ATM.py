""" 
Problem
Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 $US.

Calculate Pooja's account balance after an attempted transaction.

Input Format
Each input contains 2 integers 
�
X and 
�
Y.
�
X is the amount of cash which Pooja wishes to withdraw.
�
Y is Pooja's initial account balance.

Output Format
Output the account balance after the attempted transaction, given as a number with two digits of precision. If there is not enough money in the account to complete the transaction, output the current bank balance.

Constraints
0
<
�
≤
2000
0<X≤2000 - the amount of cash which Pooja wishes to withdraw.
0
≤
�
≤
2000
0≤Y≤2000 with two digits of precision - Pooja's initial account balance.
Sample 1:
Input
Output
30 120.00
89.50
Explanation:
Example - Successful Transaction

Sample 2:
Input
Output
42 120.00
120.00
Explanation:
Example - Incorrect Withdrawal Amount (not multiple of 5)

Sample 3:
Input
Output
300 120.00
120.00
Explanation:
Example - Insufficient Funds
"""


#code

n,atm=map(float,input().split())
n=int(n)
if (n+0.5<=atm and n%5==0):
    print(float(atm-n-0.5))
else:
    print(float(atm))
