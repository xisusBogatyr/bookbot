import sys
from stats import get_num_words, get_num_of_each_character, sort_dict_by_value


def get_book_text(path_to_file: str):
    """
    Reads the contents of a text file and returns it as a string.
    """
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if sys.argv.__len__() != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return 1
    book_to_analyze = sys.argv[1]

    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {book_to_analyze}...")
    book_text = get_book_text(book_to_analyze)
    
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")

    print("--------- Character Count -------")
    char_counts = get_num_of_each_character(book_text)
    char_counts = sort_dict_by_value(char_counts)
    for char, count in char_counts.items():
        print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
