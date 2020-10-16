import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import QSize
import auth
import os                                                  #TODO PySide2 Signals learn haan theek h jo bhi h satynaash
import time

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("Gdrive Download Manager")
        self.UI()
    
    def UI(self):
        #Define Widgets
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        downVbox = QVBoxLayout()
        plus_button = QPushButton()
        plus_button.setIcon(QIcon('icon/add-file.png'))
        plus_button.setIconSize(QSize(50, 50))
        plus_button.setFixedSize(70,70)
        hr_line = QFrame()
        hr_line.setFrameShape(QFrame.HLine)
        hr_line.setFrameShadow(QFrame.Sunken)
        self.lab1 = QLabel("Download 1")
        self.barr = QProgressBar()
        self.barr.setFixedHeight(20)
        self.group_box1 = QGroupBox()
        self.status = QLabel("Status:")
        self.service = None

        try:
            self.service = auth.gauth()
            self.status.setText("Status: Authorized")
        except :
            self.status.setText("Status: Unauthorized")
            


        #Windows Color Decision
        default_palette = QPalette()
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(200,10,20))
        dark_palette.setColor(QPalette.ButtonText, QColor(0,0,0))
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)
        plus_button.setStyleSheet("""
        background-color: rgb(100,150,250);
        border: none;
        """)
        self.barr.setStyleSheet("""
            QProgressBar::chunk{
                background-color: rgb(100,150,250);
            }
        """)
        self.status.setStyleSheet("""
        background-color: rgb(50,100,255);
        """)
        font_hel = QFont("Helvetica",14)
        self.status.setFont(font_hel)

        #Add to Layout 
        vbox.addLayout(hbox)
        hbox.addWidget(plus_button)
        hbox.addWidget(self.status)
        # hbox.addStretch()
        vbox.addWidget(hr_line)
        # vbox.addLayout(downVbox)
        downVbox.addWidget(self.lab1)
        downVbox.addWidget(self.barr)
        downVbox.addStretch()
        self.group_box1.setLayout(downVbox)
        self.group_box1.setMaximumHeight(80)
        vbox.addWidget(self.group_box1)
        vbox.addStretch()

        #connect to function
        plus_button.clicked.connect(self.dwn)

        #final manage
        sty = QStyleFactory.create('Fusion')
        self.setStyle(sty)
        plus_button.setPalette(dark_palette)
        self.setPalette(dark_palette)
        self.setLayout(vbox)
        self.group_box1.setHidden(True)
        self.show()        
    
    def dwn(self):
        self.group_box1.setHidden(False)
        self.status.setText("Status: Downloading.....")
        id = auth.get_id()
        if id is None:
            self.status.setText("Status: Error-Link")
        req = self.service.files().get(fileId = str(id), fields = 'name, size, md5Checksum' ).execute()
        self.lab1.setText(str(req['name']))
        print("Hash: ", req['md5Checksum'])
        print("File Size: ",(int(req['size'])/1024)/1024,"MB")
        f = open(os.path.join('Download', req['name']), 'ab')
        request = self.service.files().get_media(fileId=id)
        start = os.path.getsize(os.path.join('Download',req['name']))
        if start == req['size']:
            self.status.setText("Status: Error-file is downloaded already")
            f.close()

        done = False
        while done is False:
            QApplication.processEvents()
            end = start+1024*64
            if end > int(req['size']):
                end = int(req['size'])

                done = True
            request.headers['Range'] = "bytes="+str(start)+"-"+str(end)
            f.write(request.execute())
            start = end+1
            val = round((int(end)/int(req['size']))*100)
            print(val)
            self.barr.setValue(val)
        f.close()
        self.status.setText("Status: Authorized")

    def checkEve(self):
        QApplication.processEvents()

        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
    

if __name__ == "__main__":
    main()