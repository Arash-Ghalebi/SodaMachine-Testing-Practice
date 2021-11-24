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
        
    def test_get_other(self):
        """Passing in 'Other' string will return None"""
        returned_coin = self.customer.get_wallet_coin("Other")
        self.assertIsNone(returned_coin)
        

class TestAddCoinsToWallet(unittest.TestCase):
    
    def setUp(self):
        self.customer = customer.Customer()
                
    def test_add_coins(self):
        """Tests whether the length of the coin list increases when coins are appended """
        this_coin_list = [coins.Quarter(), coins.Nickel(), coins.Penny()]
        self.customer.add_coins_to_wallet(this_coin_list)
        self.assertEqual(len(self.customer.wallet.money), 91)
        
    def test_add_coins_2(self):
        """Tests whether the length of the coin list increases when coins are appended """
        this_coin_list = []
        self.customer.add_coins_to_wallet(this_coin_list)
        self.assertEqual(len(self.customer.wallet.money), 88)

class TestAddCansToBackpack(unittest.TestCase):
    
    def setUp(self):
        self.customer = customer.Customer()
        
    def test_add_cola(self):
        """Tests whether the length of the backpack list increases when cans are appended"""
        cola = cans.Cola()
        self.customer.add_can_to_backpack(cola)
        self.assertEqual(len(self.customer.backpack.purchased_cans), 1)
        
    def test_add_orange(self):
        """Tests whether the length of the backpack list increases when cans are appended"""
        cola = cans.OrangeSoda()
        self.customer.add_can_to_backpack(cola)
        self.assertEqual(len(self.customer.backpack.purchased_cans), 1)
        
    def test_add_root_beer(self):
        """Tests whether the length of the backpack list increases when cans are appended"""
        cola = cans.RootBeer()
        self.customer.add_can_to_backpack(cola)
        self.assertEqual(len(self.customer.backpack.purchased_cans), 1)
        

if __name__ == "__main__":
    unittest.main()