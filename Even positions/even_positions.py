def even_positions(grades):
	length = len(grades) // 2

	new_grades = [0] * length
	count = 0

	for index in range(1, len(grades), 2):
		new_grades[count] = grades[index]
		count += 1
	
	return new_grades