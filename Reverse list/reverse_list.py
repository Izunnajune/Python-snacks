def reverse_list(numbers):
	new_list = [0] * len(numbers)
	counter = len(numbers) - 1

	for index in range(len(numbers)):
		new_list[counter] = numbers[index]
		counter -= 1

	return new_list