def main():
	x,y,z = input("Enter a math operation: ").strip().split(' ')
	x , z = float(x) , float(z)

	if y == '+':
		print(x + z)
	elif y == '-':
		print(x - z)
	elif y == '*':
		print(x * z)
	elif y == '/':
		print(x / z)
	else:
		print("Invalid operation")

main()
