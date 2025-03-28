# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# Ask user to input string in random cases
string = input("Input string in random letter cases: ")

# Print input in lower case
lowercase_string = ""
for char in string:
    if 'A' <= char <= 'Z':
        lowercase_string += chr(ord(char) + 32)
    else:
        lowercase_string += char

print("String in lowercase:", lowercase_string)