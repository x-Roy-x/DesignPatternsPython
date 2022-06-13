import abc


class Machine:

    @abc.abstractmethod
    def print(self, document):
        pass

    @abc.abstractmethod
    def fax(self, document):
        pass

    @abc.abstractmethod
    def scan(self, document):
        pass


class MultiFunctionPrinter(Machine):

    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldPrinter(Machine):

    def print(self, document):
        #ok
        pass

    def fax(self, document):
        raise NotImplementedError("Printer can`t fax")

    def scan(self, document):
        raise NotImplementedError("Printer can`t scan")


# Better use separate interface
class Printer:

    @abc.abstractmethod
    def print(self, document):
        pass


class Scaner:

    @abc.abstractmethod
    def scan(self, document):
        pass


class MultiFunctionDevice:

    @abc.abstractmethod
    def print(self, document):
        pass

    @abc.abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):

    def print(self, document):
        pass


class PhotoCopier(MultiFunctionDevice):

    def print(self, document):
        pass

    def scan(self, document):
        pass




