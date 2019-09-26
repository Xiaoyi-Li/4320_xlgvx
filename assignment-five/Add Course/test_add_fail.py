

import pytest
import add_fail

def test_add_pass():
    ClassesNumber = "111"
    assert add_fail.add_class() == ClassesNumber
