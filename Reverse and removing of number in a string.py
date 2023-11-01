Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Get user input
>>> user_input = input("Enter a string with numbers: ")
Enter a string with numbers: Danielezemba1233
>>> # Remove numbers from the input string
>>> input_string = ''.join(char for char in user_input if not char.isdigit())
>>> # Reverse the modified string
>>> reversed_string = input_string[::-1]
>>> print("Reversed string with numbers removed:", reversed_string)
Reversed string with numbers removed: abmezeleinaD
