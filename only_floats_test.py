from only_floats import only_floats

def test_two_floats():
	assert only_floats(2.3, 5.4) == 2
 
def test_neither_floats():
	assert only_floats(2, 5) == 0

def test_one_float_test():
	assert only_floats(2.3, 5) == 1