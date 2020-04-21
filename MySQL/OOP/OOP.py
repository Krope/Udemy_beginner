stuff = list()
stuff.append('python')
stuff.append('Chuck')
stuff.sort()
print(stuff[0])
print(stuff.__getitem__(0))
print(list.__getitem__(stuff, 0))

usf = input('Enter the US Floor Number: ')
wf = int(usf) - 1
print('Non-US Floor Number is {}.'.format(wf))
