# Number Guessing Game & Word Counter

A beginner-friendly Python terminal project that combines a number guessing game with a text-file analysis tool.

## Features

### Number Guessing Game
- Generates a random number from 1 to 100.
- Gives **Too low** and **Too high** hints.
- Allows up to 7 valid guesses.
- Awards a higher score for fewer attempts.
- Handles invalid input and out-of-range guesses.

### Word Counter
- Reads a UTF-8 text file.
- Counts total words, characters, and unique words.
- Shows the frequency of each word.
- Ignores capitalization and punctuation when counting words.
- Includes `sample.txt` so you can try it immediately.

## Requirements
- Python 3.9 or newer; no third-party packages required.

## How to Run
1. Open a terminal in this folder.
2. Run `python main.py`. If that does not work, try `python3 main.py` or `py main.py`.
3. Choose `1` to play, `2` to analyze a text file, or `3` to exit.
4. For the Word Counter, press Enter at the file-path prompt to use `sample.txt`, or type a path to another text file.

## Concepts Practiced
- Variables, loops, conditionals, and functions
- `random` for number generation
- Input validation and exception handling
- File handling with `pathlib`
- String processing with regular expressions
- Word-frequency analysis with `collections.Counter`

## Project Structure
```text
number-guessing-word-counter/
├── main.py
├── sample.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Author
Harshada Bharti

## License
MIT. See `LICENSE`.
