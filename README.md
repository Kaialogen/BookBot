# BookBot
- BookBot is a Python CLI application that does data analysis on books provided as text files. It computes various statistics such as word count, unique words, average word length, and the most common words.

## Usage

```bash
uv run main.py <path_to_book>
```
Replace `<path_to_book>` with the path to the text file of the book you want to analyse.

Example data can be found using:
```bash
wget -O books/mobydick.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/mobydick.txt
wget -O books/prideandprejudice.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/prideandprejudice.txt
```

## Testing
To run the tests, use:
```bash
uv run pytest
```
