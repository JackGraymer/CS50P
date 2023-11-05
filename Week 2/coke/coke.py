def main():
    due = 50
    while due > 0:
        coin = int(input("Enter a coin: "))
        if coin == 5 or coin == 10 or coin == 25:
            due = due - coin
            if due <= 0:
                print("Change Owed:", abs(due))
                return
            print("Amount Due:", due)
        else:
            print("Amount Due:", due)

main()