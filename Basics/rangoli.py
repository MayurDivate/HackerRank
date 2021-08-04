
def print_rangoli(size):

    letters_required = [chr(ord('a') + i) for i in range(size)]
    building_blocks = []
    # one liner to calculate size of line
    size_of_line = 4 * size - 3

    for i in range(size):
        block = "-".join(letters_required[:i:-1] + letters_required[i::])
        # built in function center takes string and put it in middle of string of size n flanked by given character
        block = (block).center(size_of_line,'-')
        building_blocks.append(block)

    # print upper triangle
    print(*building_blocks[::-1], sep='\n')
    # print lower triangle
    print(*building_blocks, sep='\n')



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# old code

def print_rangoliX(size):
    # your code goes here
    size_of_line = 1 + (size - 1) * 2
    size_of_line += size_of_line - 1
    mid_point = (size_of_line + 1) / 2

    start_point = mid_point
    end_point = mid_point
    #print(size, side, mid_point)

    for i in range(1, int(mid_point)+1):
        if i != 1:
            print()

        next_letter = size-1
        for j in range(1, size_of_line+1):
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