import pytest
import add_pass

def test_add_pass():
    ClassesNumber = "111"
    assert add_pass.add_class() == ClassesNumber
