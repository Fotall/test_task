
first_list = [1, 3, 6, 8]
second_list = [2, 4, 5, 9]
general_list = []
#general_list = (first_list + second_list)
# print(general_list)
# general_list.sort() # сортировка через метод, но я так понял ей нельзя пользоваться

for i in range(0, len(first_list) ):
    print(i)
    if first_list[i] > second_list[i]:
        general_list.append(second_list[i])
        general_list.append(first_list[i])
    else:
        general_list.append(first_list[i])
        general_list.append(second_list[i])




'''

for i in range(0, len(general_list) - 1):
    if general_list[i] > general_list[i + 1]:
        general_list[i], general_list[i + 1] = general_list[i + 1], general_list[i]



'''


print(general_list)
