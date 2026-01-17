# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 135
}

portfolio = {}
total_investment = 0

print("📈 Welcome to Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' to finish entering stocks.\n")

# User input loop
while True:
    stock = input("Enter stock symbol: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available. Try again.\n")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("❗ Quantity must be positive.\n")
            continue
    except ValueError:
        print("❗ Please enter a valid number.\n")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    print("✅ Stock added successfully.\n")

# Calculation
print("\n📊 Portfolio Summary")
print("-" * 30)

for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock} | Quantity: {qty} | Value: ${value}")

print("-" * 30)
print(f"💰 Total Investment Value: ${total_investment}")

# Save to file (optional)
save = input("\nDo you want to save this report to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_report.txt", "w") as file:
        file.write("Stock Portfolio Report\n")
        file.write("-" * 30 + "\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock} | Quantity: {qty} | Value: ${value}\n")
        file.write("-" * 30 + "\n")
        file.write(f"Total Investment: ${total_investment}\n")

    print("📁 Report saved as portfolio_report.txt")

print("\n✅ Thank you for using Stock Portfolio Tracker!")
