# E06: How Good Is Our Model? Measuring Surprise (Loss)

Playlist: https://www.youtube.com/playlist?list=PLNEAUFhep8gE

## This episode

```
cd ep06
python check_e05.py
python surprise.py
python loss.py
python zeros.py
python smooth.py
```

- `check_e05.py`: checks the E05 "your turn" (the row of `e` as probabilities): a space after e is 0.36 (32/90), bigger than after t (0.28).
- `surprise.py`: `-math.log(p)` turns a probability into a surprise score. When p is 1 the surprise is 0; when p is 0.01 the surprise is 4.61. `max(0.0, …)` turns a minus zero into a plain 0.0 when p is 1.
- `loss.py`: the unsmoothed training loss, average negative log-likelihood over 705 training pairs: 2.04.
- `zeros.py`: six pairs in the validation text (the last 10%) have probability 0, including g→e and e→t in the new word `get`, and t→y in `dirty`. `-math.log(0)` is not a useful score.
- `smooth.py`: add-one smoothing, `p = (count + 1) / (total + V)` with V = 27. Training loss 2.39, validation loss 2.57. Both are finite, and val is higher than train.

Run every script from inside `ep06/`; they read `../data/proverbs.txt` (`surprise.py` needs no data). Our real run is saved next to each script (`.txt`). Versions: Python 3.13, standard library only.
