def add(x : int, y : int) -> int:
    assert type(x) == "int"
    assert type(y) == "int"
    return x + y

def testAdd(x: int, y : int) -> int:
    assert add(x, y) == (x + y)