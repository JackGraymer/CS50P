def main():
			fraction = input('Fraction:')
			#num = fraction.split('/')
			print(gauge(convert(fraction)))
			return

def convert(fraction):
	try:
		x, y = fraction.split('/')
		x, y = int(x), int(y)
		if x > y and y != '0':
			raise ValueError
		elif x == '0' or y == '0':
			raise ZeroDivisionError

		percentage = round(int(x) / int(y) * 100)
		return percentage
	except (ValueError, ZeroDivisionError) as e:
		raise(e)

def gauge(percentage):
	if percentage >100 or percentage < 0:
		raise ValueError
	elif percentage <= 1:
		return('E')
	elif percentage >= 99:
		return('F')
	else:
		return str(percentage) + '%'

if __name__ == "__main__":
    main()