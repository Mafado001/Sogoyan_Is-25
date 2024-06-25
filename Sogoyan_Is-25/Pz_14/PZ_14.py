"""
В исходном текстовом файле(hotline1.txt) найти все номера телефонов,
соответствующих шаблону 8(000)000-00-00.
Посчитать количество полученных элементов. После фразы «Горячая линия»
добавить фразу «Министерства образования
Ростовской области», выполнив манипуляции в новом файле.
"""

import re


with open('hotline1.txt', 'r') as file:
    content = file.read()


phone_numbers = re.findall(r'8\(\d{3}\)\d{3}-\d{2}-\d{2}', content)


count = len(phone_numbers)


with open('hotline2.txt', 'w') as file:

    new_content = content.replace('Горячая линия', 'Горячая линия Министерства образования Ростовской области')
    file.write(new_content)

print(f"Найдено {count} номеров телефонов, соответствующих шаблону 8(000)000-00-00.")