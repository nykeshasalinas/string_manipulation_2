# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

# Ask user to input string
string = input("Input string: ")

# Ask user to input length of string
length = int(input("Input length of string: "))

# Add zero/s at the start of string
if len(string) < length:
    string = "0" * (length - len(string)) + string

# Print input with zero/s at the beginning