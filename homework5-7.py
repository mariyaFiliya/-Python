import json
with open('new_file.json', 'w', encoding='utf-8') as f:
    with open('firm_data.txt', 'r', encoding='utf-8') as data:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in data}
        res = [profit, {'средняя прибыль равна: ': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                        len([int(i) for i in profit.values() if int(i) > 0]))}]
        json.dump(res, f, ensure_ascii=False, indent=4) 