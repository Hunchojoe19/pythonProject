# import sqlite3
#
# connection = sqlite3.connect("testdb.db")
# cursor = connection.cursor()
#
#
# cursor.execute("CREATE TABLE User (name TEXT, age INT);")
# # cursor.execute("INSERT INTO User VALUES ('Amaka', 20);")
# # cursor.execute("SELECT * FROM User")
# print(cursor.fetchone())
#
# connection.commit()
# connection.close()
#
# for letters in "paragraph":
#     print(letters, end=" ")
# print("\n")
# total = 0;
# for letters in [2,5,7,8]:
#     total += letters
#     print(total, end=" ")

# total = 0;
# gradeCounter = 0
# grade_frequency = 0
# grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]

# for grade in grades:
#     total += grade
#     grade_frequency += 1
#     # print(total, grade_frequency)
# average = total / grade_frequency
# print(f'the average score for the student is {average}')

number1 = 7
number2 = 5
answer = number1 * number2
print(f'7 times 5 is = {answer}')

total = 0
grade = 0
gradeCounter = 0

grades = int(input("Enter the grades or press -1 to exit: "))

while grades != -1:
    total += grades
    gradeCounter += 1
    grades = int(input("Enter the grades or press -1 to exit: "))
if gradeCounter != 0:
    average = total / gradeCounter
    print(f'The average score for the student = {average}')
else:
    print("No grade was entered")

passed = 0
failed = 0

for student in range(10):
    result = int(input("Enter 1 for passes or 2 for failures: "))
    if result == 1:
        passed += 1
    elif result == 2:
        failed += 1

print(passed, "students passed the course")
print(failed, "students failed the course")
if passed > 8:
    print("Bonus to the instructor")
