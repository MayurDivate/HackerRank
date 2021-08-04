def print_rangoli(size):
    # your code goes here
    side = 1 + (size - 1) * 2
    side += side - 1
    mid_point = (side + 1) / 2

    print(size, side, mid_point)

    for i in range(1, int(mid_point)+1):
        print()
        next_letter = size-1
        for j in range(1, side+1):
           if (j % 2) != 0:
               #print(abs(next_letter), end='')
               print(chr(ord('a')+abs(next_letter)), end='')
               next_letter -= 1

           else:
               print('-', end='')



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)