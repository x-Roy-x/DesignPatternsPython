import abc


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
        self.success = None

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


if __name__ == '__main__':
    ba1 = BankAccount()

    ba1.deposit(5000)

    print(ba1)

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




