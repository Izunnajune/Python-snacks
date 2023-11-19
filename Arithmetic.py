num1 = int(input('Enter an integer:'))
num2 = int(input('Enter another integer:'))
num3 = int(input('Enter another integer:'))

sum = (num1+num2+num3)
print('sum of the three integers you entered is', sum)

average = (num1+num2+num3)/3
print('average of the three integers you entered is', '%.1f' % average)
product = (num1*num2*num3)
print('product of the three integers you entered is', product)

if num1 < num2 and num1 < num3:
	print('smallest of the integers entered is', num1)
elif num2 < num1 and num2 < num3:
	print('smallest of the integers entered is', num2)
else:
	print('smallest of the integers entered is', num3)

if num1 > num2 and num1 > num3:
	print('largest of the integers entered is', num1)
elif num2 > num1 and num2 > num3:
	print('largest of the integers entered is', num2)
else:
	print('largest of the integers entered is', num3)