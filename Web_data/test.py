import re

text = 'abcdfghijk'

parser = re.search('a[b-f]*f',text)
print(parser.group())
