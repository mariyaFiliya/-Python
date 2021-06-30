some_str = input("Введите строку из нескольких слов, разделённых пробелами: ").split(' ')
for ind, el in enumerate(some_str):
    print(ind+1, el[:10])