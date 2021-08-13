import re


class CrossWord:

    def __init__(self, value, pos, start, end, isHorizontal):
        self.value = value
        self.pos = pos
        self.start = start
        self.end = end
        self.isHorizontal = isHorizontal

    def toString(self):

        if self.isHorizontal:
            return 'Hz: '+self.value+' in row '+ str(self.pos)+' from '+ str(self.start)+' to '+str(self.end)
        else:
            return 'Vr: '+self.value +' in col '+str(self.pos)+' from '+str(self.start)+ ' to '+str(self.end)

    def __hash__(self):
        return hash(self.toString())

class CrossWordGrid(CrossWord):

    def isOverlapping(self, grid2):

        if self.isHorizontal != grid2.isHorizontal:
            if (self.pos >= grid2.start) and (self.pos <= grid2.end):
                if (self.start <= grid2.pos) and (self.end >= grid2.pos):
                    return True

        return False


class CrossWordPuzzel():

    def __init__(self, crossWordGrids, answers):
        self.crossWordGrids = crossWordGrids
        self.solution = {ans: [] for ans in answers}


    def fill_answers(self):
        for word in self.solution.keys():
            for g in self.crossWordGrids:
                if len(word) == len(g.value):
                    self.solution[word].append(g)

    def print_solution(self):
        for word in self.solution.keys():
            for grid in self.solution[word]:
                print(word, grid.toString())

    def test(self):
        for g in self.crossWordGrids:
            for g2 in self.crossWordGrids:
                if g != g2:
                    print(g.toString() , g.isOverlapping(g2), g2.toString(), sep='\t')

#grid = ['+-++++++++',  '+-++++++++', '+-++++++++', '+-----++++', '+-+++-++++', '+-+++-++++', '+++++-++++', '++------++', '+++++-++++', '+++++-++++']
#answers = 'LONDON;DELHI;ICELAND;ANKARA'

#grid = ['++++++-+++', '++------++', '++++++-+++', '++++++-+++', '+++------+', '++++++-+-+', '++++++-+-+', '++++++++-+', '++++++++-+', '++++++++-+']
#answers = 'ICELAND;MEXICO;PANAMA;ALMATY'

grid = ['+-++++++++', '+-++++++++', '+-------++', '+-++++++++', '+-++++++++', '+------+++', '+-+++-++++', '+++++-++++', '+++++-++++', '++++++++++']
answers = 'AGRA;NORWAY;ENGLAND;GWALIOR'


def crossWordPuzzel(grind, answers):
    crossWordGrids = []

    for i, row in enumerate(grid):
        col = ''.join([grid[j][i] for j in range(len(grid))])

        re_matches = re.finditer(r'\-\-+', row)
        for match in re_matches:
            crossWordGrids.append((CrossWordGrid(match.group(), i, match.span()[0], match.span()[1], True)))

        re_matches = re.finditer(r'\-\-+', col)
        for match in re_matches:
            crossWordGrids.append((CrossWordGrid(match.group(), i, match.span()[0], match.span()[1], False)))

    return CrossWordPuzzel(crossWordGrids, answers)


cwp = crossWordPuzzel(grid, answers.split(';'))

cwp.fill_answers()

cwp.print_solution()
cwp.test()


