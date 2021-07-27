"""
Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some.
There are a number of different toys lying in front of him, tagged with their prices.
Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money.
Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.
Note Each toy can be purchased only once.

Example
prices = [1, 2, 3, 4]
k = 7
The budget is  units of currency. He can buy items that cost (1,2,3) for 6, or (1,2,4) for 7 units. The maximum is 3 items.
"""


def maximumToys(prices, k):
    toys = 0

    for toyPrice in sorted(prices):
        if (k - toyPrice) < 0:
            return toys
        else:
            toys += 1
            k -= toyPrice

    return toys

# time limit exceeds when bubble sort used
def bubbleSort(arr):
    for i in range(len(arr)):
        isSorted = True
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] =  arr[j+1], arr[j]
                isSorted = False

        if isSorted:
            return arr

    return arr


#print(maximumToys([1, 3, 2, 4], 7)) # 3
print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50)) # 4