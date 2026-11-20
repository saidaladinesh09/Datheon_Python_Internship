# Stock Portfolio Performance Tracker

## Project Description
The Stock Portfolio Performance Tracker is a Python-based application that helps users track stock investments and calculate portfolio performance using real-time stock market data.

The application uses the S&P 500 companies dataset to search for stock details and Yahoo Finance (`yfinance`) to retrieve the latest available stock prices.

## Features
- Load S&P 500 company data from a CSV file.
- Search stocks using ticker symbols.
- Display company name, sector, and industry.
- Fetch the latest available stock prices using Yahoo Finance.
- Calculate total investment value.
- Calculate current portfolio value.
- Calculate profit or loss.
- Calculate overall return percentage.
- Save portfolio results into a CSV file.

## Technologies Used
- Python
- CSV
- yfinance
- Yahoo Finance API

## Project Structure

```text
Stock-Portfolio-Tracker/
│
├── portfolio.py
├── constituents.csv
├── portfolio_summary.csv
├── requirements.txt
└── README.md
```

## Installation

### Step 1: Install Python
Install Python on your computer.

### Step 2: Install Required Library

Open the VS Code terminal and run:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Project

Execute the following command:

```bash
python portfolio.py
```

## How to Use
1. Run the Python program.
2. Enter the number of stocks you want to track.
3. Enter the stock ticker symbol (Example: AAPL).
4. Enter your buying price.
5. Enter the number of shares.
6. The program fetches the latest available stock price.
7. The application calculates investment performance.
8. The results are displayed and saved in `portfolio_summary.csv`.

## Dataset
The project uses the S&P 500 companies dataset.

Dataset source:

https://github.com/datasets/s-and-p-500-companies

Dataset filename: `constituents.csv`

## Output
The application displays:
- Stock ticker
- Company name
- Buying price
- Current stock price
- Number of shares
- Profit or loss
- Total investment
- Current portfolio value
- Overall return percentage

The results are saved in:

`portfolio_summary.csv`

## Author
Your Name

## Conclusion
The Stock Portfolio Performance Tracker provides a simple way to monitor stock investments and analyze portfolio performance using Python and Yahoo Finance data.
