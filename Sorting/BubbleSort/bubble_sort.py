
def countSwaps(a):
    swaps = 0

    # bubble sort implementation
    # break if no swap occurred and declared it sorted
    # this will allow to minimize iterations

    for i in range(len(a)):
        # assume it is sorted
        isSorted = True

        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                swaps += 1
                # if swap occurred set isSorted to False to allow another iteration
                isSorted = False
                a[j], a[j+1] = a[j+1], a[j]

        if isSorted:
            break

    print('Array is sorted in',swaps,'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])



a = [1, 2, 3] # 0
a = [4, 2, 3, 1] # 5

countSwaps(a)