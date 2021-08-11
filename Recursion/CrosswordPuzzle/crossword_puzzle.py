import re


def fill_vertical(crossword, word):
    for i, letter in enumerate(word):
        crossword[i] = re.sub(r'-',letter, crossword[i],1)

    return crossword


def isOverlap(new, old):
    if len(set(old) - set(new)) < len(old):
        return True
    return False


def fill_word(crossword, word):
    word_len = len(word)

    # grow through each row
    for i, row in enumerate(crossword):
        if re.search(r'\-+',row):
            blank_space = re.search(r'\-+',row).span()
            blank_space = blank_space[1] - blank_space[0]
            if blank_space == word_len:
                crossword[i] = re.sub(r'\-+', word, row)
                return crossword
            else:
                #print(word, 'Vertical')
                fill_vertical(crossword, word)
                return crossword



def crosswordPuzzle(crossword, words):
    old_word = ''
    for word in words:
        print('*****************')
        fill_word(crossword, word)
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