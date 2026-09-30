import csv

# Hardcoded dictionary defining stock prices (ticker -> price in USD)
STOCK_PRICES = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "MSFT": 420.0,
    "AMZN": 185.0,
    "GOOGL": 175.0,
    "NVDA": 120.0
}

def display_available_stocks():
    print("\nAvailable Stocks & Prices:")
    print("-" * 30)
    for ticker, price in STOCK_PRICES.items():
        print(f" • {ticker}: ${price:.2f}")
    print("-" * 30)

def save_portfolio_to_file(portfolio, total_investment):
    """Saves portfolio summary to both TXT and CSV formats."""
    # Save to TXT file
    with open("portfolio_summary.txt", "w") as txt_file:
        txt_file.write("=== STOCK PORTFOLIO SUMMARY ===\n")
        for symbol, data in portfolio.items():
            txt_file.write(f"Stock: {symbol} | Quantity: {data['quantity']} | "
                           f"Unit Price: ${data['price']:.2f} | Total Value: ${data['total']:.2f}\n")
        txt_file.write("-" * 40 + "\n")
        txt_file.write(f"Total Investment Value: ${total_investment:.2f}\n")

    # Save to CSV file
    with open("portfolio_summary.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Stock Symbol", "Quantity", "Price Per Share", "Total Value"])
        for symbol, data in portfolio.items():
            writer.writerow([symbol, data["quantity"], f"{data['price']:.2f}", f"{data['total']:.2f}"])
        writer.writerow([])
        writer.writerow(["TOTAL INVESTMENT", "", "", f"{total_investment:.2f}"])

    print("\n✅ Portfolio summary saved successfully to 'portfolio_summary.txt' and 'portfolio_summary.csv'!")

def main():
    portfolio = {}
    total_investment = 0.0

    print("========================================")
    print("      STOCK PORTFOLIO TRACKER          ")
    print("========================================")

    display_available_stocks()

    while True:
        symbol = input("\nEnter Stock Symbol to add (or type 'DONE' to finish): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"⚠️ '{symbol}' is not in the price list. Please pick from available stocks.")
            continue

        try:
            quantity = int(input(f"Enter quantity of shares for {symbol}: "))
            if quantity <= 0:
                print("⚠️ Quantity must be greater than zero.")
                continue
        except ValueError:
            print("⚠️ Invalid input! Please enter a whole number for quantity.")
            continue

        # Calculate holding value
        unit_price = STOCK_PRICES[symbol]
        position_total = unit_price * quantity

        # Update existing entry or create new
        if symbol in portfolio:
            portfolio[symbol]["quantity"] += quantity
            portfolio[symbol]["total"] += position_total
        else:
            portfolio[symbol] = {
                "quantity": quantity,
                "price": unit_price,
                "total": position_total
            }

        print(f"✅ Added {quantity} shares of {symbol} (${position_total:.2f}).")

    if not portfolio:
        print("\nNo stocks were added to your portfolio.")
        return

    # Display Final Summary
    print("\n========================================")
    print("         PORTFOLIO SUMMARY              ")
    print("========================================")
    print(f"{'Symbol':<10} {'Quantity':<10} {'Unit Price':<12} {'Total Value':<12}")
    print("-" * 46)

    for symbol, data in portfolio.items():
        print(f"{symbol:<10} {data['quantity']:<10} ${data['price']:<11.2f} ${data['total']:<11.2f}")
        total_investment += data["total"]

    print("-" * 46)
    print(f"TOTAL INVESTMENT VALUE: ${total_investment:.2f}")
    print("========================================")

    # File saving prompt
    save_choice = input("\nDo you want to save this summary to a file? (yes/no): ").strip().lower()
    if save_choice in ["yes", "y"]:
        save_portfolio_to_file(portfolio, total_investment)

if __name__ == "__main__":
    main()
