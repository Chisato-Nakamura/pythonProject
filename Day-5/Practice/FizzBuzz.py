for num in range(1, 101):
    if num in range (0, 101, 15):
        print("FizzBuzz")
    elif num in range(0, 101, 3):
        print("Fizz")
    elif num in range (0, 101, 5):
        print("Buzz")
    else:
        print(num)