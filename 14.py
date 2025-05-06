from itertools import permutations
def is_valid_digit(digit):
	return 0 <= digit <= 9
try:
	digit1 = int(input("digit1 (0-9): "))
	digit2 = int(input("digit2 (0-9): "))
	digit3 = int(input("digit3 (0-9): "))
	if is_valid_digit(digit1) and is_valid_digit(digit2) and is_valid_digit(digit3):
		digits = [digit1, digit2,digit3]
		for prem in sorted(set(permutations(digits))):
			print("".join(map(str,prem)))
	else:
		print("Invalid")
except ValueError:
	print("Invalid")
