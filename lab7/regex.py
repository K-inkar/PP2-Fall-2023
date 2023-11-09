import re
with open("row.text", "r", encoding="utf-8") as file:
     data = file.read()
# 1.Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

pattern = r'аб*'
matches = re.findall(pattern, text)
print(matches)

# 2.Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

pattern = r'а[б]{2,3}'
matches = re.findall(pattern, text)
print(matches)
    

# 3.Write a Python program to find sequences of lowercase letters joined with a underscore.

pattern = r'[а-я]+_[а-я]+'
matches = re.findall(pattern, text)
print(matches)

# 4.Write a Python program to find the sequences of one upper case letter followed by lower case letters.

pattern = r'[А-Я][а-я]+'
matches = re.findall(pattern, text)
print(matches)

# 5.Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

pattern = r'а.*б'
matches = re.findall(pattern, text)
print(matches)

# 6.Write a Python program to replace all occurrences of space, comma, or dot with a colon.

def replace(text):
    pattern = r'[ ,.]'
    matches = re.sub(pattern, ':', text)
    return matches 
    
txt = replace(text)
print(txt)

# 7.Write a python program to convert snake case string to camel case string.

def snake_to_camel(snake_str):
    words = snake_str.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])
    
camel_case_text = re.sub(r'_([а-я])', lambda x: x.group(1).upper(), text)
print(camel_case_text)


# 8.Write a Python program to split a string at uppercase letters.

def split_string_at_uppercase(input_string):
    split_strings = re.findall(r'[A-Z][a-z]*', input_string)
    return split_strings

result = split_string_at_uppercase(text)
print(result)

# 9.Write a Python program to insert spaces between words starting with capital letters.

def insert_spaces_between_words(input_string):
    modified_string = re.sub(r'([а-я])([А-Я])', r'\1 \2', input_string)
    return modified_string

result = insert_spaces_between_words(text)
print(result)

# 10.Write a Python program to convert a given camel case string to snake case.
def camel_to_snake(text):
    string = re.sub(r'([а-я0-9])([А-Я])', r'\1_\2', text)
    sting = string.capitalize()
    return sting

result = camel_to_snake(text)
print(result)