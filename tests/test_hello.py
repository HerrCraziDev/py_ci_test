import pytest
from greeter.hello import Hello


@pytest.mark.unit
def test_hello():
    hello = Hello()
    assert hello.name == "World"

    hello = Hello("user")
    assert hello.name == "user"


@pytest.mark.unit
def test_hello_greeter():
    hello = Hello()
    assert hello.greet() == "Hello World!"


@pytest.mark.unit
def test_hello_set_name():
    hello = Hello()
    name = "toto"
    hello.set_name(name)
    assert hello.name == name
    assert hello.greet() == f"Hello {name}!"
