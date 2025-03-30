# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

# Ask user to input string in random cases
string = input("Input string in random letter cases: ")

# Print input in upper case
uppercase_string = ""
for char in string:
    if 'a' <= char <= 'z':
        uppercase_string += chr(ord(char) - 32)
    else:
        uppercase_string += char

print("Input in upper case:", uppercase_string)