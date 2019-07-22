class Group(object):

    liberties = [] # list of coords
    points = []

    def __init__(self, color, coords, size):
        self.size = size
        self.color = color
        self.points = [coords]
    
    # merges points from another group into this group.  other group should be subsequently deleted.
    def merge(self, other):
        self.points += other.points
    
    #returns all points adjacent to a group
    def get_adjacent_points(self):
        direction_vectors = ((1, 0), (0, 1), (-1, 0), (0, -1))
        points = []
        for point in self.points:
            for direction in direction_vectors:
                check = (point[0]+direction[0], point[1]+direction[1])
                if check not in self.points and check not in points:
                    if check[0] >= 0 and check[0] < self.size and check[1] >= 0 and check[1] <self.size:
                        points.append(check)
        return points
    
class Board(object):

    str_translator = {None: " + ", "Black": " B ", "White": " W "}

    cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
    
    def __init__(self, size, groups):
        self.size = size
        self.groups = groups
        self.matrix = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(None)
            self.matrix.append(row)
        for group in groups:
            for point in group.points:
                self.matrix[point[0]][point[1]] = group.color
    
    # formats a Board for printing
    def __str__(self):
        formatted = '\n   '
        for i in range(self.size):
            formatted += " " + self.cols[i] + " "
        formatted += '\n\n'
        for ite, row in enumerate(self.matrix):
            formatted += str(ite) + '  '
            for col in row:
                formatted += self.str_translator[col]
            formatted += "\n\n"
        return formatted

    # returns a list of groups that are dead
    def compute_kills(self):
        kills = []
        for group in self.groups:
            liberties = self.find_liberties(group)
            if len(liberties) is 0:
                kills.append(group)
        return kills
    
    # returns a list of liberties for a group
    def find_liberties(self, group):
        liberties = []
        for point in group.get_adjacent_points():
            if self.matrix[point[0]][point[1]] is None:
                liberties.append(point)
        return liberties
    
class Game(object):
    
    score = {"Black": 0, "White": 6.5}

    teams = ('White', 'Black')
    turn_number = 0
    last_turn_passed = False
    groups = []

    cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']

    def __init__(self, size):
        self.size = size
        self.board = Board(size, self.groups)
        self.cols = self.cols[:size-1]
        self.rows = range(size)
    
    # performs all actions relevant to a turn.  returns true if the game is over
    def next_turn(self):
        self.turn_number += 1
        color = self.teams[self.turn_number%2]
        while True:
            print(f"\n{color}'s turn, where would you like to play?")
            couplet = input("\n> ").upper()
            if couplet == "PASS":
                if self.last_turn_passed is False:
                    self.last_turn_passed = True
                    if color is "White":
                        other_color = "Black"
                    else:
                        other_color = "White"
                    self.score[other_color] += 1
                    print("\nPassing Turn")
                    self.print_score()
                    return False
                else:
                    print("\nEnding Game...")
                    print(self.board)
                    return True
            if len(couplet) is not 2:
                print('\nPlease specify your move in the form "A9"')
                continue
            if couplet[0] in self.cols and int(couplet[1]) in self.rows:
                coords = self.couplet_to_coords(couplet)
                break
            else:
                print('\nOut of Bounds')
        move = Group(color, coords, self.size)
        for point in move.get_adjacent_points():
            for group in list(self.groups):
                if group.color is color:
                    if point in group.points:
                        move.merge(group)
                        self.groups.remove(group)
        self.groups.append(move)
        self.board = Board(self.size, self.groups)
        kills = self.board.compute_kills()
        if len(kills) is not 0:
            for kill in kills:
                self.score[color] += len(kill.points)
                self.groups.remove(kill)
            self.board = Board(self.size, self.groups)
        print(self.board)
        self.print_score()
        return False

    # returns a 2d tuple containing the coords associated with a couplet ex: "A0" -> (0, 0)
    def couplet_to_coords(self, couplet):
        return (int(couplet[1]), self.cols.index(couplet[0]))
    
    #prints the score, ugly but easier than making an entire score class with a __str__ method
    def print_score(self):
        print("\nWhite: {}".format(self.score["White"]))
        print("Black: {}".format(self.score["Black"]))