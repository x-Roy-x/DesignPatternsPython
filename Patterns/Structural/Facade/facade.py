

class Buffer:

    def __init__(self, width=2, height=2):
        self.width = width
        self.height = height
        self.buffer = [" "] * (width * height)

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text


class ViewPort:

    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[index + self.offset]

    def apppend(self, text):
        self.buffer.write(text)


class ConsoleFacade:

    def __init__(self):
        b = Buffer()
        self.current_view_port = ViewPort(b)
        self.buffers = [b]
        self.view_ports = [self.current_view_port]

    def write(self, text):
        self.current_view_port.buffer.write(text)

    def get_char_at(self, index):
        return self.current_view_port.get_char_at(index)


if __name__ == '__main__':
    console = ConsoleFacade()

    console.write("Hello")
    char = console.get_char_at(0)
    print(char)

