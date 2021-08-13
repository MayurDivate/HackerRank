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
            return 'Vr: '+self.value +' in row '+str(self.pos)+' from '+str(self.start)+ ' to '+str(self.end)


class CrossWordGrid(CrossWord):

    def print_me(self):
        print(self.value, self.col, self.row)


class CrossWordAnswer(CrossWord):

    def test(self):
        pass


class CrossWordPuzzel():

    def __init__(self, grid, answers):
        self.grid = grid
        self.answers = answers
        self.crossWordGrid = self.getCrossWordGrid()

    def getCrossWordGrid(self):

        crossWordGrids = {}

        for i, row in enumerate(self.grid):
            col = ''.join([self.grid[j][i] for j in range(len(self.grid))])

            re_matches = re.finditer(r'\-\-+', row)
            for match in re_matches:
                crossWordGrids[(CrossWordGrid(match.group(), i, match.span()[0], match.span()[1], True))] = []

            re_matches = re.finditer(r'\-\-+', col)
            for match in re_matches:
                crossWordGrids[(CrossWordGrid(match.group(), i, match.span()[0], match.span()[1], False))] = []

        return crossWordGrids

    def fill_answers(self):
        for word in self.answers:
            for g in self.crossWordGrid.keys():
                if len(word) == len(g.value):
                    self.crossWordGrid[g].append(word)
                    print(g.toString(), self.crossWordGrid[g])

#grid = ['+-++++++++',  '+-++++++++', '+-++++++++', '+-----++++', '+-+++-++++', '+-+++-++++', '+++++-++++', '++------++', '+++++-++++', '+++++-++++']
#answers = 'LONDON;DELHI;ICELAND;ANKARA'

#grid = ['++++++-+++', '++------++', '++++++-+++', '++++++-+++', '+++------+', '++++++-+-+', '++++++-+-+', '++++++++-+', '++++++++-+', '++++++++-+']
#answers = 'ICELAND;MEXICO;PANAMA;ALMATY'

grid = ['+-++++++++', '+-++++++++', '+-------++', '+-++++++++', '+-++++++++', '+------+++', '+-+++-++++', '+++++-++++', '+++++-++++', '++++++++++']
answers = 'AGRA;NORWAY;ENGLAND;GWALIOR'

cwf = CrossWordPuzzel(grid, answers.split(';'))

cwf.fill_answers()


#cw = CrossWordPuzzel(grid, answers.split(';'))
#out = cw.fillCrosswordPuzzle()
#print(*out,sep='\n')
#fill_word(['+-----++++'], 'mayur')