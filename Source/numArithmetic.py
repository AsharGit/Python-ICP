# Ask user for number input
print('Please enter two numbers to perform arithmetic operations on them.')
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Convert input to float
floatNum1 = float(num1)
floatNum2 = float(num2)

# Perform the arithmetic operations and print
print('Arithmetic operations using your chosen numbers:')
print('Sum: ' + num1 + " + " + num2)
print(floatNum1 + floatNum2)
print('Subtraction: ' + num1 + " - " + num2)
print(floatNum1 - floatNum2)
print('Multiplication: ' + num1 + " * " + num2)
print(floatNum1 * floatNum2)
print('Division: ' + num1 + " / " + num2)
print(floatNum1 / floatNum2)