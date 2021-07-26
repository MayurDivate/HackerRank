
def countTriplets(arr, r):
    res = 0

    num_counts = getNumCounts(arr)
    #print(len(num_counts))
    for num in num_counts:
        # create expected triplet
        triplet = {num, num * r, num * (r ** 2)}
        #print(num, triplet)
        if len(set(triplet) - num_counts.keys()) == 0:
            x = [num_counts.get(x) for x in triplet]
            #print(x[0], x[1], x[2])
            res += x[0] * x[1] * x[2]

            #print([num_counts.get(x) for x in triplet])

    print(res)
    return res


def getNumCounts(arr):

    dictX = {}
    for i,n in enumerate(arr):
        dictX[n] = dictX.get(n, 0) + 1

    return dictX


#arr = [1, 2, 2, 4] # 2
#r = 2

#arr = [1, 3, 9, 9, 27, 81] # 6
#r = 3

#arr = [1, 5 ,5 ,25 ,125] # 4
#r = 5
#countTriplets(arr, r)

#"""


#input_06 expected output = 2325652489
#                           13621903916
r = 3
with open('input06.txt') as f:
    arr = [ int(n) for n in f.readline().split(' ')]
    print(len(arr))
    print(countTriplets(arr, r))
#"""