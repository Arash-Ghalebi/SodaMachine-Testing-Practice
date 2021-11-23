import unittest
# from customer import Customer
import customer
# import wallet
# import coins

#* Tests whether or not the inputted coin value matches an assigned coin object
# class TestGetWalletCoin(unittest.TestCase):
    
#     def setUp(self):
#         self.customer = Customer()
        
#     def test_get_quarter(self):
#         """Passing in 'Quarter' string will return a Quarter object"""
#         returned_coin = self.customer.get_wallet_coin("Quarter")
#         self.assertIsInstance(returned_coin, coins.Quarter)
        
#     def test_get_dime(self):
#         """Passing in 'Dime' string will return a Dime object"""
#         returned_coin = self.customer.get_wallet_coin("Dime")
#         self.assertIsInstance(returned_coin, coins.Dime)
        
#     def test_get_nickel(self):
#         """Passing in 'Nickel' string will return a Nickel object"""
#         returned_coin = self.customer.get_wallet_coin("Nickel")
#         self.assertIsInstance(returned_coin, coins.Nickel)
        
#     def test_get_penny(self):
#         """Passing in 'Penny' string will return a Penny object"""
#         returned_coin = self.customer.get_wallet_coin("Penny")
#         self.assertIsInstance(returned_coin, coins.Penny)
        
        
class TestAddCoinsToWallet(unittest.TestCase):
    
    def setUp(self):
        self.customer = customer.Customer()
        
        
    def test_add_coins(self):
        coins_list = ["Quarter", "Dime", "Nickel"]
        for coin in coins_list:
            try:
                self.customer.wallet.money.append(coin)
            except:
                pass
        print(self.customer.wallet.money)

if __name__ == "__main__":
    unittest.main()