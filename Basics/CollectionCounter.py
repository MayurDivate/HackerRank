#Task
"""
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay P amount of money only if they get the shoe of their desired size.
Your task is to compute how much money  earned.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

num_customers = int(input())
shoes_available = Counter([int(x) for x in input().split(' ')])

customers = int(input())

income = 0

for customer in range(customers):

    deal = [int(x) for x in input().split(' ')]

    if shoes_available[deal[0]] > 0:
        shoes_available[deal[0]] -= 1
        income += deal[1]

print(income)