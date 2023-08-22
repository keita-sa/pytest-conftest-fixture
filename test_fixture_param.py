import pytest


def addition(x, y): # 足し算をして、返す
    return x + y


@pytest.fixture(params=['a', 'b', 'c']) # フィクスチャにパラメータを設定
def fix_param(request):
    if request.param == 'a':
        return (1, 2, 3)
    elif request.param == 'b':
        return (1, 2, 4)
    elif request.param == 'c':
        return (10, 23, 33)


def test_addition(fix_param): # フィクスチャをパラメータ化して、additionを検証
    x, y, result = fix_param
    assert result == addition(x, y)