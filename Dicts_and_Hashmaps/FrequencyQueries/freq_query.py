
def freqQuery(queries):

    # int to freq mapping using dir
    freq_dict = {}
    res = []

    for action, element in queries:

        # insert 1
        if action == 1:
            freq_dict[element] = freq_dict.get(element, 0) + 1

        # delete 2
        elif action == 2:
            freq_dict[element] = max(0, freq_dict.get(element, 0) - 1)

        # print if element with same frequency exists
        elif action == 3:
            if element > 10000:
                res.append(0)
                #print(0)
            elif element in set(freq_dict.values()):
                res.append(1)
                #print(1)
            else:
                res.append(0)
                #print(0)

    return res


#inputx = [(1,1),(2,2),(3,3),(1,1),(1,1),(2,1),(3,2)] # [0, 1]
#inputx = [(1, 3),(2, 3),(3, 2),(1, 4),(1, 5),(1, 5),(1, 4),(3, 2),(2, 4),(3, 2)] # [0, 1, 1 ]

inputx = [( int(x.rstrip().split(' ')[0]), int(x.rstrip().split(' ')[1])) for x in open('test12.csv')]

out = freqQuery(inputx)
print(len(out))
print([i for i, e in enumerate(out) if e == 1])
