import sys
from PySide2.QtWidgets import *
import auth 
from threading import Thread


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 150)
        self.setWindowTitle("Gdrive Download Manager")
        self.UI()
    
    def UI(self):
        #Define Widgets
        vbox = QVBoxLayout()
        self.check_clipboard = QPushButton("Check Clipboard")
        exit_button = QPushButton("Exit")

        #Add to correct layout
        vbox.addStretch()
        vbox.addWidget(self.check_clipboard)
        vbox.addWidget(exit_button)
        vbox.addStretch()

        #connect to function
        exit_button.clicked.connect(self.exit_func)
        self.check_clipboard.clicked.connect(self.driver)

        self.setLayout(vbox)
        self.show()

    def exit_func(self):
        sys.exit()

    def driver(self):
        self.check_clipboard.setHidden(True)
        self.check_clipboard.setDisabled(True)
        t = Thread(target=self.down, args=())
        t.start()
        # self.close()
    
    def down(self):
        service = auth.gauth()
        id = auth.get_id()
        auth.dwnld(service, id)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()