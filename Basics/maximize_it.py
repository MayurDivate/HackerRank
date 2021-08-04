# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

k, m = [int(x) for x in input().split(' ')]

input_lists = [[int(x) ** 2 for x in input().split(' ')[1:]] for i in range(k)]

res = 0

for x in itertools.product(*input_lists):
    if res < sum(list(x)) % m :
        res = sum(list(x)) % m

print(res)



# Input lines below one by one : expected output 763
# 6 767
# 2 488512261 423332742
# 2 625040505 443232774
# 1 4553600
# 4 92134264 617699202 124100179 337650738
# 2 778493847 932097163
# 5 489894997 496724555 693361712 935903331 518538304

