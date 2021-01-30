heightFeet = []
numStudent = 0
ftToCm = 30.48
addStudent = True

# Keep prompting user for height input until user quits
while addStudent:
    height = input("Enter student height in feet or q to quit: ")
    # Quit
    if height == 'q':
        addStudent = False
    # Append to list
    else:
        heightFeet.append(float(height))
    # Update number of students
    numStudent = numStudent + 1

# Convert feet list to cm
heightCm = [round(i * ftToCm, 1) for i in heightFeet]

# Print the number of students and their heights in feet and cm
print('\n' + 'Number of students: ' + str(numStudent - 1))
print('Student height in feet: ' + str(heightFeet))
print('Student height in cm: ' + str(heightCm))

