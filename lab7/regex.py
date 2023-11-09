import re
text = """
ДУБЛИКАТ
Филиал ТОО EUROPHARMA Астана
БИН 080841000761
НДС Серия 58001
 № 0014377
Касса 300-189
Смена 10
Порядковый номер чека №64
Чек №2331180266
Кассир Аптека 17-1
ПРОДАЖА
1.
Натрия хлорид 0,9%, 200 мл, фл
2,000 x 154,00
308,00
Стоимость
308,00
2.
Борный спирт 3%, 20 мл, фл.
1,000 x 51,00
51,00
Стоимость
51,00
3.
Шприц 2 мл, 3-х комп. (Bioject)
2,000 x 16,00
32,00
Стоимость
32,00
4.
Система для инфузии Vogt Medical
2,000 x 60,00
120,00
Стоимость
120,00
5.
Naturella прокладки Классик макси №8
1,000 x 310,00
310,00
Стоимость
310,00
6.
AURA Ватные диски №150
1,000 x 461,00
461,00
Стоимость
461,00
7.
Чистая линия скраб мягкий 50 мл
1,000 x 381,00
381,00
Стоимость
381,00
8.
Чистая линия  скраб очищающийабрикос 50 мл
1,000 x 386,00
386,00
Стоимость
386,00
9.
Чистая линия скраб мягкий 50 мл
1,000 x 381,00
381,00
Стоимость
381,00
10.
Carefree салфетки Алоэвоздухопроницаемые №20
1,000 x 414,00
414,00
Стоимость
414,00
11.
Pro Series Шампунь яркий цвет 500мл
1,000 x 841,00
841,00
Стоимость
841,00
12.
Pro Series бальзам-ополаскивательдля длител ухода за окрашеннымиволосами Яркий цвет 500мл
1,000 x 841,00
841,00
Стоимость
841,00
13.
Clear шампунь Актив спорт 2в1мужской  400 мл
1,000 x 1 200,00
1 200,00
Стоимость
1 200,00
14.
Bio World (HYDRO THERAPY)Мицеллярная вода 5в1, 445мл
1,000 x 1 152,00
1 152,00
Стоимость
1 152,00
15.
Bio World (HYDRO THERAPY) Гель-муссдля умывания с гиалуроновойкислотой, 250мл
1,000 x 1 152,00
1 152,00
Стоимость
1 152,00
16.
[RX]-Натрия хлорид 0,9%, 100 мл, фл.
1,000 x 168,00
168,00
Стоимость
168,00
17.
[RX]-Дисоль р-р 400 мл, фл.
1,000 x 163,00
163,00
Стоимость
163,00
18.
Тагансорбент с иономи серебра №30,пор.
1,000 x 1 526,00
1 526,00
Стоимость
1 526,00
19.
[RX]-Церукал 2%, 2 мл, №10, амп.
2,000 x 396,00
792,00
Стоимость
792,00
20.
[RX]-Андазол 200 мг, №40, табл.
1,000 x 7 330,00
7 330,00
Стоимость
7 330,00
Банковская карта:
18 009,00
ИТОГО:
18 009,00
в т.ч. НДС 12%:
0,00
Фискальный признак:
2331180266
Время: 18.04.2019 11:13:58
г. Нур-султан,Казахстан, Мангилик Ел,19, нп-5
Оператор фискальных данных: АО"Казахтелеком"Для проверки чека зайдите на сайт:consumer.oofd.kz
ФИСКАЛЬНЫЙ ЧЕК
ФП
ИНК ОФД: 311559
Код ККМ КГД (РНМ): 620300145316
ЗНМ: SWK00034961
WEBKASSA.KZ
"""

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