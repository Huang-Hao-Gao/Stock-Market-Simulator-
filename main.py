import random as ran


init = 100
years = 5
days = years * 365
final = init

for day in range(days):
    final += ran.randint(-10, 10)


print("Initial Stock Price:" + str(init))
print("Final Stock Price:" + str(final))