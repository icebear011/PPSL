def is_prime(n):
	if n < 2:
		return False
	for i in range(2,n):
		if n % i == 0:
			return False
	return True
upper_limit = int(input("Enter upper limit: "))
for i in range(2,upper_limit):
	if is_prime(i):
		print(i)
