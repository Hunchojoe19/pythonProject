user_input = int(input("Enter the number of your choice between 1 to 10: "))
number = user_input
factorial = 1
if number < 0:
    print ("You cant get the factorial of 0")
for i in range (1, number + 1):
    factorial = factorial * i
print(factorial)