user_input= int(input("Enter a number between 1 to 50: "))
number = 16
while number <= 50:
    if user_input < number:
        print("Number too low, try again")
        break
    elif user_input > number:
        print("Number too high, try again")
        break
    elif user_input == number:
        print("Good job, you guessed correctly")
        break
    else:
        print("Try again")
        break

