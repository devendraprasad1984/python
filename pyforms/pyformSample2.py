# https://github.com/UmSenhorQualquer/pyforms/blob/master/tutorials/2.ControlsExamples/Example2.py
# https://pyforms.readthedocs.io/en/latest/getting-started/style-layout/
import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlBoundingSlider
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from pyforms.controls import ControlCheckBox
from pyforms.controls import ControlCheckBoxList
from pyforms.controls import ControlCombo
from pyforms.controls import ControlDir
from pyforms.controls import ControlDockWidget
from pyforms.controls import ControlEmptyWidget
from pyforms.controls import ControlFile
from pyforms.controls import ControlFilesTree
from pyforms.controls import ControlImage
from pyforms.controls import ControlList
from pyforms.controls import ControlPlayer
from pyforms.controls import ControlProgress
from pyforms.controls import ControlSlider
from pyforms.controls import ControlVisVis
from pyforms.controls import ControlVisVisVolume
from pyforms.controls import ControlEventTimeline
from pyforms.controls import ControlCodeEditor
import numpy as np
import random


class Example1(BaseWidget):
    def __init__(self):
        super(Example1, self).__init__('dir examples')
        self.parent = None
        self._directory = ControlDir('Choose a directory')
        self._file = ControlFile('Choose a file')
        self._filetree = ControlFilesTree('Choose a file')
        self._image = ControlImage('Image')
        self._boundaries = ControlBoundingSlider('Bounding', horizontal=True)
        self._button = ControlButton('Click')

        self._button.value = self.onButtonClick
        # self._directory.value=self.onButtonClick

        self._checkbox = ControlCheckBox('Choose a directory')
        self._checkboxList = ControlCheckBoxList('Choose a file')
        self._player = ControlPlayer('Choose a file')
        self._slider = ControlSlider('Slider')
        self._player.show()
        self._checkboxList.value = [('Item 1', True), ('Item 2', False), ('Item 3', True)]

        self._combobox = ControlCombo('Choose a item')
        self._list = ControlList('List label')
        self._progress = ControlProgress('Progress bar')
        self._visvisVolume = ControlVisVisVolume('Visvis')
        self._timeline = ControlEventTimeline('Timeline')

        self._combobox.add_item('Item 1', 'Value 1')
        self._combobox.add_item('Item 2', 'Value 2')
        self._combobox.add_item('Item 3', 'Value 3')
        self._combobox.add_item('Item 4')

        self._list.value = [('Item1', 'Item2', 'Item3',), ('Item3', 'Item4', 'Item5',)]
        imageWithVolume = np.zeros((100, 100, 100), np.uint8)
        imageWithVolume[30:40, 30:50, :] = 255
        imageWithVolume[30:40, 70:72, :] = 255
        self._visvisVolume.value = imageWithVolume

        self._visvis = ControlVisVis('Visvis')
        values1 = [(i, random.random(), random.random()) for i in range(130)]
        values2 = [(i, random.random(), random.random()) for i in range(130)]
        self._visvis.value = [values1, values2]

        self.formset = [
            '_visvis'
            , '_directory'
            , '_button'
            , '_file'
            , '_boundaries'
            , '_filetree'
            , '_image'
            , '_slider'
            , ('_checkboxList', '_player')
            , ('_checkbox', ' ')
            , ('_combobox', ' ')
            , '_progress'
            , '='
            , ('_visvisVolume', '||', '_list')
            , '_timeline'
        ]

    def onButtonClick(self):
        self._filetree.value = self._directory.value


if __name__ == "__main__":
    pyforms.start_app(Example1)
