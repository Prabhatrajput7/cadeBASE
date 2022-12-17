import pytest

@pytest.mark.smoke
def test_f11():
    t = 'test'
    assert t == 'test','your tc failed'

@pytest.mark.skip
def test_f22():
    a = 4
    b = 5
    assert a + b == 10, 'Fail'

