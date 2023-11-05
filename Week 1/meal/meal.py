def main():
	time = input("What time is it? ")
	time = convert(time)

	if time >= 7 and time <= 8:
		print("breakfast time")
	elif time >= 12 and time <= 13 :
		print("lunch time")
	elif time >= 18 and time <= 19:
		print('dinner time')
	else:
		return

def convert(time):
	# conver time to decimal number
	hr, min = time.split(':')
	hr, min = int(hr), int(min)/60
	return hr + min

if __name__ == "__main__":
    main()