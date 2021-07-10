from sys import argv
name, prodaction, rate, prize = argv
salary = int(prodaction) * int(rate) + int(prize)
print(salary)
