"""Skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different::

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """
    # Using a set to remove duplicates and then return a list
    return list(set(words))


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    # Using set math to find the intersection of the two lists
    unique_common_items = set(items1) & set(items2)
    return list(unique_common_items)


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    count_words_dict = {}
    words = phrase.split()
    for word in words:
        if word in count_words_dict:
            count_words_dict[word] += 1
        else:
            count_words_dict[word] = 1
    return count_words_dict


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    # Create a dictionary that maps English words to their Pirate counterparts
    pirate_dict = {
        "sir": "matey",
        "hotel": "fleabag inn",
        "student": "swabbie",
        "boy": "matey",
        "girl": "matey",
        "man": "matey",
        "professor": "foul blaggart",
        "restaurant": "galley",
        "your": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "restroom": "head",
        "my": "me",
        "is": "be"
    }
    words = phrase.split()
    pirate_phrase = []
    for word in words:
        if word.lower() in pirate_dict:
            pirate_phrase.append(pirate_dict[word.lower()])
        else:
            pirate_phrase.append(word)
    pirate_phrase = " ".join(pirate_phrase)
    return pirate_phrase


def sort_by_word_length(words):
    """Given list of words, return list of ascending (len, [words]).

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- the length
    of the words for that word-length, and the list of words of
    that word length.

    For example::

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]
    """
    # Create dictionary to store the len of the words as keys and the
    # matching words in a list as values.
    word_length_dict = {}
    for word in words:
        if len(word) in word_length_dict:
            word_length_dict[len(word)].append(word)
        else:
            word_length_dict[len(word)] = [word]
    return sorted(word_length_dict.items())


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
    sum_zero_pairs = {}
    # Top for loop provides starting point and item to check.
    for idx, num in enumerate(numbers):
        # Loops through the rest of the items in the list to check to
        # sum of zero. Starts at idx to handle 0.
        for x in range(idx, len(numbers)):
            if num + numbers[x] == 0:
                # Second check makes sure that the pairs aren't repeated
                # (i.e. key value -1: 1 and 1: -1 should not both be included).
                if numbers[x] in sum_zero_pairs:
                    continue
                else:
                    sum_zero_pairs[num] = numbers[x]
    # What would be a better way to return lists?
    sum_zero_pairs = sum_zero_pairs.items()
    list_sum_zero_pairs = []
    for item in sum_zero_pairs:
        list_sum_zero_pairs.append(list(item))
    return list_sum_zero_pairs


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    # Create dictionary of first letter keys tied to a list of the
    # applicable names as values.
    first_letter_names = {}
    for name in names:
        if name[0] in first_letter_names:
            first_letter_names[name[0]].append(name)
        else:
            first_letter_names[name[0]] = [name]
    # Start results with the first name provided.
    results = [names[0]]
    # Remove name from dictionary.
    first_letter_names[results[0][0]].remove(results[0])
    # Set last_letter to the last letter of the last name in the results.
    last_letter = results[-1][-1]
    # While loop runs until the last letter is not in the dictionary, or
    # until the list of potential names starting with that letter is exhausted.
    while last_letter in first_letter_names:
        try:
            next_name = first_letter_names[last_letter].pop(0)
            # Check to see if name has alread been used (in case duplicate
            # names are entered). If it has, move on to the next name.
            if next_name in results:
                next_name = first_letter_names[last_letter].pop(0)
            results.append(next_name)
            last_letter = results[-1][-1]
        # If pop tries to pull from an empty list, end loop.
        except IndexError:
            break
    return results


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
