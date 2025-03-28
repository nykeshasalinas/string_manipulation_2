# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

# Ask user to input string
string = input("Enter the string: ")

# Print input with only the first letter capitalized
if string:
    capitalized_string = chr(ord(string[0]) - 32) if 'a' <= string[0] <= 'z' else string[0]
    capitalized_string += "".join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in string[1:])
else:
    capitalized_string = string

print("Capitalized string:", capitalized_string)