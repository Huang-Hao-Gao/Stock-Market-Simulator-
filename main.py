import stocks

def get_int(prompt: str) -> int:
    while True:
        try:
            val = int(input(f"{prompt}: ").strip())
            return val
        except ValueError:
            print("Please enter a valid integer.")

def choose_stock_class() -> type:
    choices = {
        "growth": stocks.growth_stock,
        "g": stocks.growth_stock,
        "1": stocks.growth_stock,
        "dividend": stocks.dividend_stock,
        "d": stocks.dividend_stock,
        "2": stocks.dividend_stock,
        "common": stocks.common_stock,
        "c": stocks.common_stock,
        "3": stocks.common_stock,
    }
    
    print("Brief overview of stock types:")
    print("Growth — Fast‑growing, high‑volatility companies aiming for rapid revenue/price gains (e.g., Tesla).")
    print("Dividend — Stable, cash‑generating firms that pay regular dividends for income (e.g., Lloyds).")
    print("Common — Regular publicly traded shares representing ownership; mix of income and growth depending on the company (e.g., Tesco")
    while True:
        print("Choose stock type to simulate (growth/dividend/common) or (1/2/3):", end=" ")
        choice = input().strip().lower()
        cls = choices.get(choice)
        if cls:
            return cls
        print("Invalid choice. Try again.")

def main():
    StockClass = choose_stock_class()
    investment = get_int("Initial Investment (integer GBP)")
    years = get_int("No. Yrs to Invest (integer)")
    # instantiate with provided values
    StockClass(investment, years)
    

if __name__ == "__main__":
    main()