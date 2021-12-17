# SeroChess - PWS Chess engine
This a Python-based chess engine for our PWS.
## About
This chess engine is Lisa Vrins, Kuno Zeldenrust and Anbiya Popal's PWS (profielwerkstsuk) project. We've chosen Python as our language because it is convenient to explain algorithms in our report.

Sero is latin for 'too late'. The chess engine is relatively slow, so we've chosen 'Sero' to name the engine.

## Features
* Chess engine that uses MiniMax with alpha-beta pruning

* Capable searching at depth 4 in ±1 minute

* Python [arcade](https://arcade.academy/) GUI to play chess or debug chess-related code

## How to play
To play the chess engine, you need to have ```arcade``` and ```rich``` installed.

To install these, run the following:

```pip install arcade```

```pip install rich```

Then, run the file with the following command and paramenters:

```python src/main.py [mode] [white player] [black player] -d [depth]```

For the player type, use 'player' or 'computer'. The depth field is irrelevant when two players are playing against eachother.