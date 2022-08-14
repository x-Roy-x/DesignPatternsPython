
class Person:

    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room = None

    def receive(self, sender, message):
        sender_message = f"{sender}: {message}"
        print(f"[{self.name}'s chat session] {sender_message}")
        self.chat_log.append(sender_message)

    def private_message(self, who, message):
        self.room.message(self.name, who, message)

    def say(self, message):
        self.room.broadcast(self.name, message)


class ChatRoom:

    def __init__(self):
        self.people = []

    def join(self, person):
        join_msg = f"{person.name} joins the chat"
        self.broadcast('room', join_msg)

        person.room = self
        self.people.append(person)

    def broadcast(self, source, message):
        for person in self.people:
            if person.name != source:
                person.receive(source, message)

    def message(self, source, destination, message):
        for person in self.people:
            if person.name == destination:
                person.receive(source, message)


if __name__ == '__main__':
    room = ChatRoom()

    john = Person("John")
    jane = Person("Jane")

    room.join(john)
    room.join(jane)

    john.say("Hi")
    jane.say("Hi  John")

    simon = Person("Simon")
    room.join(simon)
    simon.say("Hello everyone!")

    jane.private_message('Simon', "Hi Simon")



