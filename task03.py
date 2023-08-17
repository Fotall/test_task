a = 0
if a == 0:
    b = 2
else:
    b = 1

some_dict = {0: 'b = 2', 1: 'b = 1'}
a = int(input('Если А = 0, введите - "0", в противном случае, введите - "1"\n'))
print(some_dict[a])