import pytest

def setup_function(function):
    print("Lunching Browser---")
def teardown_function(function):
    print("Quitting Browser---")

def test_doLogin0():
    print("Executing First Test Case")
def test_doLogin1():
    print("Executing Second Test Case")

