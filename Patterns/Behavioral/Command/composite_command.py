import abc
import unittest


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, balance {self.balance}")

    def withdraw(self, amount):
        success = False
        if self.balance - amount >= self.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrew {amount}, balance {self.balance}")
            success = True

        return success

    def __str__(self):
        return f"Balance {self.balance}"


class Command(abc.ABC):

    def __init__(self):
        self.success = False

    @abc.abstractmethod
    def invoke(self):
        pass

    @abc.abstractmethod
    def undo(self):
        pass


class BankAccountCommand(Command):
    class Action:
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, account, action, amount):
        self.account = account
        self.action = action
        self.amount = amount

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True

        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if self.success:
            if self.action == self.Action.DEPOSIT:
                self.account.withdraw(self.amount)

            elif self.action == self.Action.WITHDRAW:
                self.account.deposit(self.amount)


class CompositeBankAccountCommand(Command, list):

    def __init__(self, items=[]):
        super().__init__()
        for item in items:
            self.append(item)

    def invoke(self):
        for item in self:
            item.invoke()

    def undo(self):
        for item in reversed(self):
            item.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_account, to_account, amount):
        super().__init__([
            BankAccountCommand(from_account, BankAccountCommand.Action.WITHDRAW, amount),
            BankAccountCommand(to_account, BankAccountCommand.Action.DEPOSIT, amount)
        ])

    def invoke(self):
        ok = True
        for item in self:
            if ok:
                item.invoke()
                ok = item.success
            else:
                item.success = False


class TestSuite(unittest.TestCase):

    def test_composite_deposit(self):
        print("\ntest_composite_deposit")
        ba = BankAccount()

        deposit1 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
        deposit2 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 50)
        composite_ba_cmd = CompositeBankAccountCommand([deposit1, deposit2])

        composite_ba_cmd.invoke()
        print(ba)
        composite_ba_cmd.undo()
        print(ba)

    def test_transfer_fail(self):
        print("\ntest_transfer_fail")
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        amount = 1000

        wc = BankAccountCommand(ba1, BankAccountCommand.Action.WITHDRAW, amount)
        dc = BankAccountCommand(ba2, BankAccountCommand.Action.DEPOSIT, amount)

        transfer = CompositeBankAccountCommand([wc, dc])

        transfer.invoke()
        print(f"ba1 {ba1}, ba2: {ba2}")
        transfer.undo()
        print(f"ba1 {ba1}, ba2: {ba2}")

    def test_transfer(self):
        print("\ntest_transfer")
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        amount = 1000

        transfer = MoneyTransferCommand(ba1, ba2, amount)

        transfer.invoke()
        print(f"ba1 {ba1}, ba2: {ba2}")
        transfer.undo()
        print(f"ba1 {ba1}, ba2: {ba2}")


if __name__ == '__main__':
    unittest.main()

    """
    ba2 = BankAccount()

    ba_cmd = BankAccountCommand(ba2, BankAccountCommand.Action.DEPOSIT, 5000)

    ba_cmd.invoke()

    print(ba2)

    ba_cmd.undo()

    print(ba2)

    illegal_cmd = BankAccountCommand(ba2, BankAccountCommand.Action.WITHDRAW, 1000)

    illegal_cmd.invoke()

    print(ba2)

    illegal_cmd.undo()

    print(ba2)
    """




