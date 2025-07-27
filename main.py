import random as ran
from matplotlib import pyplot as plt

class Stock:
    
    
    def __init__(self):
        self.init = self.user_input("initial stock price", "What should the initial price of our stock be")
        self.years = 1
        stock_prices = self.create_stock()
        self.plot_stock(stock_prices)


    def user_input(self, type: str, msg: str) -> int:
        print("{}:".format(msg), end=" ")
        val = input()
        try:
                val = int(val)
                print("{}: {}".format(type, val))
                return val
        except ValueError:
            print("Error: Please enter a valid integer")
            return self.user_input(type, msg)

    def create_stock(self):
        days = self.years * 365
        percents = [x/10 for x in range(-20, 41, 1)]
        stock_prices = [self.init]


        cur = self.init
        for _ in range(days):
            change = (1+ran.choices(percents, k=1)[0]/100)
            cur = cur * change
            stock_prices.append(cur)
        print("Initial Stock Price:" + str(self.init))
        print("Final Stock Price:" + str(round(cur, 2)))
        
        return stock_prices
        

    def plot_stock(self, xs):
        days = [x for x in range(len(xs))]
        plt.plot(days, xs)
        plt.show()    

    

def main():
    Stock()
    

if __name__ == "__main__":
    main()
    