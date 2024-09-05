from ..hw2_debugging import mergeSort


def test_random_arr():
    arr = [4, 52, 6, 43, 62, 5, 8, 1]

    assert mergeSort(arr) == [1, 4, 5, 6, 8, 43, 52, 62]


def test_already_sorted():
    arr = [1, 4, 5, 6, 8, 43, 52, 62]

    assert mergeSort(arr) == [1, 4, 5, 6, 8, 43, 52, 62]


def test_reverse_sorted():
    arr = [62, 52, 43, 8, 6, 5, 4, 1]

    assert mergeSort(arr) == [1, 4, 5, 6, 8, 43, 52, 62]
