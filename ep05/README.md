# E05: Chances, Not Counts: Probability and Sampling

Watch: https://youtu.be/0uhrToAoSW0

Playlist: https://www.youtube.com/playlist?list=PLNEAUFhep8gE

## This episode

```
cd ep05
python check_e04.py
python probs.py
python dice.py
python generate.py
```

- `check_e04.py`: checks the E04 "your turn" (the row of the space, sorted): words most often start with `t` (17), then `i` (13) and `w` (11).
- `probs.py`: turns the row of `t` into probabilities by dividing each count by the total (58): h 0.36, space 0.28, o 0.09, t 0.07; the whole row adds up to 1.0.
- `dice.py`: `random.choices` as a weighted dice (sides h, space, o with weights 21, 16, 5), 20 rolls with `random.seed(1)`: 11 h, 7 spaces, 2 o.
- `generate.py`: our bigram model writes five proverbs, one character at a time, starting and stopping at the new line character (`random.seed(27)`).

Run every script from inside `ep05/`; they read `../data/proverbs.txt` (`dice.py` needs no data). Our real run is saved next to each script (`.txt`); with the same seed you get the same output. Versions: Python 3.13, standard library only.
