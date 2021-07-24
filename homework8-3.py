class NotNumberException(Exception):
    def __init__(self, txt):
        self.txt = txt


result_list = []
while True:
    value = input('Введите число для добавления в список или stop для выхода: ')

    if value == 'stop':
        print(f'{result_list}')
        break

    try:
        if not value.isnumeric():
            raise NotNumberException('err')
        else:
            result_list.append(int(value))
    except NotNumberException as error:
        print('is not number')