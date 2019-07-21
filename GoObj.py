class Board(object):

    groups = {}
    black_score = 0
    white_score = 6.5

    def __init__(self, size):
        self.size = size
        self.grid = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(Point(i, j))
            grid.append(row)
    
    
    # places a piece at the given 
    def place(self, color, x, y):
        pass
    
    def 
    
class Point(object):

    color = None

    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y
    
    def place(self, color):
        if color is None:
            self.color = color
        else:
            raise Exception ('tried to place a stone where there is already one')
    
    def remove(self)
        if color is 'white' or color is 'black'
            color = None
        else:
            raise Exception('Tried to remove a stone where there is none')

class Group(object):

    def __init__(self):
        pass
    
    # returns a list with all the liberties for a group
    def get_liberties(self, board):
        pass
    
    # reutrns the number of liberties of a group
    def get_num_liberties(self, board):
        pass
    
    # returns the coords of the members of a group
    def get_members(self):
        pass
        