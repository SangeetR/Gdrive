import sys
from PySide2.QtWidgets import *
import time

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(300, 300, 500,500)
        self.setWindowTitle("AnyThing You Want")
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        self.prog_bar = QProgressBar()
        self.button = QPushButton("Start")
        exi_t  = QPushButton("exit")
        self.button.clicked.connect(self.button_listner)
        self.button.setCheckable(True)
        exi_t.clicked.connect(self.exi_t)
        
        vbox.addWidget(self.button)
        vbox.addWidget(self.prog_bar)
        vbox.addWidget(exi_t)
        self.setLayout(vbox)

        self.show()

    def button_listner(self):
        if self.button.isChecked():
            self.start()
        else:
            self.prog_bar.setValue(0) 
    def start(self):
        val =0
        while val != 100:
            self.prog_bar.setValue(val)
            time.sleep(0.3)
            val +=1 
            QApplication.processEvents()

    def exi_t(self):
        sys.exit()


def main():
    App = QApplication(sys.argv)
    ob = MainWindow()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()