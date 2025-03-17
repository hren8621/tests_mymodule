import pytest
from mymodule import mylib
import matplotlib
import kivy

class Tests:

    @pytest.fixture
    def mymod(self):
        """Fixture to create a new PopupMessage instance before each test"""
        ml_instance = mylib.MySimpleModule()
        return ml_instance
        
    # Test functions
    def test_sanity_check(self):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    def test_initializations(self, mymod):
        assert mymod._msg == "my default msg"
        assert mymod._count == 1