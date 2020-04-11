import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlDockWidget
from pyforms.controls import ControlList

from python.pyforms.personWindow import PersonWindow
from . import AddMenuFuntionality
from . import People


class PeopleWindow(AddMenuFuntionality, People, BaseWidget):
    def __init__(self):
        People.__init__(self)
        BaseWidget.__init__(self, 'People window')
        AddMenuFuntionality.__init__(self)
        self._panel = ControlDockWidget()
        self._peopleList = ControlList('People',
                                       add_function=self.__addPersonBtnAction,
                                       remove_function=self.__rmPersonBtnAction)
        self._peopleList.horizontalHeaders = ['First name', 'Middle name', 'Last name']

    def closeEvent(self, event):
        print("called on close")

    def initForm(self):
        super(PeopleWindow, self).initForm()

        self.mainmenu[0]['File'][0]['Save as'].setEnabled(False)

    def addPerson(self, person):
        super(PeopleWindow, self).addPerson(person)
        self._peopleList += [person._firstName, person._middleName, person._lastName]
        person.close()

    def removePerson(self, index):
        super(PeopleWindow, self).removePerson(index)
        self._peopleList -= index

    def __addPersonBtnAction(self):
        win = PersonWindow()
        win.parent = self
        self._panel.value = win

    def __rmPersonBtnAction(self):
        self.removePerson(self._peopleList.selected_row_index)


if __name__ == "__main__":     pyforms.start_app(PeopleWindow)
