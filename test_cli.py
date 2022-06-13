import pytest
from cli import bye

def test_hello_world():
    assert bye() == 'Bye World!'