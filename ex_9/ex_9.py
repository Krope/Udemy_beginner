name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if not line.startswith('From ') : continue
        word = line.split()
        print(word)
        email = word[1]
        counts[email] = counts.get(email,0) + 1

big_email = None
count_email = None
for email,count in counts.items():
    if big_email is None or count > big_email:
        count_email = email
        big_email = count

print(count_email, big_email)
