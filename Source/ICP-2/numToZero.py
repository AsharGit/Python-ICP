step = 1
negativeNum = True

# Prevent negative numbers
while negativeNum:
    # Get non-negative number from user
    inputNum = int(input('Enter a number to reduce to zero: '))
    if inputNum > 0:
        negativeNum = False
    else:
        print('Negative numbers are invalid!')

# Divide even numbers and subtract odd numbers to reduce to 0
while inputNum > 0:
    # Even
    if inputNum % 2 == 0:
        inputNum = inputNum / 2
        print('Step ' + str(step) + ') ' + 'After dividing by 2, new number is ' + str(inputNum))
    # Odd
    else:
        inputNum = inputNum - 1
        print('Step ' + str(step) + ') ' + 'After subtracting by 1, new number is ' + str(inputNum))
    # Update steps
    step = step + 1

# Print total steps
print('\n' + 'Total steps: ' + str(step - 1))
