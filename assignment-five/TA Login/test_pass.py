import pytest
import TAlogin_pass

def test_login_pass():
    TAname = "TA"
    password = "password"  
    assert TAlogin_pass.get_login_password() == password and TAlogin_pass.get_login_TAname() == TAname
