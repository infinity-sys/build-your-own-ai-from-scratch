# E04: The Bigram Model: Counting What Comes Next

Watch: https://youtu.be/ll-k7mSZOyo

Playlist: https://www.youtube.com/playlist?list=PLNEAUFhep8gE

## This episode

```
cd ep04
python check_e03.py
python zip_demo.py
python bigram.py
python follow.py
python heat.py
```

- `check_e03.py`: checks the E03 "your turn" (glue the pair `'s'` + `' '`: 785 → 760 tokens, 25 shorter).
- `zip_demo.py`: `zip(word, word[1:])` pairs every character with the next one.
- `bigram.py`: counts every pair of the training data (first 90%) in a 27 x 27 table `N[a][b]`; t → h 21 times, h → t 0 times.
- `follow.py`: one row of the table, sorted: what comes after `t`.
- `heat.py`: saves the whole table to `heat.json` (for the heatmap) and counts the zeros: 524 of 729 cells.

Run every script from inside `ep04/`; they read `../data/proverbs.txt`. Our real run is saved next to each script (`.txt`). In the video, `heat.py` writes `output/heat.json`; here it writes `heat.json` next to the script. Versions: Python 3.13, standard library only.
