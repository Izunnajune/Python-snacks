def return_largest(samples):
	largest = samples[0]
	for number in samples:
		if number > largest:
			largest = number
	return largest