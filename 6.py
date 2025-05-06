
x = float(input('Enter the first number: '))
y = float(input('Enter the second number: '))
z = float(input('Enter the third number: '))


if((x > z) and (x > y)):
	print('Largest number: %.1f' %(x))
elif((y > x ) and (y > z)):
	print('Largest number: %.1f' %(y))
else:
	print('Largest number: %.1f' %(z))
