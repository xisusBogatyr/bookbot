def get_num_words(text: str):
    """
    Counts the number of words in a given text string.
    """
    words = text.split()
    return len(words)


def get_num_of_each_character(text: str):
    """
    Counts the number of occurrences of each character in the given text.

    The function:
    - Converts the text to lowercase.
    - Removes all whitespace characters.
    - Returns a dictionary where each key is a character and each value is the count of that character.

    Args:
        text (str): The input string to analyze.

    Returns:
        dict: A dictionary mapping each character to its count in the text.
    """
    lowercased_text = "".join(text.split()).lower().strip()
    char_counts = {}
    for char in lowercased_text:
        if not char.isalpha():
            continue
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_dict_by_value(d: dict):
    """
    Sorts a dictionary by its values in descending order.

    Args:
        d (dict): The dictionary to sort.

    Returns:
        dict: A new dictionary sorted by values in descending order.
    """
    sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_items)
