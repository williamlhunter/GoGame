# GoGame
I'm writing a program that allows two people to play go.  To run it simply run `GoGame.py` in it's directory.

### Phases:
1. Get the game to work accurately in the terminal
    - Allow for moves while remembering state and score
    - Check for illegal moves
    - Implement accurate scoring.  To make this easier, I will use Chinese Scoring
2. Port the program into a webapp using flask
    - Implement a gui
    - Port to browser
3. Allow two people to connect to the webserver, choose sides, and play on separate browsers

### TODO for current phase (1):
- Check for illegal moves (suicide, ko)
- Improve scoring to account for territory held by each side at the end