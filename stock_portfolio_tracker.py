# ==============================
# CODEALPHA - STOCK PORTFOLIO TRACKER
# ==============================

import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 350,
    "AMZN": 140,
    "META": 320,
    "NFLX": 450,
    "NVDA": 500
}

portfolio = {}
total_value = 0

print("=" * 50)
print("        STOCK PORTFOLIO TRACKER")
print("=" * 50)

while True:
    stock = input("\nEnter Stock Symbol (Example: AAPL): ").upper()

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    try:
        quantity = int(input("Enter Quantity: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

    choice = input("Add another stock? (y/n): ").lower()

    if choice != "y":
        break

print("\n" + "=" * 50)
print("PORTFOLIO SUMMARY")
print("=" * 50)

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_value += investment

    print(f"{stock:<10} Qty: {qty:<5} Price: ${price:<8} Value: ${investment}")

print("=" * 50)
print(f"TOTAL INVESTMENT VALUE = ${total_value}")
print("=" * 50)

save = input("\nDo you want to save the portfolio? (y/n): ").lower()

if save == "y":

    # Save as TXT
    with open("portfolio.txt", "w") as file:
        file.write("STOCK PORTFOLIO TRACKER\n")
        file.write("=" * 40 + "\n")

        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            file.write(f"{stock} | Qty: {qty} | Price: ${price} | Value: ${investment}\n")

        file.write("=" * 40 + "\n")
        file.write(f"Total Investment = ${total_value}")

    # Save as CSV
    with open("portfolio.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["Stock", "Quantity", "Price", "Investment"])

        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            writer.writerow([stock, qty, price, investment])

        writer.writerow([])
        writer.writerow(["Total", "", "", total_value])

    print("\nPortfolio saved successfully!")
    print("Files Created:")
    print("1. portfolio.txt")
    print("2. portfolio.csv")

else:
    print("\nPortfolio not saved.")

print("\nThank you for using Stock Portfolio Tracker!")