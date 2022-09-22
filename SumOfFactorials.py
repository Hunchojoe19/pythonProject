user_input = int(input("Enter number of your choice: "))
sum_of_factorial = 0
if user_input < 0:
    print("You cannot enter the sum of zero")
for m in range (1, user_input+1):
    sum_of_factorial = sum_of_factorial + m
print(sum_of_factorial)


