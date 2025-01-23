# test_payment.py
import unittest
from payment import PaymentSystem

class TestPaymentSystem(unittest.TestCase):
    
    def setUp(self):
        self.payment_system = PaymentSystem()
    
    def test_validate_card_valid(self):
        """Test with a valid card number (using Luhn's algorithm)."""
        self.assertTrue(self.payment_system.validate_card(4532015112830366))

    def test_validate_card_invalid(self):
        """Test with an invalid card number."""
        self.assertFalse(self.payment_system.validate_card(1234567890123456))

    def test_authenticate_user_valid(self):
        """Test user authentication with correct credentials."""
        self.assertTrue(self.payment_system.authenticate_user('user123', '1234'))

    def test_authenticate_userPASS_invalid(self):
        """Test user authentication with incorrect credentials."""
        self.assertFalse(self.payment_system.authenticate_user('user123', 'wrongpin'))

    def test_authenticate_userUSN_invalid(self):
        """Test user authentication with incorrect credentials."""
        self.assertFalse(self.payment_system.authenticate_user('wronguser', '1234'))

    def test_process_payment_success(self):
        """Test successful payment process."""
        result = self.payment_system.process_payment(4532015112830366, 100, 'user123', '1234')
        self.assertEqual(result, "Payment of $100 processed for user user123")

    def test_process_payment_invalid_card(self):
        """Test payment with invalid card number."""
        with self.assertRaises(ValueError):
            self.payment_system.process_payment(1234567890123456, 100, 'user123', '1234')

    def test_process_payment_authentication_failed(self):
        """Test payment with authentication failure."""
        with self.assertRaises(PermissionError):
            self.payment_system.process_payment(4532015112830366, 100, 'user123', 'wrongpin')

    def test_process_payment_invalid_amount(self):
        """Test payment with invalid amount."""
        with self.assertRaises(ValueError):
            self.payment_system.process_payment(4532015112830366, -50, 'user123', '1234')

    def test_process_payment_edge_case(self):
        with self.assertRaises(ValueError):
            self.payment_system.process_payment(4532015112830366, 0, 'user123', '1234')