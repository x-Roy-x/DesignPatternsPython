class Journal:

    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text) -> None:
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, position) -> None:
        del self.entries[position]

    def __str__(self) -> str:
        return '\n'.join(self.entries)

    # Second responsibility
    """
    def save_file(self, file_name: str) -> None:
        with open(file_name) as file:
            file.write(str(self))
    """


class PersistenceManager:

    @staticmethod
    def save_file(journal, file_name: str) -> None:
        file = open(file_name, "w")
        file.write(str(journal))
        file.close()
