from divide_or_square import divide_or_square

def test_is_divisible():
	assert divide_or_square(30) == 5.477225575051661
	

def test_is_not_divisible():
	assert divide_or_square(17) == 2 