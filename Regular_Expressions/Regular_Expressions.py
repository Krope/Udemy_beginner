# ^ Соответствует началу строки
# .Соответствует любому символу
# \ s Соответствует пробелу
# \ S Соответствует любому непробельному символу
# * Повторяет символ ноль или более раз
# *? Повторяет символ ноль или более раз (без жадности)
# + Повторяет символ один или несколько раз
# +? Повторяет символ один или несколько раз (без жадности)
# [aeiou] Соответствует одному символу в указанном наборе
# [^ XYZ] Соответствует одному символу, не указанному в наборе
# [a-z0-9] Набор символов может включать диапазон
# ( указывает, где начинается
# ) извлечение строки указывает, где заканчивается извлечение строки

# re.search()  Вы можете использовать, чтобы увидеть, соответствует ли строка регулярному выражению
# re.findall() Вы можете использовать, чтобы извлечь части строки, которые соответствуют вашему регулярному выражению

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x) # поиск соответсвующих значений
print(y)
y = re.findall('[AEIOU]',x)
print(y)

x = 'From: Using the : character'
y = re.findall('^F.+:',x) # задаем начало и конец поиска и извлечения значения, вірезает до последнего указанного символа строки
print(y)

x = 'From: Using the : character'
y = re.findall('^F.+?:',x) # задаем начало и конец поиска и извлечения значения, вірезает до первого найденного совпадения символа окончания
print(y)

x = 'From stephen.marquard@uct.ac.za Fri Jan  4 04:07:34 2008'
y = re.findall('\S+@\S+',x) # извлекаем почту из строки
print(y)
y = re.findall('^From (\S+@\S+)',x) # второй способ извлечь почту из строки
print(y)


# Извлечение домена почты методом find()
data = 'From stephen.marquard@uct.ac.za Fri Jan  4 04:07:34 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)

# с помощью списков
line = 'From stephen.marquard@uct.ac.za Fri Jan  4 04:07:34 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

# с помощью регулярніх віражений
lin = 'From stephen.marquard@uct.ac.za Fri Jan  4 04:07:34 2008'
y = re.findall('@([^ ]*)',lin)
print(y)

# второй более крутой способ

lin = 'From stephen.marquard@uct.ac.za Fri Jan  4 04:07:34 2008'
y = re.findall('^From .*@([^ ]*)',lin)
print(y)

import re

# віведение максимального значения

hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

# экранирующий символ
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)
