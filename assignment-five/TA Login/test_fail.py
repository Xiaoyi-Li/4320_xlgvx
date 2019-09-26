import pytest
import TAlogin_fail

def test_login_pass():
    TAname = "TA"
    password = "password"  
    assert TAlogin_fail.get_login_password() == password and TAlogin_fail.get_login_TAname() == TAname
