with open("salary.txt", "r", encoding="utf-8") as res:
    res_dict = {line.split()[0]: float(line.split()[1]) for line in res}
    print(f'Работники, чья зарплата меньше 20тыс.: {[i[0] for i in res_dict.items() if i[1] < 20000]}\n'
          f'Средняя заработная плата: {round(sum(res_dict.values()) / len(res_dict), 1)}')