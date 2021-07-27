# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == '__main__':
    print("How many cards do you want to check?")
    cards = int(input())

    for card in range(cards):
        print(card+1,'/', cards, 'enter credit card number below!')
        num = input()

        # 16 digits or {4}-{4}-{4}-{4}
        if re.match(r'^((\d){16})$', num) or re.match(r'^(\d){4}(-((\d){4})){3}$', num):

            # should not have same number repeated consecutively 4 times or more
            # also should start with 4,5 or 6
            if re.search(r'(\d)\1{3}', num.replace('-', '')) or not re.match(r'^[456]', num):
                print('Invalid')
            else:
                print('Valid')
        else:
            print('Invalid')



##
# 42536258796157867       #17 digits in card number → Invalid
# 4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
# 5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
# 44244x4424442444        #Contains non digit characters → Invalid
# 0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid
#
# 4123456789123456  # valid
# 5123-4567-8912-3456 # valid
# 61234-567-8912-3456 #Invalid
# 4123356789123456 #valid
# 5133-3367-8912-3456 #Invalid
# 5123 - 3567 - 8912 - 3456 #Invalid
#
# #
