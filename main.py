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
    contents = get_book_text("./books/frankenstein.txt")
    num_words = word_count(contents)
    output = character_count(contents)
    sorted_list_of_characters = sorted_list(output)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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