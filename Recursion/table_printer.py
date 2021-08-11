
def table(n, until=1):

    if until < 11:
        print(until*n)
        table(n, until+1)


for i in range(21,31):
    print('Table of : ', i)
    table(i)
    r