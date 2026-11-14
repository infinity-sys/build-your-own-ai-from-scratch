# E02: Text Is Numbers: Characters and Vocabulary

Watch: https://youtu.be/vdqmUaTTkyI

Playlist: https://www.youtube.com/playlist?list=PLNEAUFhep8gE

## This episode

```
cd ep02
python exercise.py
python vocab.py
python codec.py
python data_ids.py
python unknown.py
```

- `exercise.py` — checks the E01 "your turn" (adding three proverbs; new letters `j` and `q`).
- `vocab.py` — builds the sorted set of characters (our vocabulary of 27).
- `codec.py` — `stoi` / `itos`, `encode()` and `decode()`, and the round-trip test.
- `data_ids.py` — turns the whole dataset into a list of integer IDs.
- `unknown.py` — what happens when a character is not in the vocabulary (`KeyError`).

Run every script from inside `ep02/`; they read `../data/proverbs.txt`. Our real run is saved next to each script (`.txt`). Versions: Python 3.13, standard library only.
