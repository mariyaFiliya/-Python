from itertools import count

for n in count(3):
    if n > 10:
        break
    else:
        print(n)

from itertools import cycle

i = 0
for a in cycle([1, 2, 3, 4, 5, 6, 7, 8]):
    if i == 10:
        break
    print(a)
    i += 1