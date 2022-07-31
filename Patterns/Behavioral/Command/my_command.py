import abc


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name} balance is {self.balance}"


class Command(abc.ABC):

    def __init__(self):
        self.success = False

    def get_result(self):
        return self.success

    @abc.abstractmethod
    def execute_command(self):
        pass

    @abc.abstractmethod
    def back_command(self):
        pass


class BankDepositCommand(Command):

    def __init__(self, bank_account, amount):
        super().__init__()
        self.bank_account = bank_account
        self.amount = amount

    def execute_command(self):
        self.bank_account.balance += self.amount
        self.success = True

    def back_command(self):
        if self.success:
            self.bank_account.balance -= self.amount

    def __str__(self):
        return f"Possible deposit: {self.amount}, {self.bank_account}"


class BankWithdrawCommand(Command):

    OVERDRAFT_LIMIT = -500

    def __init__(self, bank_account, amount):
        super().__init__()
        self.bank_account = bank_account
        self.amount = amount

    def execute_command(self):
        if self.bank_account.balance - self.amount >= self.OVERDRAFT_LIMIT:
            self.bank_account.balance -= self.amount
            self.success = True

    def back_command(self):
        if self.success:
            self.bank_account.balance += self.amount

    def __str__(self):
        return f"Possible withdraw: {self.amount}, {self.bank_account}"


class BankTransferCommand(Command):
    OVERDRAFT_LIMIT = -500

    def __init__(self, bank_account, amount, transfer_account):
        super().__init__()
        self.bank_account = bank_account
        self.amount = amount
        self.transfer_account = transfer_account

        self.bank_withdraw_cmd = BankWithdrawCommand(self.bank_account, self.amount)
        self.bank_deposit_cmd = BankDepositCommand(self.transfer_account, self.amount)

    def execute_command(self):
        result2 = False
        self.bank_withdraw_cmd.execute_command()
        result1 = self.bank_withdraw_cmd.get_result()

        if result1:
            self.bank_deposit_cmd.execute_command()
            result2 = self.bank_deposit_cmd.get_result()

        self.success = result1 and result2

    def back_command(self):
        result2 = False
        self.bank_withdraw_cmd.back_command()
        result1 = self.bank_withdraw_cmd.get_result()

        if result1:
            self.bank_deposit_cmd.back_command()
            result2 = self.bank_deposit_cmd.get_result()

        self.success = result1 and result2

    def __str__(self):
        return f"Possible transfer: {self.amount}, from {self.bank_account} to {self.transfer_account}"

            
class Invoker:
    
    def __init__(self, commands=[]):
        self.commands = commands

    def add_command(self, command):
        self.commands.append(command)

    def invoke(self):
        result = True
        for command in self.commands:
            if result:
                command.execute_command()
                result = command.get_result()

    def undo(self):
        for command in self.commands:
            command.back_command()


if __name__ == '__main__':
    ba1 = BankAccount("Roi", 100)
    ba2 = BankAccount("Kozak", 100)

    invoker = Invoker()

    invoker.add_command(BankTransferCommand(ba1, 100, ba2))
    invoker.add_command(BankDepositCommand(ba1, 100))
    invoker.add_command(BankWithdrawCommand(ba1, 300))

    invoker.invoke()
    print(ba1)
    print(ba2)

    invoker.undo()
    print(ba1)
    print(ba2)




