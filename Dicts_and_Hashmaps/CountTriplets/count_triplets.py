
def countTriplets(arr, r):
    res = 0

    num_counts = getNumCounts(arr)

    for num in num_counts:
        # create expected triplet
        triplet = {num, num * r, num * (r ** 2)}
        if len(set(triplet) - num_counts.keys()) == 0:
            res +=  max([num_counts.get(x) for x in triplet])

    return res


def getNumCounts(arr):

    dictX = {}
    for i,n in enumerate(arr):
        dictX[n] = dictX.get(n, 0) + 1

    return dictX

"""
arr = [1, 2, 2, 4]
r = 2

arr = [1, 3, 9, 9, 27, 81]
r = 3

arr = [1, 5 ,5 ,25 ,125]
r = 5
"""


#input_06 expected output = 2325652489
r = 3
with open('input06.txt') as f:
    arr = f.readline().split(' ')
    print(countTriplets(arr, r))
