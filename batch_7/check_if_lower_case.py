# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

# Ask user to input string
string = input("Input string: ")

is_lower = True

for char in string:
    if 'A' <= char <= 'Z':
        is_lower = False
        break

# Print "Not all are lower case" if there is an upper case letter
if is_lower == False:
    print("Not all are lower case")
# Print "All are lower case" if all characters is on lower case
else:
    print("All are lower case")