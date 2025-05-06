def factorial(n):
	if n ==0 or n == 1:
		return 1
	else:
		fact = 1
		for i in range(2,n+1):
			fact *= i 
		return fact
try:
	number = int(input("Enter a number : "))
	if number < 0:
		print("Enter a positive number")
	else:
		result = factorial(number)
		print(f"Factorial of given number is : {result}")
except ValueError:
	print("Please enter a valid integer.")
	
	
	
