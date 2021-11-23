import unittest
import customer

#* Tests the len of given wallet list, instantiated through Customer Class

class TestWalletLen(unittest.TestCase):
    def setUp(self):
        
        self.customer = customer.Customer()

                  
    def test_wallet_len(self):
        self.customer.wallet.money
        print(len(self.customer.wallet.money))
        
if __name__ == "__main__":
    unittest.main()