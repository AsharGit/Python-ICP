# Get input string from user
astring = input('Please enter string to modify and reverse: ')

# Get length of string
length = len(astring)

# Check if the string is at least 3 letters long
if length >= 3:
    # remove the first and last letter
    bstring = astring[1:length-1]
else:
    bstring = astring

# Print the reverse of the string
print(bstring[::-1])
