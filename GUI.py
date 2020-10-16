import sys
from PySide2.QtWidgets import *
# from PySide2.QtGui import *
import auth 
# from threading import Thread


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 150)
        self.setWindowTitle("Gdrive Download Manager")
        self.UI()
    
    def UI(self):
        #Define Widgets
        vbox = QVBoxLayout()
        upHbox = QHBoxLayout()
        add_download = QPushButton("Add Download")
        option_tool = QPushButton("Options")
        list_downloads = QListWidget()
        self.check_clipboard = QPushButton("Check Clipboard")
        exit_button = QPushButton("Exit")

        #Add to correct layout
        upHbox.addWidget(add_download)
        upHbox.addStretch()
        upHbox.addWidget(option_tool)
        vbox.addLayout(upHbox)
        vbox.addWidget(list_downloads)
        vbox.addStretch()
        vbox.addWidget(self.check_clipboard)
        vbox.addWidget(exit_button)
        vbox.addStretch()

        #connect to function
        exit_button.clicked.connect(self.exit_func)
        # self.check_clipboard.clicked.connect(self.driver)

        # style1 = QStyle.
        self.setLayout(vbox)
        sty = QStyleFactory.create('Fusion')
        self.setStyle(sty)
        # self.setPalette()
        # self.setStyle()
        self.show()

    def exit_func(self):
        sys.exit()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()