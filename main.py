import sys
from stats import word_count, character_count, sorted_list

def get_book_text(filepath):
    """
    @filepath: string: the file path of the file
    @return: string: contents of the file
    """
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_name = sys.argv[1]
    contents = get_book_text(file_name)
    num_words = word_count(contents)
    output = character_count(contents)
    sorted_list_of_characters = sorted_list(output)

    print("============ BOOKBOT ============")
    print(f"Analysing book found at {file_name}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list_of_characters:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
        else:
            pass
    print("============= END ==============")
    return

if __name__ == "__main__":
    main()