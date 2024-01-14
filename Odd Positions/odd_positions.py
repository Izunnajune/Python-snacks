def odd_positions(grades):
	length = 0

	if len(grades) % 2 != 0:
		length = (len(grades) // 2) + 1
	else:
		length = len(grades) // 2

	new_grades = [0] * length
	count = 0

	for index in range(0, len(grades), 2):
		new_grades[count] = grades[index]
		count += 1
	
	return new_grades
