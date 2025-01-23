# payment.py

class PaymentSystem:
    def validate_card(self, card_number):
        """Validate card number using Luhn algorithm."""
        card_number = str(card_number)
        total = 0
        reverse_digits = card_number[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

    def authenticate_user(self, user_id, pin):
        """Mock authentication that checks if the user ID and PIN are correct."""
        # For simplicity, assume user_id 'user123' and pin '1234' are valid
        return user_id == 'user123' and pin == '1234'

    def process_payment(self, card_number, amount, user_id, pin):
        """Process the payment if card and user authentication are valid."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        if not self.validate_card(card_number):
            raise ValueError("Invalid card number")

        if not self.authenticate_user(user_id, pin):
            raise PermissionError("Authentication failed")

        # Mock payment processing logic
        return f"Payment of ${amount} processed for user {user_id}"