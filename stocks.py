import random as ran
from abc import ABC, abstractmethod
from matplotlib import pyplot as plt


class Stock(ABC):
    
    def __init__(self):
        self.init_stock_price = 10.0
        # self.investment = self.user_input("Initial Investment", "How much do you want to invest")
        # self.years = self.user_input("No. Yrs to Invest", "How many years do you want to simulate?")
        self.investment = 1000
        self.years = 10
        stock_prices = self.create_stock()
        self.final_stock_price = stock_prices[-1]
        self.calc_return()
        self.plot_stock(stock_prices)

    def calc_return(self):
        self.investment
        self.final_stock_price
        
        no_stocks = self.investment/self.init_stock_price
        gross = self.final_stock_price * no_stocks
        net = round(gross - self.investment, 2)
        ROI = round(net / self.investment * 100, 2)

        
        print("Initial Stock Price: £{}\nInitial Investment: £{}\nInitial Stocks Bought: {}\nFinal Stock Price: £{}\nFinal Amount: £{}\nReturn: £{}\n Return on Investment: {}%".format(self.init_stock_price, self.investment, round(no_stocks, 2), round(self.final_stock_price, 2), round(gross, 2), net, ROI))
        return net

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
        threshold_years = 2  # Change this to whatever threshold you want
        
        if self.years <= threshold_years:
            # Show days on x-axis
            days = [x for x in range(len(xs))]
            plt.plot(days, xs)
            plt.xlabel("Days")
            plt.title(f"Stock Price Over {len(xs)} Days")
        else:
            # Show years on x-axis
            # Convert day indices to years (day 0 = year 0, day 365 = year 1, etc.)
            days_to_years = [day / 365 for day in range(len(xs))]
            plt.plot(days_to_years, xs)
            plt.xlabel("Years")
            plt.title(f"Stock Price Over {self.years} Years")
        
        plt.ylabel("Stock Price (£)")
        plt.grid(True, alpha=0.3)  # Optional: adds a subtle grid
        plt.show() 


class default_stock(Stock):
    
    def __init__(self):
        super().__init__()
        
    def create_stock(self) -> list[float]:
        days = self.years * 365
        stock_prices = [self.init_stock_price]
        
        current_price = self.init_stock_price
        
        for day in range(days):
            # Simple approach: 70% chance of going up, 30% chance of going down
            if ran.random() < 0.6:
                # Stock goes up 
                daily_change = ran.uniform(1.0001, 1.002)
            else:
                # Stock goes down
                daily_change = ran.uniform(0.998, 0.9999)
            
            # Occasionally add larger movements for realism
            if ran.random() < 0.02: 
                if ran.random() < 0.5:
                    # Big gain
                    daily_change = ran.uniform(1.001, 1.05)
                else:
                    # Big loss
                    daily_change = ran.uniform(0.95, 0.995)
            
            current_price *= daily_change
            stock_prices.append(current_price)
        
        return stock_prices
        
    