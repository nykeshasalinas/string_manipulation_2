# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

# Ask user to input string
string = input("Enter the string: ")

# Ask user to input total length of string
length = int(input("Enter the total length of the string: "))

# Print input in the center
if len(string) < length:
    total_padding = length - len(string)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    string = " " * left_padding + string + " " * right_padding

print("Centered string:", repr(string))