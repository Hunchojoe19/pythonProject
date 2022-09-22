numbers = 1
while numbers <= 100:

    if numbers % 15 == 0:
        print("FizzBuzz")
    elif numbers % 5 == 0:
        print("Buzz")
    elif numbers % 3 == 0:
        print("Fizz")
    else:
        print(numbers)
    numbers += 1
