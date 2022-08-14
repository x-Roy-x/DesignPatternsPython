
class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        self.mediator.participants.append(self)

    def say(self, value):
        self.mediator.broadcast(self, value)


class Mediator:

    def __init__(self):
        self.participants = []

    def broadcast(self, sender, value):
        for participant in self.participants:
            if participant != sender:
                participant.value += value


if __name__ == '__main__':
    mediator = Mediator()

    participant1 = Participant(mediator)
    participant2 = Participant(mediator)

    participant1.say(3)

    print(participant1.value)
    print(participant2.value)
