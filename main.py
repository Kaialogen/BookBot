
def get_book_text(filepath):
    """
    @filepath: string: the file path of the file
    @return: string: contents of the file
    """
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    """
    @text: string: The books content to count
    @return: number: number of words in the text
    """
    count = len(text.split())
    return count

def main():
    contents = get_book_text("./books/frankenstein.txt")
    num_words = word_count(contents)
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()