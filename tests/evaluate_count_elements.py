from count_elements import count_elements


def test_count_elements():
    assert count_elements([45, 46, 47, 48, 52, 60], [34, 45, 18, 20, 35, 40, 50, 65, 75]) == ([3, 3, 3, 3, 2, 2], 54)
    assert count_elements([45, 46, 47, 48, 52, 60], [87, 89, 80, 78, 90, 38, 32, 45, 58]) == ([6, 6, 6, 6, 6, 5], 54)
    assert count_elements([1, 2, 0, 4], [1, 1, 1, 1, 1, 1, 1, 1, 1]) == ([0, 0, 9, 0], 36)
    assert count_elements([10, 2, 5, 23], [16, 87, 5, 9, 1, 3, 8, 22, 34]) == ([4, 8, 6, 2], 36)
    assert count_elements([45, 46, 47, 48, 52, 60], [16, 87, 5, 9, 1, 3, 8, 22, 34]) == ([1, 1, 1, 1, 1, 1], 54)
    assert count_elements([90, 79, 10, 18, 99, 31, 23, 5, 8], [10, 12, 102, 89, 52, 60]) == (
    [1, 2, 5, 4, 1, 4, 4, 6, 6], 54)
    assert count_elements([23, 23, 23, 23, 23, 23, 23, 23, 23], [23, 23, 23, 23, 23, 23]) == (
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 54)
    assert count_elements([230, 230, 230, 230, 230, 230, 230, 230, 230], [2300, 2300, 230, 53, 203, 213]) == (
    [2, 2, 2, 2, 2, 2, 2, 2, 2], 54)
