from stats import word_count, character_count

def get_book_text(filepath):
    """
    @filepath: string: the file path of the file
    @return: string: contents of the file
    """
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    contents = get_book_text("./books/frankenstein.txt")
    num_words = word_count(contents)
    print(f"Found {num_words} total words")
    output = character_count(contents)
    print(output)

if __name__ == "__main__":
    main()