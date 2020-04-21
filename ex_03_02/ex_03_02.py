hrs = input("Enter Hours:")
rate = input("Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter nuveric input") 
h = float(hrs)
r = float(rate)
k = 1.5
if h>40:
    reg = 40 * r
    tp = (h - 40) * (r * 1.5)
    pay = reg + tp
    print (pay)
else:
    p = h * r
    print (p)
