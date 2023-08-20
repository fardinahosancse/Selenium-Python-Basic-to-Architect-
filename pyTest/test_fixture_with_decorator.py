import pytest
from colorama import Fore,Back,Style


@pytest.fixture(scope="module")
def setup_for_module():
    print(Back.GREEN+"DB CONNECTION CREATING >>>>>>>>>")
    yield #like teardown function
    print(Fore.RED +"DB CONNECTION CLOSING <<<<<<<<<<")

@pytest.fixture(scope="function")
def setup_for_function():
    print(Back.GREEN+"BROWSER OPENING >>>>>>>>>")
    yield
    print(Fore.RED +"BROWSER CLOSING <<<<<<<<<")

def test_doLogin0(setup_for_module,setup_for_function):
    print(" ")
    print(Back.GREEN+" Executing First Test Case")
def test_doLogin1(setup_for_module,setup_for_function):
    print(" ")
    print(Back.GREEN+" Executing Second Test Case")

