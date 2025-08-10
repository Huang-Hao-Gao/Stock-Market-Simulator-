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

class dividend_stock(Stock):
    #to calculate the overall return on this stock i will need to add the regular dividend onto the return
    
    
    def __init__(self):
        super().__init__()
        self.total_dividends = 0
        
    def create_stock(self) -> list[float]:
        days = self.years * 365
        stock_prices = [self.init_stock_price]
        
        current_price = self.init_stock_price
        quarterly_dividend = 0.15  # £0.15 per share every quarter
        total_dividends_received = 0
        
        for day in range(days):
            # Very stable daily movements (±0.5% max)
            if ran.random() < 0.53:  # Slight upward bias
                daily_change = ran.uniform(1.0001, 1.001)  # Small gains
            else:
                daily_change = ran.uniform(0.999, 0.9999)  # Small losses
                
            if ran.random() < 0.02: 
                if ran.random() < 0.5:
                    # Big gain
                    daily_change = ran.uniform(1.001, 1.02)
                else:
                    # Big loss
                    daily_change = ran.uniform(0.98, 0.999)
            
            # Pay dividend every 90 days (quarterly)
            if day % 90 == 0 and day > 0:
                shares_owned = self.investment / self.init_stock_price
                dividend_payment = shares_owned * quarterly_dividend
                total_dividends_received += dividend_payment
                            
            current_price *= daily_change
            stock_prices.append(current_price)
        
        # Store total dividends for final calculation
        self.total_dividends = total_dividends_received
        return stock_prices


class growth_stock(Stock):
    
    def __init__(self):
        super().__init__()
        
    def create_stock(self) -> list[float]:
        days = self.years * 365
        stock_prices = [self.init_stock_price]
        bankrupt_threshold = 0.10 #company declares bankruptcy if stock falls below this value
        
        current_price = self.init_stock_price
        momentum = 1.0  # Tracks current market sentiment
        
        for day in range(days):
            if current_price > 100:
                if ran.random() < 0.6:
                    # Normal upward movement
                    daily_change = ran.uniform(1.001, 1.002)
                    momentum = min(momentum + 0.01, 1.5)  # Build positive momentum
                else:
                    # Downward movement
                    daily_change = ran.uniform(0.998, 0.999)
                    momentum = max(momentum - 0.02, 0.5)  # Lose momentum
                
                    # Apply momentum effect
                    if momentum > 1.1:
                        daily_change *= ran.uniform(1.002, 1.004)  # Momentum boost
                    elif momentum < 0.8:
                        daily_change *= ran.uniform(0.996, 0.998)  # Momentum drag
                    
                    # Growth stocks have frequent dramatic movements (10% chance)
                    if ran.random() < 0.10:
                        if ran.random() < 0.45:
                            # Explosive growth day
                            daily_change = ran.uniform(1.01, 1.02)
                            momentum = min(momentum + 0.1, 1.8)
                        else:
                            # Crash day
                            daily_change = ran.uniform(0.98, 0.99)
                            momentum = max(momentum - 0.1, 0.3)
            else:
                if ran.random() < 0.6:
                    # Normal upward movement (60% chance)
                    daily_change = ran.uniform(1.001, 1.008)
                    momentum = min(momentum + 0.01, 1.5)  # Build positive momentum
                else:
                    # Downward movement (40% chance)
                    daily_change = ran.uniform(0.990, 0.999)
                    momentum = max(momentum - 0.02, 0.5)  # Lose momentum
                
                    # Apply momentum effect
                    if momentum > 1.1:
                        daily_change *= ran.uniform(1.005, 1.015)  # Momentum boost
                    elif momentum < 0.8:
                        daily_change *= ran.uniform(0.985, 0.995)  # Momentum drag
                    
                    # Growth stocks have frequent dramatic movements (10% chance)
                    if ran.random() < 0.10:
                        if ran.random() < 0.75:
                            # Explosive growth day
                            daily_change = ran.uniform(1.05, 1.2)
                            momentum = min(momentum + 0.1, 1.8)
                        else:
                            # Crash day
                            daily_change = ran.uniform(0.70, 0.92)
                            momentum = max(momentum - 0.15, 0.3)
                
            current_price *= daily_change
            
            # Check for bankruptcy
            if current_price < bankrupt_threshold:  # If stock falls below 10p (essentially worthless)
                print(f"Company Bankruptcy on Day {day + 1}!")
                print(f"Stock price fell to £{current_price:.4f} - Company has gone bust!")
                print("All remaining investment is lost.")
                # Set all remaining days to 0
                stock_prices.append(0.0)
                for _ in range(day + 1, days):
                    stock_prices.append(0.0)
                break            
            
            stock_prices.append(current_price)
        
        return stock_prices


class default_stock(Stock):
    
    def __init__(self):
        super().__init__()
        
    def create_stock(self) -> list[float]:
        days = self.years * 365
        stock_prices = [self.init_stock_price]
        
        current_price = self.init_stock_price
        
        for day in range(days):
            if ran.random() > 0.4:
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
        
    