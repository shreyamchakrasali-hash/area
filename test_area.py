from area import area_circumference

def test_area_circumference():
    result = area_circumference(5)
    expected = "Area:78.53981633974483, Circumference:31.41592653589793"
    assert result == expected
