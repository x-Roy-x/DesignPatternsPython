import abc
from enum import Enum, auto


class ListStrategy(abc.ABC):

    def start(self, buffer):
        pass

    def end(self, buffer):
        pass

    def add_list_item(self, buffer, item):
        pass


class MarkdownListStrategy(ListStrategy):

    def add_list_item(self, buffer, item):
        buffer.append(f"* {item}\n")


class HtmlListStrategy(ListStrategy):

    def start(self, buffer):
        buffer.append(f"<ul>\n")

    def end(self, buffer):
        buffer.append(f"</ul>\n")

    def add_list_item(self, buffer, item):
        buffer.append(f"\t<li>{item}</li>\n")


class OutputFormat(Enum):

    MARKDOWN = auto()
    HTML = auto()


class TextProcessor:

    def __init__(self, list_strategy=HtmlListStrategy()):
        self.list_strategy = list_strategy
        self.buffer = []

    def append_list(self, items):
        ls = self.list_strategy
        ls.start(self.buffer)

        for item in items:
            ls.add_list_item(self.buffer, item)

        ls.end(self.buffer)

    def set_output_format(self, output_format):
        if output_format == OutputFormat.HTML:
            self.list_strategy = HtmlListStrategy()
        elif output_format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return "".join(self.buffer)


if __name__ == '__main__':

    items = ["foo", "bar", "baz"]

    tp = TextProcessor()

    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list(items)
    print(tp)

    tp.clear()

    tp.set_output_format(OutputFormat.HTML)
    tp.append_list(items)
    print(tp)

