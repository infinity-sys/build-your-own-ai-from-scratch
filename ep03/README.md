# E03: Tokens: Words, Characters and Pieces of Words

Playlist: https://www.youtube.com/playlist?list=PLNEAUFhep8gE

## This episode

```
cd ep03
python check_e02.py
python words.py
python unknown_word.py
python pairs.py
python merge.py
python split.py
```

- `check_e02.py`: checks the E02 "your turn" (encode a word, find the characters missing from `stoi`).
- `words.py`: word tokens with `split()`: 159 words, 100 different words.
- `unknown_word.py`: a new word (`patiently`) is unknown to a word tokenizer but fine for a character tokenizer.
- `pairs.py`: counts neighbour pairs with `zip`, the first step of byte pair encoding (BPE).
- `merge.py`: one BPE merge by hand: glue `'e'` + `' '` into `'e '` (785 → 751 tokens).
- `split.py`: 90% training data, 10% validation data (706 and 79 IDs).

Run every script from inside `ep03/`; they read `../data/proverbs.txt`. Our real run is saved next to each script (`.txt`). Versions: Python 3.13, standard library only.
