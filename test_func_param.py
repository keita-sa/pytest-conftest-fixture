import pytest


def addition(x, y):
    """
    足し算をして、返す
    """
    return x + y


# テスト関数のパラメータ化
@pytest.mark.parametrize(
    "x, y , result",
    [   (1, 2, 3),
        (1, 2, 4), #
        (10, 23, 33)
    ],
)
def test_addition(x, y, result):
    """
    関数をパラメータ化して、additionを検証
    """
    assert result == addition(x, y)