import pytest
import remove_pass

def test_remove_pass():
    TAsID = "1234"
    assert remove_pass.remove_ta() == TAsID
