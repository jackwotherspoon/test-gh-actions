import os

def test_secret():
    print("TESTING VARIABLES!")
    expected = "Hello"
    actual = os.environ["TEST_VAR"]
    assert expected == actual
