import math

number = int (input ("Enter any number: "))
number_length = math.ceil(math.log10(number))
number_square = number**2
square_divider = 10 ** number_length
number_from_square = number_square % square_divider
if number_from_square == number:
    print("Number is an ambigram")
else :
    print("Number is not an ambrigram")