import go_obj

def main():
    print('\nWhat size of a board do you want to play on?')
    print('Available options are "9x9" "13x13" and "19x19":')
    size_dict = {"9x9": 9, "13x13": 13, "19x19": 19}
    size = size_dict.get(input("\n> "), 19)
    print(f"\nStarting a new game on a {size}x{size} board.")
    game = go_obj.Game(size)
    while not game.next_turn():
        pass
    print("\nBlack's score: {}".format(game.score["Black"]))
    print("White's score: {}".format(game.score["White"]))
    if game.score["Black"] > game.score["White"]:
        winner = "Black"
    else:
        winner = "White"
    print(f"\nCongratulations {winner}!\n")

main()