

class Memento:
    
    def __init__(self, balance):
        self.balance = balance


class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

        self.changes = [Memento(self.balance)]
        self.memento_position = 0

    def deposit(self, amount):
        self.balance += amount

        memento = Memento(self.balance)
        self.changes.append(memento)
        self.memento_position += 1
        return memento

    def restore(self, memento):
        if memento:
            self.balance = memento.balance
            self.changes.append(memento)
            self.memento_position = len(self.changes) - 1

    def undo(self):
        if self.memento_position > 0:
            self.memento_position -= 1
            memento = self.changes[self.memento_position]
            self.balance = memento.balance

    def redo(self):
        if self.memento_position < len(self.changes) - 1:
            self.memento_position += 1
            memento = self.changes[self.memento_position]
            self.balance = memento.balance

    def __str__(self):
        return f"Balance = {self.balance}"


if __name__ == '__main__':
    ba = BankAccount(100)
    m1 = ba.deposit(100)
    m2 = ba.deposit(25)

    print(ba)

    ba.undo()

    print(ba)

    ba.undo()

    print(ba)

    ba.undo()

    print(ba)

    ba.redo()

    print(ba)
