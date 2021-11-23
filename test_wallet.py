import unittest
import customer

class TestWalletLen(unittest.TestCase):
    def setUp(self):
        
        self.customer = customer.Customer()

                  
    def test_wallet_len(self):
        """Tests the len of given wallet list, instantiated through Customer Class"""
        self.customer.wallet.money
        self.assertEqual(len(self.customer.wallet.money), 88)
        
if __name__ == "__main__":
    unittest.main()