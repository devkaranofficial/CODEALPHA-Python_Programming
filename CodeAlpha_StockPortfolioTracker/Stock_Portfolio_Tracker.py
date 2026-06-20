# ==============================
# CODEALPHA TASK 2
# STOCK PORTFOLIO TRACKER
# ==============================

stock_prices = {
    "Google": 1500,
    "AMD": 1200,
    "Infosys": 800,
    "Nvidia": 1100,
    "Intel": 1300
}

portfolio = {}


def display_stocks():
    print("\n" + "=" * 70)
    print("                  STOCK PORTFOLIO TRACKER")
    print("=" * 70)

    print("\n{:<15} {:<15}".format("STOCK", "PRICE (₹)"))
    print("-" * 70)

    for stock, price in stock_prices.items():
        print("{:<15} {:<15}".format(stock, price))

    print("-" * 70)


def get_stock_name():
    stock_name = input("Enter Stock Name: ").strip()

    for stock in stock_prices:
        if stock.lower() == stock_name.lower():
            return stock

    return None


# ==============================
# MAIN PROGRAM
# ==============================

while True:

    display_stocks()

    choice = input("\nDo you want to buy stocks? (Y/N): ").upper()

    if choice == "Y":

        stock_name = get_stock_name()

        if stock_name is None:
            print("\n❌ Stock not available!")
            continue

        try:
            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("\n❌ Quantity must be greater than 0")
                continue

        except ValueError:
            print("\n❌ Please enter valid numbers only")
            continue

        investment = stock_prices[stock_name] * quantity

        if stock_name in portfolio:
            portfolio[stock_name]["quantity"] += quantity
            portfolio[stock_name]["investment"] += investment
        else:
            portfolio[stock_name] = {
                "quantity": quantity,
                "investment": investment
            }

        print("\n" + "-" * 50)
        print("           PURCHASE SUCCESSFUL")
        print("-" * 50)
        print(f"Stock      : {stock_name}")
        print(f"Quantity   : {quantity}")
        print(f"Unit Price : ₹{stock_prices[stock_name]}")
        print(f"Amount     : ₹{investment}")
        print("-" * 50)

    elif choice == "N":
        break

    else:
        print("\n❌ Invalid choice! Please enter Y or N.")

# ==============================
# PORTFOLIO SUMMARY
# ==============================

print("\n")
print("=" * 75)
print("                         PORTFOLIO SUMMARY")
print("=" * 75)

if len(portfolio) == 0:
    print("\nNo stocks purchased.")

else:

    print(
        "{:<15} {:<15} {:<20}".format(
            "STOCK",
            "QUANTITY",
            "INVESTMENT (₹)"
        )
    )

    print("-" * 75)

    total_investment = 0

    for stock, details in portfolio.items():

        print(
            "{:<15} {:<15} {:<20}".format(
                stock,
                details["quantity"],
                details["investment"]
            )
        )

        total_investment += details["investment"]

    print("-" * 75)
    print(f"TOTAL INVESTMENT VALUE : ₹{total_investment}")
    print("=" * 75)

    # Save Report
    with open("portfolio.txt", "w") as file:

        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 50 + "\n\n")

        for stock, details in portfolio.items():
            file.write(
                f"{stock} | Quantity: {details['quantity']} | Investment: Rs.{details['investment']}\n"
            )
            

        file.write("\n")
        file.write(f"TOTAL INVESTMENT VALUE : Rs.{total_investment}")

    print("\n📁 Portfolio report saved successfully to 'portfolio.txt'")

print("\nThank you for using Stock Portfolio Tracker!")