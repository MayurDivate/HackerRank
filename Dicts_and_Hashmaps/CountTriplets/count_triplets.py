
def countTriplets(arr, r):

    ntriplets = 0
    num_freq = {}
    num_pair = {}

    for i in reversed(arr):
        i_r = i * r
        i_r_r = i * r * r

        # if first number then increment triplet count
        # by number of time pair of other two number exists
        ntriplets += num_pair.get((i_r, i_r_r), 0)

        # if it is second number in the triplet
        # i.e if only (i_r) present in the freq dict
        # then add a pair to pair dict
        # either it can be first entry pair value number times third num is present
        # or zero
        # as we are not checking presence of third number directly
        # we will set it to zero
        num_pair[(i, i_r)] = num_pair.get((i, i_r), 0) + num_freq.get(i_r, 0)

        # if third element then add it to the freq dict
        num_freq[i] = num_freq.get(i, 0) + 1

    return ntriplets


#--------- test datasets ---------------
filex = None
#arr, r, out = [1, 2, 2, 4], 2, 2
arr, r, out = [1, 3, 9, 9, 27, 81], 3, 6
#arr, r, out = [1, 5 ,5 ,25 ,125] , 5, 4
#arr, r, out = [5, 20, 25, 100, 125, 500], 5, 2
#arr, filex, r , out = [], 'input06.txt', 100, 0
#arr, filex, r, out  = [], 'input06.txt', 3, 2325652489

if len(arr) == 0:
    with open(filex) as f:
        x = [arr.append(int(n)) for n in f.readline().split(' ')]

print(countTriplets(arr, r), True if out == countTriplets(arr, r) else False)