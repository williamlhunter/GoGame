import GoObj as go

def main():
    print('\nWhat size of a board do you want to play on?')
    print('Available options are "9x9" "13x13" and "19x19":')
    size_dict = {"9x9": 9, "13x13": 13, "19x19": 19}
    size = size_dict.get(input("\n> "), "19x19")
    print(f"Starting a new game on a {size}x{size} board.")
    game = go.Game(size)
    while not game.next_turn():
        pass
    print(f"\nBlack's score: {game.black_score}")
    print(f"White's score: {game.white_score}")
    if game.white_score > game.black_score:
        winner = "Black"
    else:
        winner = "White"
    print(f"\nCongradulations {winner}!")

main()