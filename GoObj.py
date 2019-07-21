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
       pass 
    
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
    last_turn_passed = False
    groups = []

    cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']

    def __init__(self, size, groups = []):
        self.size = size
        self.board = Board(size, groups)
        self.cols = self.cols[:size-1]
        self.rows = range(size)
    
    # performs all actions relevant to a turn.  returns true if the game is over
    def next_turn(self):
        self.turn_number += 1
        color = self.teams[self.turn_number%2]
        while True:
            print(f"\n{color}'s turn, where would you like to play?")
            couplet = input("\n> ").upper()
            if couplet == "PASS"
                # TODO implement passing
            if len(couplet) is not 2:
                print('\nPlease specify your move in the form "A9"')
                continue
            if couplet[0] in self.cols and int(couplet[1]) in self.rows:
                coords = couplet_to_coords(couplet)
                break
            else:
                print('\nOut of Bounds')
        move = Group(color, coords, self.size)
        for point in move.get_adjacent_points():
            pass
            # TODO implement this
        return False

    # returns a 2d tuple containing the coords associated with a couplet ex: "A0" -> (0, 0)
    def couplet_to_coords(self, couplet):
        return (self.cols.index(couplet[0]), int(couplet[1]))
    
    # given a set of coords returns the associated couplet ex: (0, 0)
    def coords_to_couplet(self, coords):
        return cols[coords[0]] + str(coords[1])