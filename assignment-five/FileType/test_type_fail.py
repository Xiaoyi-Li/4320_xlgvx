import pytest
import type_fail

def test_type_pass():
    FilesType = "pdf"
    assert type_fail.file_type() == FilesType

