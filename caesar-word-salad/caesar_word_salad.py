import string
import collections
from itertools import islice


def take(n, iterable):
    """Return the first n items of the iterable as a list."""
    return list(islice(iterable, n))


def caesar_word_salad(text, shift=1):
    shifted_result = "".join(
        [
            char
            if char not in string.ascii_lowercase
            else string.ascii_lowercase[
                (string.ascii_lowercase.index(char) + shift) % 26
            ]
            for char in text.lower()
        ]
    )

    commons = get_common_letters(shifted_result)
    if shift == 26:
        return
    elif not contains_most_common_letters(commons):
        print(f"not found, shift {shift}, continue")
        caesar_word_salad(text, shift=shift + 1)
    else:
        print(shifted_result)
        print("found in shift", shift)


def contains_most_common_letters(items):
    common_letters = ["e", "t", "a", "i", "o", "n"]
    print(items)
    counts = [key for key, _ in items if key in common_letters]
    return len(counts) > 2


def get_common_letters(text, top=5):
    counter = collections.Counter(text)
    sorted_letters = {
        k: v for k, v in sorted(counter.items(), key=lambda item: item[1], reverse=True)
    }

    return take(top, sorted_letters.items())
