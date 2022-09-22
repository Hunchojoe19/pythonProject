user_input = int(input("Enter your 4 digit number: "))
separator = user_input % 10000 // 1000, user_input % 1000 // 100, user_input % 100//10, user_input % 10
print(separator)