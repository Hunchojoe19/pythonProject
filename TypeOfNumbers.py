user_input = int (input("Enter a number: "))
factor = 1
sum_of_factors = 0;
while factor < user_input:
    if user_input % factor == 0:
        sum_of_factors += factor
    factor += 1
print("The sum of factors", sum_of_factors)

if sum_of_factors > user_input:
    print(user_input, "is an Abundant numbers")
elif sum_of_factors == user_input:
    print(user_input, "is a Perfect numbers")
else:
    print(user_input, "is a Deficient number")