"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))        # 5
	print(find_largest_digit(281))          # 8
	print(find_largest_digit(6))            # 6
	print(find_largest_digit(-111))         # 1
	print(find_largest_digit(-9453))        # 9


def find_largest_digit(n):
	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, max_digit):
	if n < 0:			# n為負數
		n = n*(-1)
	if n < 10: 			# one digit only
		if n > max_digit:
			return n
		else:
			return max_digit
	else:
		unit = n % 10  # get units digit
		if unit > max_digit:
			max_digit = unit
			return find_largest_digit_helper((n-unit)//10, max_digit)
		else:
			return find_largest_digit_helper((n-unit)//10, max_digit)


if __name__ == '__main__':
	main()
