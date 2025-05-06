x = float(input('subject 1: '))
y = float(input('subject 2: '))
z = float(input('subject 3: '))
a = float(input('subject 4: '))
b = float(input('subject 5: '))

avg = (x + y + z + a + b)/ 5
print('Average Marks: %.2f' %(avg))
if((avg > 90) and (avg < 100 )):
	print('Grade: A')

elif((avg > 80) and (avg < 89 )):
	print('Grade: B')

elif((avg > 70) and (avg < 79)):
	print('Grade: C')

elif((avg > 60) and (avg < 69)):
	print('Grade: D ')

elif( (avg < 60)):
	print('Grade: F')
