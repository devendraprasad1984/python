from . import BaseWindow


class MainWindow(BaseWindow):
    def __init__(self):
        super(MainWindow, self).__init__()


# self.loadWindowData('teste.txt')


if __name__ == "__main__":
    import pyforms

    pyforms.start_app(MainWindow)
