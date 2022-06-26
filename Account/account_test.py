import unittest

from Account import account


class AccountTest(unittest.TestCase):
    def test_that_account_can_be_created(self):
        account1 = account.Account("Ademola")
        self.assertIsNotNone(account1)
        self.assertIsInstance(account1, account.Account)

    def test_that_account_has_a_name(self):
        """
        GIVEN: an account class
        WHEN: i create an account object
        THEN: account object should have a name
        """

        account1 = account.Account("Ademola")
        name = account1.name
        self.assertEqual("Ademola", name)

    def test_that_account_can_deposit(self):
        """
        GIVEN: an account class
        WHEN: i create an account object
        THEN: account object should be reflected
        """
        account1 = account.Account("ADEMOLA")
        account1.deposit(2000)
        self.assertEqual(2000, account1.balance)

    def test_that_negative_deposit_is_invalid_and_raises_an_error(self):
        account1 = account.Account("ADEMOLA")
        account1.deposit(2000)

        self.assertRaises(ValueError, account1.deposit, -1000)

        self.assertEqual(2000, account1.balance)

    def test_that_we_can_withdraw_from_the_account(self):
        account1 = account.Account("Ademola")
        account1.deposit(2000)
        account1.withdraw(1000)
        self.assertEqual(1000, account1.balance)

    def test_that_we_cannot_withdraw_more_than_our_balance(self):
        account1 = account.Account("Ademola")
        account1.deposit(2000)

        self.assertRaises(ValueError, account1.withdraw, 3000)

    def test_that_we_can_make_a_transfer_from_one_bank_to_another(self):
        account1 = account.Account("Ademola")
        account2 = account.Account("Ayoola")
        account1.deposit(2000)
        account1.transfer(2000, account2)
        # self.assertEqual(2000, account2.balance)
        self.assertEqual(0, account1.balance)

    def test_that_we_cab_buy_recharge_card(self):
        account1 = account.Account("Ademola")
        account1.deposit(2000)
        account1.buy_airtime(500)
        self.assertEqual(1500, account1.balance)



if __name__ == '__main__':
    unittest.main()
