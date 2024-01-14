from odd_positions import odd_positions

def test_odd_postions():
	grades = [56, 90, 100, 67, 88, 99, 99, 77]
	assert odd_positions(grades) == [56, 100, 88, 99]