import unittest
import customer
import coins
import cans

#* Tests whether or not the inputted coin value matches an assigned coin object

class TestGetWalletCoin(unittest.TestCase):
    
    def setUp(self):
        self.customer = customer.Customer()
        
    def test_get_quarter(self):
        """Passing in 'Quarter' string will return a Quarter object"""
        returned_coin = self.customer.get_wallet_coin("Quarter")
        self.assertIsInstance(returned_coin, coins.Quarter)
        
    def test_get_dime(self):
        """Passing in 'Dime' string will return a Dime object"""
        returned_coin = self.customer.get_wallet_coin("Dime")
        self.assertIsInstance(returned_coin, coins.Dime)
        
    def test_get_nickel(self):
        """Passing in 'Nickel' string will return a Nickel object"""
        returned_coin = self.customer.get_wallet_coin("Nickel")
        self.assertIsInstance(returned_coin, coins.Nickel)
        
    def test_get_penny(self):
        """Passing in 'Penny' string will return a Penny object"""
        returned_coin = self.customer.get_wallet_coin("Penny")
        self.assertIsInstance(returned_coin, coins.Penny)
        
        
#^ Tests whether the length of the coin list increases when coins are appended 

class TestAddCoinsToWallet(unittest.TestCase):
    
    def setUp(self):
        self.customer = customer.Customer()
                
    def test_add_coins(self):
        
        this_coin_list = [coins.Quarter(), coins.Nickel(), coins.Penny()]
        self.customer.add_coins_to_wallet(this_coin_list)
        print(len(self.customer.wallet.money))

#! Tests whether the length of the backpack list increases when coins are appended

class TestAddCansToBackpack(unittest.TestCase):
    
    def setUp(self):
        self.customer = customer.Customer()
        
    def test_add_cans(self):
        cola = cans.Cola()
        self.customer.add_can_to_backpack(cola)
        print(len(self.customer.backpack.purchased_cans))
        

if __name__ == "__main__":
    unittest.main()