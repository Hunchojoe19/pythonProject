# user_input = int(input("Enter the number for fibonacci to be generated: "))
# a, b = 0, 1
# while a < user_input:
#     a, b = b, a+b
#     print(a)
#
# my_str = "Hello"
# print (my_str.find("l"))
# print(my_str.upper("h"))
# s = "This is the world of Python"
# s.find("t")
# s.rfind("t")
# s.count("t")
# s.count("T")
# s.lower().count("t")
# s.replace("Python", "Java")
# s = "1010001110001".translate(str.maketrans("01", "10"))
# print(s)
print("sorry, is this the {} minute {}".format(5, "Argument"))
print(f'{10:<20.2f}')
smiley = "\U0001f600"
print(smiley)
star = "*"
for i in range (1, 11):
    print(f"{star * i:<10}      {star * (11 - i):<10}       {star * (11-i):>10}     {star * i:>10}")