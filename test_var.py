import os

def test_secret():
    expected = "Hello"
    actual = os.environ["TEST_VAR"]
    assert expected == actual
