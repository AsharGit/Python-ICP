python, course, deep, learning = 0, 0, 0, 0

# Open file and read text
inputFile = open('input.txt', 'r')
text = inputFile.read()
inputFile.close()

# Iterate word by word and add each found word to count
for i in text.split():
    if i == 'Python':
        python = python + 1
    elif i == 'Course':
        course = course + 1
    elif i == 'Deep':
        deep = deep + 1
    elif i == 'Learning':
        learning = learning + 1

# Print word count information
print('Word Count:')
print('Python: ' + str(python))
print('Course: ' + str(course))
print('Deep: ' + str(deep))
print('Learning: ' + str(learning))

# Write word count information back to file
inputFile = open('input.txt', 'a')
inputFile.write('\n' + 'Word Count:' + '\n')
inputFile.write('Python: ' + str(python) + '\n')
inputFile.write('Course: ' + str(course) + '\n')
inputFile.write('Deep: ' + str(deep) + '\n')
inputFile.write('Learning: ' + str(learning) + '\n')
inputFile.close()
