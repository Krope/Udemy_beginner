import re

hand = open('regex_sum_349899.txt')
read_hand = hand.read()
rstr_read_hand = read_hand.rstrip()
numbers = re.findall('[0-9]+',rstr_read_hand)
list_num = list()
for num in numbers:
    num_int = int(num)
    print(num_int)
    list_num.append(num_int)

#print(sum(list_num))
