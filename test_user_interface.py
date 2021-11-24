from os import name
from unittest import result
import user_interface
import unittest
import cans
import coins

class TestValidateMainMenu(unittest.TestCase):
    
    
    def test_main_menu_1(self):
        """Tests If an input of 1 will return the appropriate tuple (True, 1)"""
        result = user_interface.validate_main_menu(1)
        self.assertEqual(result, (True, 1))
        
    def test_main_menu_2(self):
        """Tests If an input of 2 will return the appropriate tuple (True, 2)"""
        result = user_interface.validate_main_menu(2)
        self.assertEqual(result, (True, 2))
        
    def test_main_menu_3(self):
        """Tests If an input of 3 will return the appropriate tuple (True, 3)"""
        result = user_interface.validate_main_menu(3)
        self.assertEqual(result, (True, 3))
        
    def test_main_menu_4(self):
        """Tests If an input of 4 will return the appropriate tuple (True, 4)"""
        result = user_interface.validate_main_menu(4)
        self.assertEqual(result, (True, 4))
        
    def test_main_menu_5(self):
        """Tests If an input of 5 will return the 'False' Tuple"""
        result = user_interface.validate_main_menu(5)
        self.assertEqual(result, (False, None))
        
    def test_parse_int_1(self):
        """Tests if user input integers are returned appropriately"""
        result = user_interface.try_parse_int(10)
        self.assertEquals(result, 10)
        
    def test_parse_int_2(self):
        """Tests that a string input will equal 0"""
        result = user_interface.try_parse_int("Hello")
        self.assertEquals(result, 0)
        
        
    def test_get_unique_can_names(self):
        """Tests whether the len of list is shortened to 3 from 6"""
        soda_list = []
        self.can_1 = cans.Cola()
        self.can_2 = cans.Cola()
        self.can_3 = cans.OrangeSoda()
        self.can_4 = cans.OrangeSoda()
        self.can_5 = cans.RootBeer()
        self.can_6 = cans.RootBeer()
        soda_list.append(self.can_1)
        soda_list.append(self.can_2)
        soda_list.append(self.can_3)
        soda_list.append(self.can_4)
        soda_list.append(self.can_5)
        soda_list.append(self.can_6)
        self.user_interface = user_interface
        self.assertEqual(3, len(self.user_interface.get_unique_can_names(soda_list)))
        
    def test_unique_empty_list(self):
        """Tests response to an empty list"""
        soda_list_1 = []
        self.user_interface = user_interface
        self.assertIsNot(0, self.user_interface.get_unique_can_names(soda_list_1))
        
    def test_display_payment_value(self):
        """Tests that each coin value will be added to a total of .41"""
        self.user_interface = user_interface
        this_coin_list = []
        this_coin_list = [coins.Quarter(), coins.Nickel(), coins.Dime(), coins.Penny()]
        result = self.user_interface.display_payment_value(this_coin_list)
        self.assertEqual(result, .41)
        
    def test_display_empty_payment(self):
        """Tests that an empty coin list has no value"""
        self.user_interface = user_interface
        coin_list = []
        result = self.user_interface.display_payment_value(coin_list)
        self.assertEqual(result, 0)
        
    def test_validate_coins(self):
        """Tests if 'Quarter' is one of the assigned coins"""
        result = user_interface.validate_coin_selection(1)
        self.assertEqual(result, (True, "Quarter"))
        
    def test_validate_coins_2(self):
        """Tests if 'Dime' is one of the assigned coins"""
        result = user_interface.validate_coin_selection(2)
        self.assertEqual(result, (True, "Dime"))
     
    def test_validate_coins_3(self):
        """Tests if 'Nickel' is one of the assigned coins"""
        result = user_interface.validate_coin_selection(3)
        self.assertEqual(result, (True, "Nickel"))
    
    def test_validate_coins_4(self):
        """Tests if 'Penny' is one of the assigned coins"""
        result = user_interface.validate_coin_selection(4)
        self.assertEqual(result, (True, "Penny"))
        
    def test_validate_coins_5(self):
        """Tests that an input of 5 will return 'Done'"""
        result = user_interface.validate_coin_selection(5)
        self.assertEqual(result, (True, "Done"))
        
    def test_validate_coins_6(self):
          """Tests that any number outside of 1-5 returns 'False, None'"""
          result = user_interface.validate_coin_selection(6)
          self.assertEqual(result, (False, None))
     
  
if __name__ =="__main__":
    unittest.main()