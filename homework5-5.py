from random import randint

with open('numbers.txt', 'w', encoding='utf-8') as num:
    num_list = [randint(1, 101) for _ in range(1, 500)]
    num.write(" ".join(map(str, num_list)))

print(f'Сумма всех элементов равна {sum(num_list)}')