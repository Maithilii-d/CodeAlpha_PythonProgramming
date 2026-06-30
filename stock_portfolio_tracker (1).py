import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135,
    "NFLX": 420,
    "META": 310
}


def display_stocks():
    print("\nAvailable Stocks")
    print("-" * 35)
    print(f"{'Stock':<10}{'Price ($)':>10}")
    print("-" * 35)
    for stock, price in stock_prices.items():
        print(f"{stock:<10}{price:>10}")
    print("-" * 35)


def get_number_of_stocks():
    while True:
        try:
            count = int(input("\nEnter the number of different stocks you own: "))
            if count > 0:
                return count
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def get_stock_details(count):
    portfolio = []
    for i in range(count):
        print(f"\nStock {i + 1}")

        while True:
            stock = input("Enter stock symbol: ").upper().strip()
            if stock in stock_prices:
                break
            print("Invalid stock! Please enter one from the available list.")

        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity > 0:
                    break
                print("Quantity must be greater than 0.")
            except ValueError:
                print("Please enter a valid integer.")

        investment = stock_prices[stock] * quantity

        portfolio.append({
            "Stock": stock,
            "Quantity": quantity,
            "Price": stock_prices[stock],
            "Investment": investment
        })

    return portfolio


def display_summary(portfolio):
    print("\n" + "=" * 65)
    print("                     PORTFOLIO SUMMARY")
    print("=" * 65)
    print(f"{'Stock':<10}{'Qty':<10}{'Price($)':<15}{'Investment($)':<15}")
    print("-" * 65)

    total = 0
    highest_stock = ""
    highest_value = 0

    for item in portfolio:
        print(f"{item['Stock']:<10}{item['Quantity']:<10}{item['Price']:<15}{item['Investment']:<15}")
        total += item["Investment"]
        if item["Investment"] > highest_value:
            highest_value = item["Investment"]
            highest_stock = item["Stock"]

    print("-" * 65)
    print(f"{'Total Investment':<35}${total:.2f}")
    print("=" * 65)

    print(f"\nHighest Investment Stock : {highest_stock}")
    print(f"Investment Value         : ${highest_value:.2f}")

    print("\nPortfolio Contribution:")
    for item in portfolio:
        percentage = (item["Investment"] / total) * 100
        print(f"{item['Stock']:<10}: {percentage:.2f}%")

    return total


def save_txt(portfolio, total):
    with open("portfolio_report.txt", "w") as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 50 + "\n\n")
        file.write(f"{'Stock':<10}{'Qty':<10}{'Price':<10}{'Investment':<15}\n")
        file.write("-" * 50 + "\n")
        for item in portfolio:
            file.write(f"{item['Stock']:<10}{item['Quantity']:<10}{item['Price']:<10}{item['Investment']:<15}\n")
        file.write("-" * 50 + "\n")
        file.write(f"Total Investment = ${total:.2f}\n")


def save_csv(portfolio, total):
    with open("portfolio_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Investment"])
        for item in portfolio:
            writer.writerow([item["Stock"], item["Quantity"], item["Price"], item["Investment"]])
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total])


print("=" * 60)
print("            STOCK PORTFOLIO TRACKER")
print("       CodeAlpha Python Internship - Task 2")
print("=" * 60)

display_stocks()
number = get_number_of_stocks()
portfolio = get_stock_details(number)
total = display_summary(portfolio)

choice = input("\nDo you want to save the report? (Y/N): ").upper()

if choice == "Y":
    save_txt(portfolio, total)
    save_csv(portfolio, total)
    print("\nPortfolio saved successfully!")
    print("- portfolio_report.txt")
    print("- portfolio_report.csv")
else:
    print("\nReport was not saved.")

print("\nThank you for using the Stock Portfolio Tracker!")
