import pytest

@pytest.mark.smoke
def test_login():
    print("Executing Login TestCase")

@pytest.mark.functional
def test_userReg():
    print("Executing User Regsitration TestCase")

@pytest.mark.smoke
def test_comment():
    print("Executing Comment TestCase")

@pytest.mark.regression
def test_like():
    print("Executing Like TestCase")


