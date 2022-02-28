import os

def test_secret():
    expected = "Hello world!"
    actual = os.environ("TEST_VAR")
    assert expected == actual
