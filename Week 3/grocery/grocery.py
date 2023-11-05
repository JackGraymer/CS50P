def main():
	list = {}
	while True:
		try:
			item = input().strip().lower()

			if item in list:
				list[item] += 1
			else:
				list[item] = 1

		except EOFError:
			sorlist = dict(sorted(list.items()))
			for item in sorlist:
				print(str(list[item]) + ' ' + item.upper())
				#print(list[item] + item.upper())

			return

main()