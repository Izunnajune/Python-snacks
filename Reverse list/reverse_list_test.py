from reverse_list import reverse_list

def test_reverse_list():
	numbers = [1, 2, 3, 4, 5]
	assert reverse_list(numbers) == [5, 4, 3, 2, 1]