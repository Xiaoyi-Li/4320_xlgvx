import pytest
import remove_pass

def test_remove_pass():
    StudentsID = "5678"
    assert remove_pass.remove_student() == StudentsID
