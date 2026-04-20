from work import add, hello

def test_add():
    assert add(2,5) == 7

def test_hello():
    assert hello("Durai") == "Hello, Durai"
