import abc
from abc import ABC


class Sender(abc.ABC):

    @abc.abstractmethod
    def send(self, message):
        pass


class NotificationSender(Sender):

    def send(self, message):
        return message


class DecoratorSender(Sender):

    def __init__(self, sender):
        self._sender = sender

    @property
    def sender(self):
        return self._sender

    def send(self, message):
        self._sender.send(message)


class EmailSender(DecoratorSender):

    def send(self, message):
        return f"You have Email message: {self.sender.send(message)}"


class SMSSender(DecoratorSender):

    def send(self, message):
        return f"You have SMS message: {self.sender.send(message)}"


def send(sender, message):
    print(sender.send(message))


if __name__ == '__main__':
    simple = NotificationSender()

    send(simple, "Hi. I am human")

    email = EmailSender(simple)
    sms = SMSSender(email)

    send(sms, "Hi. I am human")



