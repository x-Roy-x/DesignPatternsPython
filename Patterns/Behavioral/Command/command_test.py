from enum import Enum


class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount
        self.success = False


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def process(self, command):
        if command.Action.DEPOSIT == command.action:
            self.balance += command.amount
            command.success = True
        elif command.Action.WITHDRAW == command.action:
            command.success = self.balance >= command.amount
            if command.success:
                self.balance -= command.amount


if __name__ == '__main__':
    a = Account()

    cmd = Command(Command.Action.DEPOSIT, 100)
    a.process(cmd)

    print(a.balance)