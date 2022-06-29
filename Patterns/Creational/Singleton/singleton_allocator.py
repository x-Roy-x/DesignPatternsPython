import random


class Database:

    _instance = None

    def __init__(self):
        self.id = random.randint(1, 100)
        print(f"id = {self.id}")

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)

        return cls._instance


if __name__ == "__main__":
    db1 = Database()
    db2 = Database()

    print(db1 == db2)
