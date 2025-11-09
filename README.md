# Stock Market Investment Simulator

A Python-based stock market simulation modeling three distinct investment strategies with realistic price movements, dividend payments, and risk scenarios.

## Features

- **Three Stock Types**:
  - **Growth** — High-volatility momentum trading with bankruptcy risk
  - **Dividend** — Stable income stocks with quarterly dividend payments (£0.15/share every 90 days)
  - **Common** — Standard market behavior with moderate volatility

- **Realistic Market Dynamics**: Momentum effects, dramatic swings, and probability-based daily price movements
- **ROI Analysis**: Detailed breakdowns of returns, dividends, and stock performance
- **Visualization**: Automatic day/year axis scaling with matplotlib graphs

## Requirements

- Python 3.13.0+
- NumPy
- Matplotlib

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Stock-Market-Simulator-.git
cd Stock-Market-Simulator-

# Install dependencies
pip install -r requirements.txt
```

## Usage

Run the simulator:

```bash
python main.py
```

**Example Session**:

```
Brief overview of stock types:
Growth — Fast‑growing, high‑volatility companies aiming for rapid revenue/price gains (e.g., Tesla).
Dividend — Stable, cash‑generating firms that pay regular dividends for income (e.g., Lloyds).
Common — Regular publicly traded shares representing ownership; mix of income and growth (e.g., Tesco).

Choose stock type to simulate (growth/dividend/common) or (1/2/3): growth
Initial Investment (integer GBP): 1000
No. Yrs to Invest (integer): 5

Initial Stock Price: £10
Initial Investment: £1000
Initial Stocks Bought: 100.0
Years Invested: 5
Final Stock Price: £47.23
Final Amount: £4723.0
Return: £3723.0
Return on Investment: 372.3%
```

A matplotlib window displays the stock price over time.

## How It Works

Each stock type implements a distinct `_create_stock()` algorithm:

- **Growth**: Momentum-based system with explosive gains/crashes and bankruptcy below £0.10
- **Dividend**: Stable ±0.5% daily movements with quarterly cash payouts
- **Common**: 60% upward bias with 2% chance of large swings

The simulation runs 365 days/year and calculates total returns including dividends (where applicable).

## Project Structure

```
Stock-Market-Simulator-/
├── main.py           # Entry point and user interaction
├── stocks.py         # Stock simulation classes and algorithms
├── requirements.txt  # Python dependencies
└── README.md
```

## Development

The codebase uses abstract base classes (`Stock`) with three concrete implementations. To add new stock types:

1. Inherit from `Stock` in `stocks.py`
2. Implement `_create_stock()` returning a list of daily prices
3. Optionally override `_calc_return()` for custom return logic
4. Add to the `choices` dict in `main.py`


## Author

Huang Hao Gao - Personal project for quantitative finance simulation and Python OOP practice