import demo as m


def test_add() -> None:
    assert m.__version__ == ""
    assert m.add(1, 2) == 3
    assert m.subtract(1, 2) == -1
