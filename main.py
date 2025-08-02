import random as ran
from abc import ABC, abstractmethod
from matplotlib import pyplot as plt

class Stock(ABC):
    
    def __init__(self):
        self.init_stock_price = 10.0
        self.investment = self.user_input("Initial Investment", "How much do you want to invest")
        self.years = self.user_input("No. Yrs to Invest", "How many years do you want to simulate?")
        stock_prices = self.create_stock()
        self.final_stock_price = stock_prices[-1]
        self.calc_return()
        self.plot_stock(stock_prices)

    def calc_return(self):
        self.investment
        self.final_stock_price
        
        no_stocks = self.investment/self.init_stock_price
        pl = round(self.final_stock_price * no_stocks - self.investment, 2)
        
        print("Initial Stock Price: £{}\nInitial Investment: £{}\nInitial Stocks Bought: {}\nFinal Stock Price: £{}\nReturn: £{}".format(self.init_stock_price, self.investment, round(no_stocks, 2), round(self.final_stock_price, 2), pl))
        return pl

    def user_input(self, type: str, msg: str) -> int:
        print("{}:".format(msg), end=" ")
        val = input()
        try:
                val = int(val)
                print("{}: {}\n".format(type, val))
                return val
        except ValueError:
            print("Error: Please enter a valid integer")
            return self.user_input(type, msg)
    
    @abstractmethod
    def create_stock(self) -> list[float]:
        pass
        

    def plot_stock(self, xs):
        days = [x for x in range(len(xs))]
        plt.plot(days, xs)
        plt.show()    


class default_stock(Stock):
    
    def __init__(self, fname, lname, year):
        super().__init__()
        
    def create_stock(self) -> list[float]:
        days = self.years * 365
        percents = [x/10 for x in range(-20, 41, 1)]
        stock_prices = [self.init_stock_price]
        cur = self.init_stock_price
        for _ in range(days):
            change = (1+ran.choices(percents, k=1)[0]/100)
            cur = cur * change
            stock_prices.append(cur)
        return stock_prices

def main():
    Stock()
    

if __name__ == "__main__":
    main()
    