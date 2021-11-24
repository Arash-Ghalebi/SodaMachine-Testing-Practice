from os import name
import user_interface
import unittest
import cans
import coins

class TestValidateMainMenu(unittest.TestCase):
    
    
    def test_main_menu_1(self):
        """Tests If an inputted number will return the appropriate tuple"""
        self.user_interface = user_interface
        self.assertIn(1, self.user_interface.validate_main_menu(1))
        
    def test_main_menu_2(self):
        self.user_interface = user_interface
        self.assertIn(2, self.user_interface.validate_main_menu(2))
        
    def test_main_menu_3(self):
        self.user_interface = user_interface
        self.assertIn(3, self.user_interface.validate_main_menu(3))
        
    def test_main_menu_4(self):
        self.user_interface = user_interface
        self.assertIn(4, self.user_interface.validate_main_menu(4))
        
    def test_main_menu_5(self):  #* This one fails the test because the main menu is only coded to accept int 1-4
        """Tests If an inputted number will return the 'False' Tuple"""
        self.user_interface = user_interface
        self.assertIn(5, self.user_interface.validate_main_menu(5))
        
    def test_parse_int_1(self):
        """Tests if user input integers are returned appropriately"""
        self.user_interface = user_interface
        self.assertEquals(self.user_interface.try_parse_int(10), 10)
        
    def test_parse_int_2(self):
        """Tests that a string input will equal 0"""
        self.user_interface = user_interface
        self.assertEquals(self.user_interface.try_parse_int("Hello"), 0)
        
        
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
        """Tests that each coin value will be added to a total opf .41"""
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
        self.user_interface = user_interface
        self.assertIn("Quarter", self.user_interface.validate_coin_selection(1))
        
    def test_validate_coins_2(self):
        """Tests if 'Dime' is one of the assigned coins"""
        self.user_interface = user_interface
        self.assertIn("Dime", self.user_interface.validate_coin_selection(2))
     
    def test_validate_coins_3(self):
        """Tests if 'Nickel' is one of the assigned coins"""
        self.user_interface = user_interface
        self.assertIn("Nickel", self.user_interface.validate_coin_selection(3))
    
    def test_validate_coins_4(self):
        """Tests if 'Penny' is one of the assigned coins"""
        self.user_interface = user_interface
        self.assertIn("Penny", self.user_interface.validate_coin_selection(4))
        
    def test_validate_coins_5(self):
        """Tests that an input of 5 will return 'Done'"""
        self.user_interface = user_interface
        self.assertIn("Done", self.user_interface.validate_coin_selection(5))
        
    def test_validate_coins_6(self):
          """Tests that any number outside of 1-5 returns 'False, None'"""
          self.user_interface = user_interface
          self.assertIn("None", self.user_interface.validate_coin_selection(6))
     
  
if __name__ =="__main__":
    unittest.main()