import unittest
import soda_machine
import coins

class TestFillRegister(unittest.TestCase):
    def setUp(self):
        
        self.sodaMachine = soda_machine.SodaMachine()

                  
    def test_register_length(self):
        """ Call register list within instance of SodaMachine to ensure list is initialized to 88 objects when created."""
        self.assertEqual(len(self.sodaMachine.register), 88)

class TestFillInventory(unittest.TestCase):
    def setUp(self):

        self.sodaMachine = soda_machine.SodaMachine()

                  
    def test_inventory_length(self):
        """ Call inventory list within instance of SodaMachine to ensure list is initialized to 30 objects when created."""
        self.assertEqual(len(self.sodaMachine.inventory), 30)

class TestGetCoinFromRegister(unittest.TestCase):
    def setUp(self):

        self.sodaMachine = soda_machine.SodaMachine()

    def test_coin_returned_register(self):
        """ Call get_coin_from_register with specific coin arguments to ensure they match the list."""
        coin = 'Dime'
        result = self.sodaMachine.get_coin_from_register(coin)
        self.assertEqual(result.name, 'Dime')

        
if __name__ == "__main__":
    unittest.main()