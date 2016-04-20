"""Advanced skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    top_chars_dict = {}
    unique_chars = set()
    # Create set of unique chars
    for char in phrase:
        if char == " ":
            continue
        else:
            unique_chars.add(char)

    for item in unique_chars:
        occurences = phrase.count(item)
        if occurences in top_chars_dict:
            top_chars_dict[occurences].append(item)
        else:
            top_chars_dict[occurences] = [item]

    top_char = max(top_chars_dict)

    return top_chars_dict[top_char]


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """
    words_dict = {}
    for word in words:
        length = len(word)
        if length in words_dict:
            words_dict[length].append(word)
        else:
            words_dict[length] = [word]

    for key in words_dict:
        words_dict[key] = sorted(words_dict[key])
    return words_dict.items()


#####################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
