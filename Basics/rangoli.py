def print_rangoli(size):
    # your code goes here
    side = 1 + (size - 1) * 2
    side += side - 1
    mid_point = (side + 1) / 2

    start_point = mid_point
    end_point = mid_point
    #print(size, side, mid_point)


    for i in range(1, int(mid_point)+1):
        if i != 1:
            print()

        next_letter = size-1
        for j in range(1, side+1):
           if ((j % 2) != 0) and (j >= start_point) and (j <= end_point):
               #print(abs(next_letter), end='')
               print(chr(ord('a')+abs(next_letter)), end='')
               if j < mid_point:
                   next_letter -= 1
               else:
                   next_letter += 1

           else:
               print('-', end='')

        if i < (mid_point/ 2):
            start_point -= 2
            end_point += 2
        else:
            start_point += 2
            end_point -= 2



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)