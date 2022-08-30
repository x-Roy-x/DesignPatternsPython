import abc


class Game(abc.ABC):

    def __init__(self, player_numbers):
        self.player_numbers = player_numbers
        self.current_player = 0

    def run(self):
        self.start()

        while not self.have_winner():
            self.take_turn()

        print(f"Player {self.winning_player} wins!")

    def start(self):
        pass

    def have_winner(self):
        pass

    def take_turn(self):
        pass

    @property
    def winning_player(self):
        pass


class Chess(Game):

    def __init__(self):
        super().__init__(2)
        self.max_turns = 10
        self.turn = 1

    def run(self):
        super().run()

    def start(self):
        print(f"Starting a chess game with {self.player_numbers} players")

    def have_winner(self):
        return self.turn == self.max_turns

    def take_turn(self):
        print(f"Turn {self.turn} taken by player {self.current_player}")
        self.turn += 1
        self.current_player = 1 - self.current_player

    @property
    def winning_player(self):
        return self.current_player


if __name__ == '__main__':
    chess = Chess()

    chess.run()

