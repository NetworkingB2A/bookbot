

def _sort_on(items):
    return items["num"]

def get_number_of_words(text: str) -> int:
    return len(text.split())

def get_char_dict(text: str) -> dict[str, int]:
    letter_count = {}
    for letter in text:
        letter = letter.lower()
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def get_sorted_dict_list(unsorted: dict[str, int]) -> list[dict[str, int]]:
    temp_list = [ {"char": key, "num": value} for key, value in unsorted.items()]
    temp_list.sort(reverse=True, key=_sort_on)
    return temp_list
