
class FormattedText:

    def __init__(self, plain_text):
        self.plain_text = plain_text

        self.caps = [False] * len(self.plain_text)

    def capitalize(self, start, end):
        for i in range(start, end):
            self.caps[i] = True

    def __str__(self):
        result = []

        for i in range(len(self.plain_text)):
            letter = self.plain_text[i]
            letter = letter.upper() if self.caps[i] else letter

            result.append(letter)

        return "".join(result)


class BetterFormattedText:

    def __init__(self, plaint_text):
        self.plaint_text = plaint_text
        self.formatting = []

    def get_range(self, start, end):
        r = self.TextRange(start, end)
        self.formatting.append(r)

        return r

    def __str__(self):
        result = []

        for i in range(len(self.plaint_text)):
            character = self.plaint_text[i]
            for r in self.formatting:
                if r.covers(i) and r.capitalize:
                    character = character.upper()

            result.append(character)

        return "".join(result)

    class TextRange:
        
        def __init__(self, start, end, capitalize=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        def covers(self, position):
            return self.start <= position <= self.end


if __name__ == '__main__':
    text = "This is a brave new world"
    ft = FormattedText(text)
    ft.capitalize(10, 15)
    print(ft)

    btf = BetterFormattedText(text)
    btf.get_range(16, 19).capitalize = True
    print(btf)