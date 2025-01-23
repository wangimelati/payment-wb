# main.py

from payment import PaymentSystem

def main():
    # Initialize the payment system
    payment_system = PaymentSystem()

    # Input data
    card_number = input("Enter card number: ").strip()
    user_id = input("Enter user ID: ").strip()
    pin = input("Enter PIN: ").strip()
    try:
        amount = float(input("Enter payment amount: ").strip())
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    # Process payment
    try:
        result = payment_system.process_payment(card_number, amount, user_id, pin)
        print(result)
    except ValueError as ve:
        print(f"Error: {ve}")
    except PermissionError as pe:
        print(f"Error: {pe}")

if __name__ == "__main__":
    main()
