

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        memento = Memento(self.name, self.balance)
        return memento

    def __str__(self):
        return f"{self.name} current balance: {self.balance}"


class Memento:

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    @property
    def name(self):
        return self._name

    @property
    def balance(self):
        return self._balance

    def __str__(self):
        return f"{self.name} current balance: {self.balance}"


class BankAccountController:

    def __init__(self, bank_account):
        self._bank_account = bank_account
        self._mementos = [Memento(self._bank_account.name, self._bank_account.balance)]
        self._mementos_position = 0

    def take_deposit(self, amount):
        memento = self._bank_account.deposit(amount)
        self._mementos.append(memento)
        self._mementos_position += 1

    def undo(self):
        if 0 < self._mementos_position:
            self._mementos_position -= 1
            memento = self._mementos[self._mementos_position]
            self._bank_account.name = memento.name
            self._bank_account.balance = memento.balance

    def redo(self):
        if len(self._mementos) > self._mementos_position + 1:
            self._mementos_position += 1
            memento = self._mementos[self._mementos_position]
            self._bank_account.name = memento.name
            self._bank_account.balance = memento.balance

    def history(self):
        print("All operation")
        for memento in self._mementos:
            print(memento)


if __name__ == '__main__':
    ba = BankAccount("Roi", 100)

    ba_controller = BankAccountController(ba)

    ba_controller.take_deposit(100)
    ba_controller.take_deposit(25)

    print(ba)

    ba_controller.undo()
    print(ba)

    ba_controller.undo()
    print(ba)

    ba_controller.redo()
    print(ba)

    ba_controller.redo()
    print(ba)

    ba_controller.redo()
    print(ba)

    ba_controller.history()

