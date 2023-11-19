number1 = int(input('Enter number:'))
number2 = int(input('Enter another number:'))
number3 = int(input('Enter another number:'))

if number1 > number2 and number1 > number3: 
	print(number1, 'is the highest number')

if number2 > number1 and number2 > number3: 
	print(number2, 'is the highest number')

if number3 > number1 and number3 > number2: 
	print(number3, 'is the highest number')