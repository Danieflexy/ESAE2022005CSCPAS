Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> user_input = input("Enter a string: ")
Enter a string: 1daniel134
>>> pattern = '123'
>>> if pattern in user_input:
...     print(f"Pattern '{pattern}' found in the input.")
... else:
...     print(f"Pattern '{pattern}' not found in the input.")
... 
...     
Pattern '123' not found in the input.
>>> user_input = input("Enter a string: ")
Enter a string: danieleze123
>>> pattern = '123'
>>> if pattern in user_input:
...     print(f"Pattern '{pattern}' found in the input.")
... else:
...      print(f"Pattern '{pattern}' not found in the input.")
... 
...      
Pattern '123' found in the input.
