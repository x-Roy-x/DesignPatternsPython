class Singleton(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instance[cls]


class Database(metaclass=Singleton):

    def __init__(self, id):
        self.id = id
        print("Loading database")


if __name__ == "__main__":

    db1 = Database(2)
    db2 = Database(3)

    print(db1 == db2)
        
