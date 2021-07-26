# solution 1
def countTriplets(arr, r):
    count = 0
    dict_freq = {}
    dict_pairs = {}

    for i in reversed(arr):
        if i * r in dict_pairs:
            count += dict_pairs[i * r]
        if i * r in dict_freq:
            dict_pairs[i] = dict_pairs.get(i, 0) + dict_freq[i * r]

        dict_freq[i] = dict_freq.get(i, 0) + 1
    print('Hacker',count)
    print(dict_pairs)
    return count

# solution 2

def countTripletsX(arr, r):
    res = 0
    num_freq = {}
    num_pair = {}

    for num in reversed(arr):
        num_r = num * r
        num_r_r = num * r * r

        # num 1 if NUM 2 exist in pair means it's a triplet
        res += num_pair.get((num_r, num_r_r), 0)

        # num 2 if num 3 exists
        num_pair[(num, num_r)] = num_pair.get((num, num_r), 0) + num_freq.get(num_r, 0)

        # for any number update the frequency
        num_freq[num] = num_freq.get(num, 0) + 1


    print('Solved',res)
    return res



#--------- test data

#arr = [1, 2, 2, 4] # 2
#r = 2

#arr = [1, 3, 9, 9, 27, 81] # 6
#r = 3

#arr = [1, 5 ,5 ,25 ,125] # 4
#r = 5

arr = [5, 20, 25, 100, 125, 500]
r = 5

""""
#print(arr)
countTriplets(arr, r)
countTripletsX(arr, r)

"""


#input_06 expected output = 2325652489
#                           1359210564
#                           13621903916
#r = 3


# input_08 r = 100 output = 0
r = 3
with open('input06.txt') as f:
    arr = [ int(n) for n in f.readline().split(' ')]
    print(len(arr))
    countTriplets(arr, r)
    countTripletsX(arr, r)
#"""