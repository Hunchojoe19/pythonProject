def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Atleast you can see divide")
        # raise ZeroDivisionError("You cannot divide to zero")
    return a / b


# print(divide(2,5))
num1 = input("Enter the numerator:")
den1 = input("Enter the denominator:")

while True:
    try:
        print(divide(num1, den1))

    except (ValueError, TypeError):
        print("Wrong input")
        num1 = int(input("Enter the numerator:"))
        den1 = int(input("Enter the denominator:"))
    except ZeroDivisionError as e:
        print("ZeroError", e)
    except IndexError as e:
        print("IndexError", e)
    else:
        print("I only run when there is no error")
        break
    finally:
        print("I run regardless of the errors or not")


