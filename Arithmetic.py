user_input1 = int (input("Enter first number: "))
user_input2 = int (input("Enter first number: "))
user_input3 = int (input("Enter first number: "))
sum = user_input1 + user_input2 + user_input3
average = sum / 3
product = user_input1 * user_input2 * user_input3
print(sum)
print(average)
print(product)
if user_input1 < user_input2 and user_input3:
    print(user_input1, "is the smallest number")
elif user_input2 < user_input1 and user_input3:
    print(user_input2, "is the smallest number")
elif user_input3 < user_input1 and user_input1:
    print(user_input3, " is the smallest number")
if user_input1 > user_input2 and user_input1 > user_input3:
    print(user_input1, "is the largest number")
elif user_input2 > user_input1 and user_input2 > user_input3:
    print(user_input2, "is the largest number")
else:
    print(user_input3, "is the largest number")