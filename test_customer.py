import unittest
from customer import Customer
import coins

class TestGetWalletCoin(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer()
        
    def test_get_quarter(self):
        """Passing in 'Quarter' string will return a Quarter object"""
        returned_coin = self.customer.get_wallet_coin("Quarter")
        self.assertEqual(returned_coin.name, "Quarter")
        
    def test_get_dime(self):
        """Passing in 'Dime' string will return a Dime object"""
        returned_coin = self.customer.get_wallet_coin("Dime")
        self.assertEqual(returned_coin.name, "Dime")
        
    def test_get_nickel(self):
        """Passing in 'Nickel' string will return a Nickel object"""
        returned_coin = self.customer.get_wallet_coin("Nickel")
        self.assertEqual(returned_coin.name, "Nickel")
        
    def test_get_penny(self):
        """Passing in 'Penny' string will return a Penny object"""
        returned_coin = self.customer.get_wallet_coin("Penny")
        self.assertEqual(returned_coin.name, "Penny")
        
        
if __name__ == "__main__":
    unittest.main()