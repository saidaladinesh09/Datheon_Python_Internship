
import csv
import os
from datetime import datetime

import yfinance as yf

# CSV dataset filename changed here
INPUT_FILE = "constituents.csv"
OUTPUT_FILE = "portfolio_summary.csv"


# STEP 1: Load stock dataset
def load_stocks():
    stocks = {}

    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found!")
        return stocks

    with open(INPUT_FILE, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            symbol = row["Symbol"].strip().upper()

            stocks[symbol] = {
                "name": row["Security"],
                "sector": row["GICS Sector"],
                "industry": row["GICS Sub-Industry"]
            }

    return stocks


# STEP 2: Search for a stock
def search_stock(stocks):
    symbol = input("\nEnter stock ticker (example: AAPL): ")
    symbol = symbol.strip().upper()

    if symbol not in stocks:
        print("Stock symbol not found in your dataset!")
        return None

    stock = stocks[symbol]

    print("\nStock Details")
    print("------------------------------")
    print("Symbol:", symbol)
    print("Company:", stock["name"])
    print("Sector:", stock["sector"])
    print("Industry:", stock["industry"])

    return symbol, stock


# STEP 3: Get latest available stock price
def get_current_price(symbol):
    try:
        # Yahoo Finance uses a hyphen for certain share-class tickers
        yahoo_symbol = symbol.replace(".", "-")

        stock = yf.Ticker(yahoo_symbol)
        history = stock.history(period="5d")

        if history.empty:
            print("Price data not available for", symbol)
            return None

        prices = history["Close"].dropna()

        if prices.empty:
            return None

        return float(prices.iloc[-1])

    except Exception as error:
        print("Price retrieval error:", error)
        return None


# STEP 4: Calculate stock performance
def calculate_stock(symbol, stock):
    try:
        buy_price = float(input("Enter buying price: "))
        shares = float(input("Enter number of shares: "))

        if buy_price <= 0 or shares <= 0:
            print("Price and shares must be greater than zero.")
            return None

    except ValueError:
        print("Please enter valid numeric values.")
        return None

    current_price = get_current_price(symbol)

    if current_price is None:
        return None

    invested = buy_price * shares
    current_value = current_price * shares

    profit_loss = current_value - invested
    percentage = (profit_loss / invested) * 100

    return {
        "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ticker": symbol,
        "company": stock["name"],
        "sector": stock["sector"],
        "buy_price": round(buy_price, 2),
        "shares": shares,
        "current_price": round(current_price, 2),
        "invested_value": round(invested, 2),
        "current_value": round(current_value, 2),
        "gain_loss": round(profit_loss, 2),
        "gain_loss_percent": round(percentage, 2)
    }


# STEP 5: Display portfolio results
def display_results(results):
    print("\n" + "=" * 105)
    print("             STOCK PORTFOLIO PERFORMANCE TRACKER")
    print("=" * 105)

    print(
        f"{'Ticker':<9}"
        f"{'Company':<24}"
        f"{'Buy Price':>12}"
        f"{'Current':>12}"
        f"{'Shares':>10}"
        f"{'Profit/Loss':>15}"
    )

    print("-" * 105)

    total_investment = 0
    total_value = 0

    for item in results:
        print(
            f"{item['ticker']:<9}"
            f"{item['company'][:22]:<24}"
            f"{item['buy_price']:>12.2f}"
            f"{item['current_price']:>12.2f}"
            f"{item['shares']:>10.2f}"
            f"{item['gain_loss']:>15.2f}"
        )

        total_investment += item["invested_value"]
        total_value += item["current_value"]

    total_gain = total_value - total_investment

    if total_investment:
        total_return = (total_gain / total_investment) * 100
    else:
        total_return = 0

    print("-" * 105)
    print(f"Total Investment : {total_investment:.2f}")
    print(f"Current Value    : {total_value:.2f}")
    print(f"Total Gain/Loss  : {total_gain:.2f}")
    print(f"Overall Return   : {total_return:.2f}%")
    print("=" * 105)


# STEP 6: Save results to CSV
def save_results(results):
    if not results:
        return

    fields = [
        "date_time",
        "ticker",
        "company",
        "sector",
        "buy_price",
        "shares",
        "current_price",
        "invested_value",
        "current_value",
        "gain_loss",
        "gain_loss_percent"
    ]

    file_exists = (
        os.path.exists(OUTPUT_FILE)
        and os.path.getsize(OUTPUT_FILE) > 0
    )

    with open(
        OUTPUT_FILE, "a", newline="", encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(file, fieldnames=fields)

        if not file_exists:
            writer.writeheader()

        writer.writerows(results)

    print("\nResults saved successfully!")
    print("Output file:", OUTPUT_FILE)


# STEP 7: Main program
def main():
    print("\nWELCOME TO STOCK PORTFOLIO PERFORMANCE TRACKER")

    stocks = load_stocks()

    if not stocks:
        print("Could not load the stock dataset.")
        return

    print(f"\nSuccessfully loaded {len(stocks)} stock records.")

    results = []

    try:
        count = int(input("\nHow many stocks do you want to track? "))

        if count <= 0:
            print("Enter a number greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    for i in range(count):
        print(f"\n========== STOCK {i + 1} ==========")

        selected = search_stock(stocks)

        if selected is None:
            print("Skipping invalid stock.")
            continue

        symbol, stock = selected

        result = calculate_stock(symbol, stock)

        if result is not None:
            results.append(result)

    if results:
        display_results(results)
        save_results(results)
    else:
        print("\nNo valid portfolio results available.")


if __name__ == "__main__":
    main()
