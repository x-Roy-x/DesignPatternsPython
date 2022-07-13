import time


def time_it(function):
    def wrapper():
        start = time.time()

        result = function()

        end = time.time()
        duration = end - start
        print(f"{function.__name__} took {duration} s")
        return result

    return wrapper


@time_it
def some_operation():
    print("Statr operation")
    time.sleep(1)
    print("We are done")
    return 0


if __name__ == '__main__':
    #some_operation()
    #time_it(some_operation)()
    some_operation()
