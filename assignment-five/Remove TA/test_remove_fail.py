import pytest
import remove_fail

def test_remove_pass():
    TAsID = "1234"
    assert remove_fail.remove_ta() == TAsID
