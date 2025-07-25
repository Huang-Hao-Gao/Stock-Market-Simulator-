import random as ran


init = 100
years = 1
days = years * 10
cur = init
percents = [x/10 for x in range(-20, 41, 1)]



for day in range(days):
    change = (1+ran.choices(percents, k=1)[0]/100)
    cur = cur * change
    print("percent:" + str(change) + "\ncurrent:" + str(cur))
    print("\n\n")
    


print("Initial Stock Price:" + str(init))
print("Final Stock Price:" + str(round(cur, 2)))