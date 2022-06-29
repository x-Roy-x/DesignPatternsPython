def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:

    def __init__(self, id):
        self.id = id
        print("Loading database")


if __name__ == "__main__":

    db1 = Database(2)
    db2 = Database(3)

    print(db1 == db2)
