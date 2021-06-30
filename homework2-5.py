rank = [23, 15, 12, 5, 1]
print(rank)
n = int(input("Введите новый элемент рейтинга: "))
i = 0
for elements in rank:
    if n > rank[i]:
        rank.insert(i, n)
        break
    elif n == rank[i]:
        rank.insert(i+1, n)
        break
    elif n < rank[i]:
        i += 1
        continue
    i += 1
    rank.append(n)
print(rank)