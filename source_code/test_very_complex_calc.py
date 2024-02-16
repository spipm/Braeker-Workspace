def test_very_complex_function():
    assert very_complex_function(1, 1, 1) == 3**(1/3)
    assert very_complex_function(0, 0, 0) == 0
    assert very_complex_function(-1, -1, -1) == -3**(1/3)
