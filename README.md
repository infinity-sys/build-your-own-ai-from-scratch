# Build Your Own AI from Scratch

The code for the Infinity Systems YouTube course **Build Your Own AI from Scratch**. Step by step, we build a tiny GPT-style chatbot trained on Egyptian proverbs (English translations). No AI or math knowledge is assumed: every term is defined the first time it appears, and every line of code is explained.

**Prerequisite: basic Python.** You need to be comfortable with variables, lists, dictionaries, `for` loops, `if`, and writing your own functions. The course does not teach Python. Episode 1 includes a short self-check program: if you can predict its output, you are ready.

Playlist: https://www.youtube.com/playlist?list=PLNEAUFhep8gE

Every episode has a folder (`ep01/`, `ep02`, …). Run each script from inside its episode folder; they read the shared dataset at `../data/proverbs.txt`.

## Setup

You need Python 3.11 or newer (the course uses **Python 3.13**). Episodes E01–E06 use only the Python standard library. From E07 we add PyTorch and a few other packages (pinned in `requirements.txt` when those episodes land).

| Platform | Install Python |
|---|---|
| macOS | `brew install python@3.13` |
| Windows | python.org installer (tick "Add python.exe to PATH"), or `winget install Python.Python.3.13` |
| Linux: Ubuntu / Debian | `sudo apt install python3 python3-venv python3-pip` |
| Linux: Fedora | `sudo dnf install python3 python3-pip` |
| Linux: Arch | `sudo pacman -S python python-pip` |

Then, in the repository folder:

```
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # no packages needed yet for E01–E02
cd ep01
python self_check.py
python peek.py
```

`peek.py` should print 20 proverbs, 785 characters, and 27 different characters.

## Episodes

| Episode | Topic | Code |
|---|---|---|
| E01 | What Is a Chatbot, Really? (Course Opener) | [`ep01/`](ep01/) |
| E02 | Text Is Numbers: Characters and Vocabulary | [`ep02/`](ep02/) |
| E03 | Tokens: Words, Characters and Pieces of Words | [`ep03/`](ep03/) |
| E04 | The Bigram Model: Counting What Comes Next | coming soon |
| E05 | Chances, Not Counts: Probability and Sampling from Zero | coming soon |
| E06 | How Good Is Our Model? Measuring Surprise (Loss) | coming soon |
| E07 | Numbers in Grids: Vectors, Matrices and Tensors with PyTorch | coming soon |
| E08 | What Is a Neuron? A Tiny Network, Forward Pass | coming soon |
| E09 | Learning from Mistakes: Slopes and Gradient Descent | coming soon |
| E10 | Backpropagation, Step by Step | coming soon |
| E11 | The Bigram Model as a Neural Network | coming soon |
| E12 | Embeddings: Giving Each Character a Meaning Made of Numbers | coming soon |
| E13 | Looking Back: Using Earlier Characters (Averaging) | coming soon |
| E14 | Self-Attention: Queries, Keys and Values | coming soon |
| E15 | The Transformer Block: Many Heads, Thinking, Shortcuts | coming soon |
| E16 | Assembling Tiny GPT | coming soon |
| E17 | Training on Egyptian Proverbs | coming soon |
| E18 | Sampling: Temperature, Top-k, Careful vs Creative | coming soon |
| E19 | A Simple Chat App: Talk to Your Own AI | coming soon |

## License

MIT, see LICENSE.
