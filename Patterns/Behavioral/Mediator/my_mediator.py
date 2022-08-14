import abc
from abc import ABC


class Mediator(ABC):

    @abc.abstractmethod
    def notify(self, sender, event):
        pass


class UIMediator(Mediator):

    def __init__(self, component1, component2):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender, event):
        if isinstance(sender, ButtonAlert) and event == "click_button":
            self._component2.show_text("Alert")



class BaseComponent:

    def __init__(self):
        self._mediator = None

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator


class Button(BaseComponent):

    def click_button(self):
        self.mediator.notify(self, "click_button")


class ButtonAlert(Button):

    def __init__(self):
        super().__init__()


class Field(BaseComponent):

    def show_text(self, text):
        print(text)


if __name__ == '__main__':
    component1 = ButtonAlert()
    component2 = Field()

    UIMediator(component1, component2)

    component1.click_button()

