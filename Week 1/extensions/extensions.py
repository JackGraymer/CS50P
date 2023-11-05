import mimetypes

def main():
	file = input("Enter file name: ").strip().lower()

	if file.endswith(".gif") or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".pdf") or file.endswith(".txt") or file.endswith(".zip"):
		print(mimetypes.guess_type(file)[0])
	else:
		print("application/octet-stream")
main()