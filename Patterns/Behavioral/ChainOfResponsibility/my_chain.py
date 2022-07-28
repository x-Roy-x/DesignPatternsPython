import abc
from enum import Enum


class User:

    def __init__(self, name, age, work, year_salary):
        self.name = name
        self.age = age
        self.work = work
        self.salary = year_salary
        self.max_credit_sum = 0


class Work(Enum):

    UNEMPLOYED = 1
    GOVERNMENT = 2
    IT = 3


class ChainOfResponsibility(abc.ABC):

    @abc.abstractmethod
    def add_verifier(self, next_verifier):
        pass

    @abc.abstractmethod
    def verify(self):
        pass


class Credit(ChainOfResponsibility):

    def __init__(self, user):
        self.user = user
        self.verifier = None

    def add_verifier(self, next_verifier):
        if self.verifier:
            self.verifier.add_verifier(next_verifier)
        else:
            self.verifier = next_verifier

    def verify(self):
        if self.verifier:
            self.verifier.verify()

    def __str__(self):
        return f"Max credit sum {self.user.max_credit_sum} for {self.user.name}"


class VerifyAge(Credit):

    def verify(self):
        if self.user.age >= 18:
            self.user.max_credit_sum = 5000
            super().verify()


class VerifySalary(Credit):

    def verify(self):
        if self.user.salary >= 120000:
            self.user.max_credit_sum = 60000
            super().verify()


class VerifyWork(Credit):

    def verify(self):
        if self.user.work == Work.UNEMPLOYED:
            print("Call the police. Illegal business")
        else:
            super().verify()


if __name__ == '__main__':

    user = User("Roi", 18, Work.IT, 240000)

    credit = Credit(user)

    credit.add_verifier(VerifyAge(user))
    credit.add_verifier(VerifySalary(user))
    credit.add_verifier(VerifyWork(user))

    credit.verify()

    print(credit)
