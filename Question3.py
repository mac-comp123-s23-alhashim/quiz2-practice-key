"""
Python Developer Name: Amin G. Alhashim
"""


def most_frequent_words(s: str) -> dict:
    """
    Compute the frequency of each word in a given string

    :param s: a string
    :return: a dictionary words and their frequencies
    """
    words = s.split()

    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] = word_freq[word] + 1
        else:
            word_freq[word] = 1

    return word_freq


"""
To run the tests, the pytest framework needs to be activated.  To activate the
pytest framework on Pycharm follow these steps:
> go to Pycharm Settings
> Expand Tools
> Expand Python Integrated Tools
> under Testing section -> Default test runner, select pytest
> click Fix to install the module if prompted
"""


def test_most_frequent_words_empty() -> None:
    """
    A unit test for when the input in empty

    :return: None
    """
    assert most_frequent_words('') == {}


def test_most_frequent_words_one_word() -> None:
    """
    A unit test for when the input contain only one word

    :return: None
    """
    assert most_frequent_words('hi') == {'hi': 1}


def test_most_frequent_words_two_same_words() -> None:
    """
    A unit test for when the input contains 2 same words

    :return: None
    """
    assert most_frequent_words('hi hi') == {'hi': 2}


def test_most_frequent_words_three_same_words() -> None:
    """
    A unit test for when the input contains 3 same words

    :return: None
    """
    assert most_frequent_words('hi hi hi') == {'hi': 3}


def test_most_frequent_words_three_diff_words() -> None:
    """
    A unit test when the input contain 3 different words

    :return: None
    """
    assert most_frequent_words('hi1 hi2 hi3') == {'hi1': 1, 'hi2': 1, 'hi3': 1}


def test_most_frequent_words_multiple_words_1() -> None:
    """
    A unit test for when the input more than 3 words
    :return: None
    """
    assert most_frequent_words('hi1 hi2 hi3 hi1 hi2 hi3') == {'hi1': 2,
                                                              'hi2': 2,
                                                              'hi3': 2}


def test_most_frequent_words_multiple_words_2():
    """
    A unit test for when the input more than 3 words
    :return: None
    """
    assert most_frequent_words(
        'the quick brown fox jumped over the lazy dog') == \
           {'brown': 1, 'dog': 1, 'fox': 1, 'jumped': 1, 'lazy': 1, 'over': 1,
            'quick': 1, 'the': 2}
