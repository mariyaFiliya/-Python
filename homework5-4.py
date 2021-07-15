translate_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open('new_translate.txt', 'w', encoding="utf-8") as new:
    with open("translate.txt", 'r', encoding="utf-8") as f:
        new.writelines([line.replace(line.split()[0], translate_dict.get(line.split()[0])) for line in f])

