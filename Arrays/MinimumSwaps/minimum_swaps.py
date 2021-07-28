# Complete the minimumSwaps function below.
def minimumSwaps(arr):

    nswaps = 0
    arr = [x-1 for x in arr]

    value_index_dict = {x:i for i, x in enumerate(arr)}

    for i, x in enumerate(arr):
        if i != x:
            pos2 = value_index_dict[i]

            # send x to the position of i and bring i to current position
            arr[i], arr[pos2] = i , x
            nswaps += 1

            # update new positions in the dict
            value_index_dict[i] = i
            value_index_dict[x] = pos2

    #print(nswaps)
    return nswaps

x= [1, 3, 5, 2, 4, 6, 7] #3
minimumSwaps(x)