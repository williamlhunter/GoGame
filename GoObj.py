class Group(object):

    def __init__(self, color, x, y):
        self.color = color
        self.points = [(x,y)]
    
    # merges points from another group into this group.  other group should be subsequently deleted.
    def merge(self, other):
        if self.color == other.color:
            self.points += other.points
            self.calc_liberties()
            #TODO fix this
    
    #returns all points adjacent to a group
    def get_adjacent_points(self):
        pass
    

class Board(object):

    groups = []

    def __init__(self, size):
        pass
    
    
    # places a piece at the given coords
    def place(self, color, x, y):
        pass
    
    def remove(self, color):
        pass
    