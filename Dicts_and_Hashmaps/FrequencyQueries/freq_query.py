
def freqQuery(queries):

    # int to freq mapping using dir
    data = {}
    res = []

    for action, element in queries:

        if (action in [1, 2]) and (element in data.keys()):
            if action == 1:
                data[element] += 1
            elif action == 2:
                data[element] -= 1

        elif action == 1:
            data[element] = 1

        elif action == 3:
            if element in set(data.values()):
                res.append(1)
            else:
                res.append(0)

    return res


#inputx = [(1,1),(2,2),(3,3),(1,1),(1,1),(2,1),(3,2)] # [0, 1]
inputx = [(1, 3),(2, 3),(3, 2),(1, 4),(1, 5),(1, 5),(1, 4),(3, 2),(2, 4),(3, 2)] # [0, 1, 1 ]
print(freqQuery(inputx))