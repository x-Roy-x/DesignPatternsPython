from copy import deepcopy


class Token:
    def __init__(self, value=0):
        self.value = value

    def __str__(self):
        return f"Token: {self.value}"


class Memento(list):
    pass


class TokenMachine:
    def __init__(self):
        self.tokens = []

    def add_token_value(self, value):
        return self.add_token(Token(value))

    def add_token(self, token):
        self.tokens.append(token)
        return Memento(deepcopy(self.tokens))

    def revert(self, memento):
        self.tokens = [Token(token.value) for token in memento]

    def history(self):
        print("All tokens")
        for token in self.tokens:
            print(token)


if __name__ == '__main__':
    tm = TokenMachine()

    t = Token(5)
    m1 = tm.add_token(t)
    m2 = tm.add_token_value(2)
    m3 = tm.add_token_value(3)

    tm.history()

    t.value = 1
    tm.history()
    tm.revert(m3)
    tm.history()

    tm.revert(m2)
    tm.history()
