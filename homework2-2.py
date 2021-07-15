user_list = input("Введите список элементов через запятую: ").split(',')
i = 0
n = 0
for elements in user_list:
    if i < (len(user_list)-1):
        n = user_list[i]
        user_list[i] = user_list[i+1]
        user_list[i+1] = n
        i += 2
    else:
        break
print(user_list)


