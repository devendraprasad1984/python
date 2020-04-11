from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton


class SimpleExample1(BaseWidget):

    def __init__(self):
        super(SimpleExample1, self).__init__('Simple example 1')
        self._firstname = ControlText('First name', 'Default value')
        self._middlename = ControlText('Middle name')
        self._lastname = ControlText('Lastname name')
        self._fullname = ControlText('Full name')
        self._button = ControlButton('Press this button')

        self._button.value = self.__buttonAction

    def __buttonAction(self):
        self._fullname.value = self._firstname.value + " " + self._middlename.value + \
                               " " + self._lastname.value


if __name__ == "__main__":
    import pyforms

    pyforms.start_app(SimpleExample1)
