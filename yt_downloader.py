from pytube import YouTube
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import qdarkstyle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Youtube Video Downloader")
        self.setWindowIcon(QtGui.QIcon('image.jpg'))
        self.setGeometry(200, 200, 400, 150)

        # Number of Thread
        self.urllabel = QLabel(self)
        self.urllabel.setText('Video URL')
        self.urlbox = QLineEdit(self)
        self.urlbox.setPlaceholderText('URL of video')

        self.urlbox.move(100, 20)
        self.urlbox.resize(200, 30)
        self.urllabel.move(20, 20)

        self.getbutton = QPushButton('Get', self)
        self.getbutton.move(300, 20)
        self.getbutton.resize(40, 30)
        self.getbutton.clicked.connect(self.getdata)

        self.reslabel = QLabel(self)
        self.reslabel.setText('Resolution')
        self.resbox = QComboBox(self)

        self.resbox.move(150, 50)
        self.resbox.resize(80, 30)
        self.reslabel.move(20, 50)

        self.dowbutton = QPushButton('Download', self)
        self.dowbutton.move(100, 80)
        self.dowbutton.resize(200, 30)
        self.dowbutton.clicked.connect(self.download)

        self.titlelabel = QLabel(self)
        # self.titlelabel.setStyleSheet("background-color: lightgreen")
        self.titlelabel.move(100, 110)
        self.titlelabel.resize(500, 30)
    
    def getdata(self):
        yt_adress = self.urlbox.text()
        yt = YouTube(yt_adress)
        print(yt.title)
        res_set = set()
        
        for i in yt.streams.filter(progressive = True, file_extension = "mp4"): 
            if i.resolution != None:
                res_set.add(i.resolution)

        res_list = list(res_set)
        res_list = sorted(res_list, key=lambda x: int(x.split('p')[0]), reverse=False)
        print(res_list)

        self.resbox.addItems(res_list)
        self.titlelabel.setText(yt.title)
    
    def download(self):
        yt_input = self.urlbox.text()
        res_input = self.resbox.currentText()
        print(yt_input)
        print(res_input)
        YouTube(yt_input).streams.filter(res=res_input).first().download()


        



app = QApplication([])
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
window = MainWindow()
window.show()
app.exec()





# https://www.youtube.com/watch?v=8GhKoyWY6fY