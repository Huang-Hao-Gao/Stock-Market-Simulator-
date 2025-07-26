import random as ran
from matplotlib import pyplot as plt

def create_stock(init, years):
    days = years * 365
    percents = [x/10 for x in range(-20, 41, 1)]
    stock_prices = [init]



    cur = init
    for _ in range(days):
        change = (1+ran.choices(percents, k=1)[0]/100)
        cur = cur * change
        stock_prices.append(cur)
        # print("percent:" + str(change) + "\ncurrent:" + str(cur))
        # print("\n\n")
        


    print("Initial Stock Price:" + str(init))
    print("Final Stock Price:" + str(round(cur, 2)))
    
    return stock_prices
    
def plot_stock(xs):
    days = [x for x in range(len(xs))]
    plt.plot(days, xs)
    plt.show()    

def main():
    stock_prices = create_stock(100, 1)
    plot_stock(stock_prices)
    

if __name__ == "__main__":
    main()
    