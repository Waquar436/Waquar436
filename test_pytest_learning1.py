import pytest
# def method1():
#     print("Hello world")

@pytest.mark.smoke
def test_method1():
    print("This is pytest method.")
    assert 1-1 == 2
@pytest.mark.smoke
def test_method2():
    print("test2")
    assert 1+1 == 2