import re


class CrossWord:

    def __init__(self, value, pos, start, end, isHorizontal):
        self.value = value
        self.pos = pos
        self.start = start
        self.end = end
        self.isHorizontal = isHorizontal
        self.possible_words = []
        self.isFilled = False

    def toString(self):

        if self.isHorizontal:
            return 'Row '+str(self.pos)+':'+str(self.start)+'-'+str(self.end)
        else:
            return 'Col '+str(self.pos)+':'+str(self.start)+'-'+str(self.end)

    def __hash__(self):
        cwg_str = 'Horizontal='+str(self.isHorizontal)+'In='+str(self.pos)+':'+str(self.start)+':'+str(self.end)
        return hash(cwg_str)


class CrossWordGrid(CrossWord):

    def isOverlapping(self, grid2):

        if self.isHorizontal != grid2.isHorizontal:
            if (self.pos >= grid2.start) and (self.pos <= grid2.end):
                if (self.start <= grid2.pos) and (self.end >= grid2.pos):
                    return True

        return False

    def get_overlapping_position(self, g2):

        assert isinstance(g2, CrossWordGrid)

        if self.isOverlapping(g2):
            return g2.pos - self.start, self.pos - g2.start


class CrossWordPuzzel():

    def __init__(self, matrix, crossWordGridList, answers):
        self.matrix = matrix
        self.crossWordGridDict = {cw : None for cw in crossWordGridList}
        self.word_to_grids = {ans: [] for ans in answers}
        self.grid_to_words = {cw: [] for cw in crossWordGridList}
        self.overlaps = {cw : [] for cw in crossWordGridList}
        self.assign_overlapping()

    def print_matrix(self):
        print(*self.matrix, sep='\n')

    def assign_overlapping(self):
        for cw1 in self.overlaps.keys():
            for cw2 in self.crossWordGridDict:
                if cw1 != cw2 and cw1.isOverlapping(cw2):
                    self.overlaps[cw1].append(cw2)

    def fill_unique_solutions(self):
        # fill a word in grid if that is
        # the only one grid associated with it
        for possible_word in self.word_to_grids.keys():
            if len(self.word_to_grids[possible_word]) == 1:
                cwg = self.word_to_grids[possible_word][0]
                cwg.value = possible_word
                cwg.isFilled = True
                self.crossWordGridDict[cwg] = possible_word

    def solve_puzzle(self, grid, word):
        overlap_flag = False

        # both should of equal sizes
        if len(word) == (grid.end - grid.start):

            overlap_flag = True
            assert isinstance(grid, CrossWordGrid)

            # get all overlapping grind
            for overlapping_grid in self.overlaps[grid]:
                # if those are filled with a word then
                # overlapping positiions should match

                x, y = grid.get_overlapping_position(overlapping_grid)

                if overlapping_grid.isFilled:
                    if word[x] != overlapping_grid.value[y]:
                        # overlapping positions did not match
                        overlap_flag = False


        if overlap_flag:
            grid.value = word
            grid.isFilled = True
            self.crossWordGridDict[grid] = word
            self.update_matrix()


    def get_possible_answers(self):
        # add list of grids to words
        for word in self.word_to_grids.keys():
            for g in self.crossWordGridDict:
                if len(word) == len(g.value):
                    g.possible_words.append(word)
                    self.word_to_grids[word].append(g)
                    self.grid_to_words[g].append(word)

    def update_matrix(self):
        for cwg in self.crossWordGridDict:
            if cwg.isFilled:
                if cwg.isHorizontal:
                    a = '' if cwg.start == 0 else self.matrix[cwg.pos][:cwg.start]
                    b = '' if cwg.end == 10 else self.matrix[cwg.pos][cwg.end:]
                    self.matrix[cwg.pos] = a + cwg.value + b
                else:
                    for i in range(cwg.start, cwg.end):
                        a = '' if cwg.pos == 10 else self.matrix[i][:cwg.pos]
                        b = '' if cwg.pos == 10 else self.matrix[i][cwg.pos+1:]
                        self.matrix[i] = a + cwg.value[i-cwg.start] + b





def crossWordPuzzel(grid, words):
    crossWordGrids = []

    for i, row in enumerate(grid):
        col = ''.join([grid[j][i] for j in range(len(grid))])

        re_matches = re.finditer(r'\-\-+', row)
        for match in re_matches:
            crossWordGrids.append((CrossWordGrid(match.group(), i, match.span()[0], match.span()[1], True)))

        re_matches = re.finditer(r'\-\-+', col)
        for match in re_matches:
            crossWordGrids.append((CrossWordGrid(match.group(), i, match.span()[0], match.span()[1], False)))

    cwp = CrossWordPuzzel(grid, crossWordGrids, words)
    cwp.get_possible_answers()
    cwp.fill_unique_solutions()

    while sum([1 for cw in cwp.crossWordGridDict if cw.isFilled]) < len(words):
        words_already_filled = [cwp.crossWordGridDict.get(cw, '') for cw in cwp.crossWordGridDict]
        for ans in words:
            if ans not in words_already_filled:
                for grid in cwp.crossWordGridDict:
                    cwp.solve_puzzle(grid, ans)


    cwp.print_matrix()
    return cwp.matrix



#grid = ['+-++++++++',  '+-++++++++', '+-++++++++', '+-----++++', '+-+++-++++', '+-+++-++++', '+++++-++++', '++------++', '+++++-++++', '+++++-++++']
#answers = 'LONDON;DELHI;ICELAND;ANKARA'

#grid = ['++++++-+++', '++------++', '++++++-+++', '++++++-+++', '+++------+', '++++++-+-+', '++++++-+-+', '++++++++-+', '++++++++-+', '++++++++-+']
#answers = 'ICELAND;MEXICO;PANAMA;ALMATY'

grid = ['+-++++++++', '+-++++++++', '+-------++', '+-++++++++', '+-++++++++', '+------+++', '+-+++-++++', '+++++-++++', '+++++-++++', '++++++++++']
answers = 'AGRA;NORWAY;ENGLAND;GWALIOR'


print(crossWordPuzzel(grid, answers.split(';')))
