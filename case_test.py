from main import symmetric_difference


def test_simple_case():
    # sym([1, 2, 3], [5, 2, 1, 4]) should return [3, 4, 5].
    a = [1, 2, 3]
    b = [5, 2, 1, 4]
    response = symmetric_difference([a, b])

    print(response == [3, 4, 5])
    assert response == [3, 4, 5]
