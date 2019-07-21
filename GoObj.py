"""
All instances of coords are a touple of zero indexed coordinates in the following order: (column, row)
"""

class Group(object):

    liberties = [] # list of coords

    def __init__(self, color, coords, size):
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
    
    # sets the liberties of a group to the given tuple of coords 
    def set_liberties(self, *coords):
        pass

    

class Board(object):

    def __init__(self, size, groups):
        pass
    
    # places a piece at the given coords
    def place(self, color, coords):
        pass
    
    def remove(self, color, coords):
        pass
    
class Game(object):
    
    black_score = 0
    white_score = 6.5

    teams = ('White', 'Black')
    turn_number = 0
    groups = []

    cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']

    def __init__(self, size, groups = []):
        self.board = Board(size, groups)
    
    # performs all actions relevant to a turn.  returns true if the game is over
    def next_turn(self):
        self.turn_number += 1
        color = self.teams[self.turn_number%2]
        print(f"\n{color}'s turn, where would you like to play?")
        input("\n> ")
        return False

    # returns a 2d tuple containing the coords associated with a couplet ex: "A0" -> (0, 0)
    def couplet_to_coords(couplet):
        return (cols.index(couplet[0]), int(couplet[1]))
    
    # given a set of coords returns the associated couplet ex: (0, 0)
    def coords_to_couplet(coords):
        return cols[coords[0]] + str(coords[1])