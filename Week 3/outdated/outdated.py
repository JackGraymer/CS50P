def main():
	months = [
		"January",
		"February",
		"March",
		"April",
		"May",
		"June",
		"July",
		"August",
		"September",
		"October",
		"November",
		"December"
	]

	while True:
		try:
			date = input("Date: ")
			if "/" in date:
				month, day, year = date.split("/")
			elif "," in date:
				month_day, year = date.split(", ")
				month, day = month_day.split(" ")
				month = (months.index(month)) + 1
			if int(month) > 12 or int(day) > 31 or int(year) > 3000:
				raise ValueError
		except :
			pass
		else:
			print(f"{int(year)}-{int(month):02}-{int(day):02}")
			break

main()