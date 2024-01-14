from even_positions import even_positions

def test_even_positions():
	grades = [80, 39, 88, 90, 12, 78]
	assert even_positions(grades) == [39, 90, 78]