import sys
from PySide2.QtWidgets import *
from PySide2.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("Qtool button")

        self.tool = QToolButton(self)
        # tool.popupMode(QToolButton.InstantPopup)
        self.menu = QMenu()
        self.action = QAction("action ")
        self.action.triggered.connect(self.act)
        self.menu.addAction(self.action)
        self.tool.setMenu(self.menu)
        self.tool.clicked.connect(self.sh)

        self.show()
        self.tool.showMenu()

    def sh(self):
        self.tool.showMenu()

    def act(self):
        print("action")

App = QApplication(sys.argv)
main = MainWindow()
sys.exit(App.exec_())






























# from file_info import FileHistory

# ob = FileHistory()
# # od = FileHistory()
# ob.addfile('test1', '1', 'sadlf', 'folder')
# ob.addfile('test2', '2', 'sdf')
# # ob.clearHistory()
# ob.addfile('test3', '3', 'sd')
# print(ob.getfile())

'''
url = ''

r = requests.head(url)
leng =int(r.headers['content-length'])
print(r.headers)
f = open('panjeban.mp4','ab')
start = 0   
done = False
while done is False:
    end = start + 512*1024
    if end > leng:
        if end == leng:
            print("Completed")
            done = True
            break
        end = leng   
        done = True
    print("start:",start,"-",end)
    head = {"Range": "bytes={}-{}".format(start, end)}
    f.write(requests.get(url, headers=head).content)
    print("Downloaded: ",end/leng*100,'\t')
    start = end+1

f.close()
# 53f4b47352be492e8e2836a273492567
# 'Content-Length': '55095924'

'''
