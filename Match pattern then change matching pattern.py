Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> user_input = input("Enter a string: ")
Enter a string: danielabc123xyz
>>> pattern = 'abc'
>>> if pattern in user_input:
...     print(f"Pattern '{pattern}' found in the input.")
...     replacement = 'xyz'
...     modified_string = user_input.replace(pattern, replacement)
...     print(f"Modified string: {modified_string}")
... else:
...     print(f"Pattern '{pattern}' not found in the input.")
... 
...     
Pattern 'abc' found in the input.
Modified string: danielxyz123xyz
