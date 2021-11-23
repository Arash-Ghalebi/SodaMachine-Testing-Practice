import user_interface
import unittest
import cans

class TestValidateMainMenu(unittest.TestCase):
    
    
    def test_main_menu_1(self):
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
        self.user_interface = user_interface
        self.assertIn(5, self.user_interface.validate_main_menu(5))
        
    def test_parse_int_1(self):
        self.user_interface = user_interface
        self.assertEquals(self.user_interface.try_parse_int(10), 10)
        
    def test_parse_int_2(self):  #^ This fails because "Hello" can't be parsed into an integer
        self.user_interface = user_interface
        self.assertEquals(self.user_interface.try_parse_int("Hello"), 0)
        
        
    def test_get_unique_can_names(self):
        
        soda_list = []
        self.cans = cans.Can("Cola", 0.60)
        soda_list.append(self.cans)
        self.user_interface = user_interface
        self.assertIn(soda_list[0].name, self.user_interface.get_unique_can_names(soda_list[0].name))
        
        
if __name__ =="__main__":
    unittest.main()