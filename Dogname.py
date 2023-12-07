Dogname = input('What is your dog\'\'s name: ')

Age = int(input('Enter dog\'\'s age: '))

if Age <= 2:
	yrs = dogAge*10.5
else:
	dogAge1 = Age-2
yrs = 2*10.5+dogAge1*4

print(Dogname, 'is ', '%.0f' % yrs, 'years old')