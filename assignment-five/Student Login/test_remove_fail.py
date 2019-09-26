import pytest
import remove_fail

def test_remove_pass():
    StudentsID = "5678"
    assert remove_fail.remove_student() == StudentsID
