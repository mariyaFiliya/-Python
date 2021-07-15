my_dict = {}
with open("text_6.txt", "r", encoding="utf-8") as f:
    for line in f:
        lesson, hours = line.split(":")
        les_sum = sum(map(int, "".join([i for i in hours if i == ' ' or '9' >= i >= '0']).split()))
        my_dict[lesson] = les_sum
print(f"{my_dict}")



