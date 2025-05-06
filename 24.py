import fibonacci_module
try:
	n = int(input('Enter the max value: '))
	if n>0:
		seq = fibonacci_module.fibbo_seq(n)
		print('Fibonacci series upto',n,':')
		for num in seq:
			print(num,end=' ')
	else:
		print('Please enter a positive integer')
except ValueError:
	print('Invalid input')
