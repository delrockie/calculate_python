def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

def main():
    # Prompting the user to enter the original price
    original_price = float(input('Enter the original price: '))

    # Prompting the user to enter the discount percentage
    discount_percent = float(input('Enter the discount percentage: '))

    # Calculating the final price after applying the discount
    final_price = calculate_discount(original_price, discount_percent)

    # Printing the final price
    if final_price == original_price:
        print(f'No discount applied. Final price: ${final_price:.2f}')
    else:
        print(f'Discount applied. Final price: ${final_price:.2f}')

if __name__ == "__main__":
    main()
