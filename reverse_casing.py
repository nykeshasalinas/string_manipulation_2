# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

# Ask user to input string in random letter cases
string = input("Input string in random letter cases: ")

# Print input in reversed letter cases
swapped_string = ""

for char in string:
    if 'a' <= char <= 'z':
        swapped_string += chr(ord(char) - 32)
    elif 'A' <= char <= 'Z':
        swapped_string += chr(ord(char) + 32)
    else:
        swapped_string += char

print("String after reversing letter case:", swapped_string)