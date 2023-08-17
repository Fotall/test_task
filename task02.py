a = 25
b = 8
c = 0
if a > b:
    a,b = b,a
    

while b > 0:
    print('b = ', b)
    b -= a
    print('b - a = ', b)
    if b == 0:
        print('число  делиться без остатка на ')
        break
    if b < 0:
        print('число  не делиться без остатка на ')
        break

