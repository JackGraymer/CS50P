def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
	l = len(s)
	numbers = '0123456789'
	digits = []
	for digit in s:
		if digit.isdigit():
			digits.append(digit)

 # Check for non-alphanumerical characters
	if s.isalnum() == False:
		return False

	#vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
	if l > 6 or l < 2:
		#print("Too long or short")
		return False

	# The first number used cannot be a ‘0’.”
	if len(digits) > 0:
		if digits[0] == '0' or digits[0] == 0:
			#print("First number is 0", digits)
			return False
		#Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable plate, but AAA22A would not.
		i = 0
		for char in s:
			if char in numbers:
				i += 1
			if char not in numbers and i > 0:
				return False

	#All vanity plates must start with at least two letters.
	if s[0] in numbers and s[1] in numbers:
		#print("First two not letters")
		return False
	return True

if __name__ == '__main__':
	main()