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

    def __init__(self, matrix, crossWordGrids, answers):
        self.matrix = matrix
        self.crossWordGrids = crossWordGrids
        self.solution = {ans: [] for ans in answers}

    def get_possible_answers(self):
        for word in self.solution.keys():
            for g in self.crossWordGrids:
                if len(word) == len(g.value):
                    self.solution[word].append(g)

    def updateGrid(self):
        # update positions with only one possible answer

        for ans in self.solution.keys():
            if len(self.solution[ans]) == 1:
                for g in self.solution[ans]:
                    assert isinstance(g, CrossWordGrid)

                    if g.isHorizontal:
                        self.fill_horizontal(ans, g)
                    else:
                        print(g.value, 'col', ans, g.pos, 'from',g.start, 'end', g.end )
                        self.fill_vertical(ans, g)
            
    def fill_horizontal(self, word, grid):

        assert isinstance(grid, CrossWordGrid)

        gx = self.matrix[grid.pos]
        gx = gx[:grid.start]+word+gx[grid.end:]
        self.matrix[grid.pos] = gx

    def fill_vertical(self, word, grid):

        assert isinstance(grid, CrossWordGrid)

        for row in range(grid.start, grid.end):
            gx = self.matrix[row]
            gx = gx[:grid.pos] + word[len(word) - row] + gx[ grid.pos+1 :]
            self.matrix[row] = gx


    def print_solution(self):
        for word in self.solution.keys():
            for grid in self.solution[word]:
                print(word, grid.toString())


    def print_matrix(self):
        print(*self.matrix, sep='\n')

#grid = ['+-++++++++',  '+-++++++++', '+-++++++++', '+-----++++', '+-+++-++++', '+-+++-++++', '+++++-++++', '++------++', '+++++-++++', '+++++-++++']
#answers = 'LONDON;DELHI;ICELAND;ANKARA'

#grid = ['++++++-+++', '++------++', '++++++-+++', '++++++-+++', '+++------+', '++++++-+-+', '++++++-+-+', '++++++++-+', '++++++++-+', '++++++++-+']
#answers = 'ICELAND;MEXICO;PANAMA;ALMATY'

grid = ['+-++++++++', '+-++++++++', '+-------++', '+-++++++++', '+-++++++++', '+------+++', '+-+++-++++', '+++++-++++', '+++++-++++', '++++++++++']
answers = 'AGRA;NORWAY;ENGLAND;GWALIOR'


def crossWordPuzzel(grid, answers):
    crossWordGrids = []

    for i, row in enumerate(grid):
        col = ''.join([grid[j][i] for j in range(len(grid))])

        re_matches = re.finditer(r'\-\-+', row)
        for match in re_matches:
            crossWordGrids.append((CrossWordGrid(match.group(), i, match.span()[0], match.span()[1], True)))

        re_matches = re.finditer(r'\-\-+', col)
        for match in re_matches:
            crossWordGrids.append((CrossWordGrid(match.group(), i, match.span()[0], match.span()[1], False)))

    return CrossWordPuzzel(grid,crossWordGrids, answers)


cwp = crossWordPuzzel(grid, answers.split(';'))
cwp.get_possible_answers()
cwp.print_solution()
cwp.updateGrid()
cwp.print_matrix()


