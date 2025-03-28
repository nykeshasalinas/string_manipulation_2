# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# Ask user to input string
string = input("Input string: ")

for char in string:
    if 'a' <= char <= 'z':
        # Print "All are upper case" if there is a lowercase letter
       
    else:
        # Print "Not all are upper case" if all characters is on upper case