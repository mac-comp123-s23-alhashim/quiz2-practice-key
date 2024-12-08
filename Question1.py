"""
Python Developer Name: Amin G. Alhashim
"""


def unique_words(s: str) -> list:
    """
    Process a given string to return the unique words

    :param s: a string
    :return: list of unique words
    """
    uw_list = []
    for word in s.split():
        if word not in uw_list:
            uw_list.append(word)

    return uw_list


"""
To run the tests, the pytest framework needs to be activated.  To activate the
pytest framework on Pycharm follow these steps:
> go to Pycharm Settings
> Expand Tools
> Expand Python Integrated Tools
> under Testing section -> Default test runner, select pytest
> click Fix to install the module if prompted
"""


def test_unique_words_empty() -> None:
    """
    A unit test for when the input is empty

    :return: None
    """
    s = ''
    expected_list = []

    assert set(unique_words(s)) == set(expected_list)


def test_unique_words_one_word() -> None:
    """
    A unit test for when the input contains one word

    :return: None
    """
    s = 'hi'
    expected_list = ['hi']

    assert set(unique_words(s)) == set(expected_list)


def test_unique_words_two_same_words() -> None:
    """
    A unit test for when the input contains 2 same words

    :return: None
    """
    s = 'hi hi'
    expected_list = ['hi']

    assert set(unique_words(s)) == set(expected_list)


def test_unique_words_three_same_words() -> None:
    """
    A unit test for when the input contains 3 same words

    :return: None
    """
    s = 'hi hi hi'
    expected_list = ['hi']

    assert set(unique_words(s)) == set(expected_list)


def test_unique_words_multiple_different_words() -> None:
    """
    A unit test for when the input contains multiple different words

    :return: None
    """
    s = 'hi1 hi2 hi3 hi1 hi2 hi3'
    expected_list = ['hi1', 'hi2', 'hi3']

    assert set(unique_words(s)) == set(expected_list)
