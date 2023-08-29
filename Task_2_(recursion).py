def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number-1)

while True:
    num = input("Enter your number or write 'q' to exit\n")
    if num == "q":
        break
    try:
        print(f"factorial of the number {num} = {factorial(int(num))}")
    except ValueError:
        print("Enter a number!!!")
    