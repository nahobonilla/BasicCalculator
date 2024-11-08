def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2
    else:
        raise ValueError("Invalid operator")

print(calculator(10, 5, '+'))
print(calculator(10, 5, '-'))
print(calculator(10, 5, '*'))
print(calculator(10, 5, '/'))