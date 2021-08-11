import re


def fill_vertical(crossword, word):
    for i, letter in enumerate(word):
        crossword[i] = re.sub(r'-',letter, crossword[i],1)
    return crossword


def is_overlap(new, old):
    if len(set(old) - set(new)) < len(old):
        return True
    return False


def fill_word(crossword, word):
    word_len = len(word)

    # grow through each row of grid
    for i, row in enumerate(crossword):

        # if grid contains blank space and
        # it is less than size of word then
        # fill it vertically

        if re.search(r'\-+', row):
            blank_space = re.search(r'\-+',row).span()
            blank_space = blank_space[1] - blank_space[0]
            if blank_space == word_len:
                crossword[i] = re.sub(r'\-+', word, row)
                return crossword
            else:
                fill_vertical(crossword, word)
                return crossword

def fill_horizontal(crossword, word):
    pass

def fill_horizontal_sub(crossword, word):

    for i, row in enumerate(crossword):
        if re.search(r'\-+\w+',row):

            substr = re.search(r'(\-+)(\w+)', row).groups()
            word = word.replace(substr[1], '')
            if len(substr[0]) == len(word):
                x = re.sub(r'\-+', crossword[i], word)
                print(x)

            fill_word(crossword, word)

        elif re.search(r'\w+\-+',row):
            substr = re.search(r'(\w+)(\-+)', row).groups()
            word = word.replace(substr[0],'')

            if len(substr[1]) == len(word):
                print(crossword[i], word)
                crossword[i] = re.sub(r'\-+', word, row)
                return crossword


def crosswordPuzzle(crossword, words):
    old_word = ''
    for word in words:
        if is_overlap(word, old_word):
            print('Yes overlap ')
            fill_horizontal_sub(crossword, word)

        fill_word(crossword, word)
        old_word = word
        print(*crossword, sep='\n')





grid = ['+-++++++++',
        '+-++++++++',
        '+-++++++++',
        '+-----++++',
        '+-+++-++++',
        '+-+++-++++',
        '+++++-++++',
        '++------++',
        '+++++-++++',
        '+++++-++++']
answers = 'LONDON;DELHI;ICELAND;ANKARA'.split(';')

crosswordPuzzle(grid, answers)
#fill_word(['+-----++++'], 'mayur')