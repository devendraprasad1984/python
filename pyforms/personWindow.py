from pyforms.utils.settings_manager import conf;
from . import settings;
conf += settings

from . import Person

import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton


class PersonWindow(Person, BaseWidget):
    def __init__(self):
        Person.__init__(self, '', '', '')
        BaseWidget.__init__(self, 'Person window')
        self.parent = None

        # Definition of the forms fields
        self._firstnameField = ControlText('First name')
        self._middlenameField = ControlText('Middle name')
        self._lastnameField = ControlText('Lastname name')
        self._fullnameField = ControlText('Full name')
        self._buttonField = ControlButton('Press this button')

        # Define the button action
        self._buttonField.value = self.buttonAction

        self.formset = ['_firstnameField', '_middlenameField', '_lastnameField',
                        '_fullnameField',
                        (' ', '_buttonField', ' '), ' ']

    def buttonAction(self):
        self._firstName = self._firstnameField.value
        self._middleName = self._middlenameField.value
        self._lastName = self._lastnameField.value
        self._fullnameField.value = self.fullName

        # In case the window has a parent
        if self.parent != None: self.parent.addPerson(self)

    def printFullName(self):
        print(self._fullnameField.value)

if __name__ == "__main__":     pyforms.start_app(PersonWindow)
