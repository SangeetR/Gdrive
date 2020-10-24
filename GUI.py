import sys
from PySide2.QtWidgets import *
from PySide2.QtGui     import *
from PySide2.QtCore    import QSize
from db                import Data

# d = Data()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 700, 600)
        self.setWindowTitle("Google Drive Downloader")
        self.ui()

    def ui(self):
        #define 
        vbox_main = QVBoxLayout()
        hbox_upper = QHBoxLayout()
        # add 
        add_vbox = QVBoxLayout()
        add_h_up = QHBoxLayout()
        add_h_down = QHBoxLayout()
        self.url = QLineEdit(self)
        location = QLineEdit()
        start_download_button = QPushButton("Download")
        browse_button = QPushButton("Browse")
        self.group_add = QGroupBox()
        #adding group here to avoid mess
        self.group_add.setLayout(add_vbox)
        add_vbox.addLayout(add_h_up)
        add_vbox.addLayout(add_h_down)
        add_h_up.addWidget(self.url)
        add_h_up.addWidget(start_download_button)
        add_h_down.addWidget(location)
        add_h_down.addWidget(browse_button)
        #everything else
        add_button = QPushButton("Add")
        option_button = QPushButton("Option") 
        scroll = QScrollArea()
        # file_widget = self.file_group_func()        ##################################################
        self.head_label = QLabel("Here i am ")

        # Properties
        self.group_add.setHidden(True)
        self.url.setPlaceholderText("Click Download to paste easily")
        #connect
        browse_button.clicked.connect(self.browse)
        add_button.clicked.connect(self.add_func)
        start_download_button.clicked.connect(self.download_func)
        

        # Wireframe
        self.setLayout(vbox_main)
        vbox_main.addLayout(hbox_upper)
        vbox_main.addWidget(scroll)
        hbox_upper.addWidget(add_button)
        hbox_upper.addWidget(self.head_label)
        hbox_upper.addWidget(self.group_add)
        hbox_upper.addWidget(option_button)
        # Wirframe of add download 


        self.show()

    def browse(self):
        save_file_location = QFileDialog.getSaveFileName(self,"Where i should save this file ....")
        print(save_file_location)

    def add_func(self):
        self.head_label.setHidden(True)
        self.group_add.setHidden(False)
        
    def download_func(self):
        if self.url.text() == '':
            self.url.paste()
        else:
            self.group_add.setHidden(True)
            self.head_label.setHidden(False)

    def file_group_func(self,file_name,filesize,d_size=0):
        pass


def main():
    App = QApplication(sys.argv)
    main_page = MainWindow()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()

# last stored location 
# settings 