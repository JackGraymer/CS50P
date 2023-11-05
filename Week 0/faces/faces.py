def faces():
    str = input('What are you feeling? ').replace(':)', '🙂').replace(':(', '🙁')
    print(str)
    return str

faces()
