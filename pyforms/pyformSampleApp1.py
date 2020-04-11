from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from pyforms.controls import ControlMatplotlib
import pyforms


class SimpleExample1(BaseWidget):
    def __init__(self):
        super(SimpleExample1, self).__init__('Simple example 1')

        self._firstname = ControlText('First name', 'Devenra Prasad')
        self._testcontrol = ControlText('Test control')
        self._middlename = ControlText('Middle name')
        self._lastname = ControlText('Lastname name')
        self._fullname = ControlText('Full name')
        self._button = ControlButton('Click')
        self._graph = ControlMatplotlib('Graph')

        # self.formset = ['_firstname','_middlename','_lastname', '_fullname', '_button', ' ']
        self.formset = [ {
            'Tab1':['_firstname','||','_middlename','||','_lastname'],
            'Tab2': ['_fullname']
        },
            '=',(' ','_button', ' ') ]

        submenu = self._fullname.add_popup_submenu('Path')
        self._fullname.add_popup_menu_option('Delete', function_action=self.__dummyEvent, submenu=submenu)
        self._fullname.add_popup_menu_option('Edit', function_action=self.__dummyEvent, submenu=submenu)
        self._fullname.add_popup_menu_option('Interpolate', function_action=self.__dummyEvent, submenu=submenu)

        #Define the window main menu using the property main menu
        self.mainmenu = [
            { 'File': [
                {'Open': self.__dummyEvent},
                '-',
                {'Save': self.__dummyEvent},
                {'Save as': self.__dummyEvent}
            ]
            },
            { 'Edit': [
                {'Copy': self.__dummyEvent},
                {'Past': self.__dummyEvent}
            ]
            }
        ]

        self._button.value = self.__buttonAction
        self._graph.value = self.__on_draw

    def __dummyEvent(self):
        print ("Menu option selected")

    def __on_draw(self, figure):
        data = [1, 2, 1, 4]
        x = range(len(data))
        axes = figure.add_subplot(111)
        axes.bar(left=x, height=data)
        axes = figure.add_subplot(222, projection='3d')
        pts = axes.scatter(x, data, data, c=x)
        figure.colorbar(pts)

    def __buttonAction(self):
        self._fullname.value = self._testcontrol.value + " -> " + self._firstname.value + " " + self._middlename.value + " " + self._lastname.value


if __name__ == "__main__":     pyforms.start_app(SimpleExample1)
