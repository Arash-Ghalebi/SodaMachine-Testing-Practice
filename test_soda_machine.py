import unittest
from cans import Can, Cola
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

    def test_coin_returned_register_dime(self):
        """ Call get_coin_from_register with dime arguments to ensure they match the list."""
        coin = 'Dime'
        result = self.sodaMachine.get_coin_from_register(coin)
        self.assertEqual(result.name, 'Dime')

    def test_coin_returned_register_Quarter(self):
        """ Call get_coin_from_register with quarter arguments to ensure they match the list."""
        coin = 'Quarter'
        result = self.sodaMachine.get_coin_from_register(coin)
        self.assertEqual(result.name, 'Quarter')

    def test_coin_returned_register_nickel(self):
        """ Call get_coin_from_register with nickel arguments to ensure they match the list."""
        coin = 'Nickel'
        result = self.sodaMachine.get_coin_from_register(coin)
        self.assertEqual(result.name, 'Nickel')

    def test_coin_returned_register_penny(self):
        """ Call get_coin_from_register with penny arguments to ensure they match the list."""
        coin = 'Penny'
        result = self.sodaMachine.get_coin_from_register(coin)
        self.assertEqual(result.name, 'Penny')
        

class TestRegisterHasCoin(unittest.TestCase):
    def setUp(self):

        self.sodaMachine = soda_machine.SodaMachine()

    def test_register_has_dime(self):
        """ Call register_has_coin with Dime to ensure it is True."""
        coin = 'Dime'
        result = self.sodaMachine.register_has_coin(coin)
        self.assertTrue(result)

    def test_register_has_quarter(self):
        """ Call register_has_coin with Quarter to ensure it is True."""
        coin = 'Quarter'
        result = self.sodaMachine.register_has_coin(coin)
        self.assertTrue(result)

    def test_register_has_Nickel(self):
        """ Call register_has_coin with Nickel to ensure it is True."""
        coin = 'Nickel'
        result = self.sodaMachine.register_has_coin(coin)
        self.assertTrue(result)

    def test_register_has_Penny(self):
        """ Call register_has_coin with Penny to ensure it is True."""
        coin = 'Penny'
        result = self.sodaMachine.register_has_coin(coin)
        self.assertTrue(result)


class TestDetermineChangeValue(unittest.TestCase):
    def setUp(self):

        self.sodaMachine = soda_machine.SodaMachine()

    def test_change_value_paymenthigher(self):
        """ Testing to determine change value with greater payment than price, ensuring correct change is recorded for buyer."""
        result = self.sodaMachine.determine_change_value(10, 5)
        self.assertEqual(result, 5)

    def test_change_value_pricehigher(self):
        """Testing to determine change value with greater price than payment, ensuring that buyer still owes set amount for item."""
        result = self.sodaMachine.determine_change_value(5, 10)
        self.assertEqual(result, -5)

    def test_change_value_equalvalues(self):
        """Testing to determine change value with equal payment and price, meaning that no change is owed (0)."""
        result = self.sodaMachine.determine_change_value(10, 10)
        self.assertEqual(result, 0)


class TestCalculateCoinValue(unittest.TestCase):
    def setUp(self):

        self.sodaMachine = soda_machine.SodaMachine()

    def test_calculate_coin_value(self):
        """Testing obtaining the value of the sum of each of the four coins."""
        this_coin_list = [coins.Quarter(), coins.Nickel(), coins.Dime(), coins.Penny()]
        result = self.sodaMachine.calculate_coin_value(this_coin_list)
        self.assertEqual(result, .41)

    def test_calculate_coin_value_empty(self):
        """Testing obtaining the value of an empty list."""
        this_coin_list = []
        result = self.sodaMachine.calculate_coin_value(this_coin_list)
        self.assertEqual(result, 0)


class TestGetInventorySoda(unittest.TestCase):
    def setUp(self):

        self.sodaMachine = soda_machine.SodaMachine()

    def test_get_inventory_cola(self):
        """Testing to insert the string Cola into the function to ensure it is returned."""
        soda = 'Cola'
        result = self.sodaMachine.get_inventory_soda(soda)
        self.assertEqual(result.name, soda)

    def test_get_inventory_orangesoda(self):
        """Testing to insert the string Orange Soda into the function to ensure it is returned."""
        soda = 'Orange Soda'
        result = self.sodaMachine.get_inventory_soda(soda)
        self.assertEqual(result.name, soda)

    def test_get_inventory_rootbeer(self):
        """Testing to insert the string Root Beer into the function to ensure it is returned."""
        soda = 'Root Beer'
        result = self.sodaMachine.get_inventory_soda(soda)
        self.assertEqual(result.name, soda)

    def test_get_inventory_mountaindew(self):
        """Testing to insert the string Mountain Dew into the function to get None returned."""
        soda = 'Mountain Dew'
        result = self.sodaMachine.get_inventory_soda(soda)
        self.assertIsNone(result, soda)


class TestReturnInventory(unittest.TestCase):
    def setUp(self):

        self.sodaMachine = soda_machine.SodaMachine()
        self.can = Can('Cola', 2.50)

    def test_return_inventory(self):
        """Testing to see if the new initialized can was added to the inventory."""
        self.sodaMachine.return_inventory(self.can)
        self.assertEqual(len(self.sodaMachine.inventory), 31)

class TestDepositCoinsIntoRegister(unittest.TestCase):
    def setUp(self):

        self.sodaMachine = soda_machine.SodaMachine()

    def test_coin_deposit_register(self):
        """Testing to ensure the new length of the register list is 92."""
        this_coin_list = [coins.Quarter(), coins.Nickel(), coins.Dime(), coins.Penny()]
        self.sodaMachine.deposit_coins_into_register(this_coin_list)
        self.assertEqual(len(self.sodaMachine.register), 92)


        
if __name__ == "__main__":
    unittest.main()