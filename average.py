num = float(input('Enter number: '))
count = 0
total = 0
while num != -1:
	total += num
	count += 1
	num = float(input('Enter number: '))

print('Sum of all numbers entered is ', total)

Average = total/count
print('average of numbers entered is ', Average)