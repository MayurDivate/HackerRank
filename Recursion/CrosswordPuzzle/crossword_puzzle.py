import re

class CrossWordPuzzel:

    def __init__(self, crossword, words):
        self.crossword = crossword
        self.words = words

    def is_overlap(self, new_word, old_word):
        # check if there was orverlap with previous word
        if len(set(old_word) - set(new_word)) < len(old_word):
            return True
        return False

    def fill_vertical(self, word):
        # fill words vertically without interruption
        for i, letter in enumerate(word):
            self.crossword[i] = re.sub(r'-',letter, self.crossword[i],1)

    def flip_crossword(self):
        grid = []
        for i in range(10):
            g = []
            for j in range(10):
                g.append(self.crossword[j][i])
            grid.append(''.join(g))

        self.crossword = grid

    def fill_vertical_sub(self, word):
        self.flip_crossword()
        self.fill_horizontal_sub(word)
        self.flip_crossword()

    def fill_word(self, word):
        word_len = len(word)

        # grow through each row of grid
        for i, row in enumerate(self.crossword):

            # if grid contains blank space and
            # it is less than size of word then
            # fill it vertically

            if re.search(r'\-+', row):
                blank_space = re.search(r'\-+', row).span()
                blank_space = blank_space[1] - blank_space[0]
                if blank_space == word_len:
                    self.crossword[i] = re.sub(r'\-+', word, row)
                    return self.crossword
                else:
                    self.fill_vertical(word)
                    return self.crossword

    def fill_horizontal_sub(self, word):
        for i, row in enumerate(self.crossword):
            if re.search(r'\-+\w\-+', row):
                m = re.search(r'(\-+)(\w+)(\-+)', row).groups()
                start = len(m[0])
                end = start + len(m[1])
                wordx = word[start:end]
                regx = '\w{' + str(len(m[0])) + '}' + m[1] + '\w{' + str(len(m[2])) + '}$'

                if (wordx == m[1]) and (re.match(regx, word)):
                    self.crossword[i] = re.sub(r'\-+\w\-+', word, row)

            elif re.search(r'\-+\w+', row):

                substr = re.search(r'(\-+)(\w+)', row).groups()
                word = word.replace(substr[1], '')

                if len(substr[0]) == len(word):
                    self.crossword[i] = re.sub(r'\-+', word, row)
                    return True

            elif re.search(r'\w+\-+', row):
                substr = re.search(r'(\w+)(\-+)', row).groups()
                word = word.replace(substr[0], '')

                if len(substr[1]) == len(word):
                    self.crossword[i] = re.sub(r'\-+', word, row)
                    return True

        return False

    def fillCrosswordPuzzle(self):
        # set old not to nothing
        old_word = ''

        # one word at time to fill
        for word in self.words:
            # if word is overlaps with previous then
            # try both vertical or horizontal.
            if self.is_overlap(word, old_word):

                if self.fill_horizontal_sub(word):
                    old_word = word
                else:
                    self.fill_vertical_sub(word)
                    old_word = word

            else:

                self.fill_word(word)
                old_word = word

        print(*self.crossword, sep='\n')


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

cw = CrossWordPuzzel(grid, answers)
cw.fillCrosswordPuzzle()

#fill_word(['+-----++++'], 'mayur')