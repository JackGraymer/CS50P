def main():
	while True:
		try:
			fraction = input('Fraction:')
			num = fraction.split('/')
			percentage = round(int(num[0]) / int(num[1]) * 100)
			#print(str(percentage) + '%')
			level(percentage)
			return

		except:
			pass

def level(percentage):
	if percentage >100 or percentage < 0:
		raise ValueError('Invalid percentage')
	elif percentage <= 1:
		print('E')
	elif percentage >= 99:
		print('F')
	else:
		print(str(percentage) + '%')

main()