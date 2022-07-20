from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import requests
import time
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainui = QtWidgets.QLabel(self.centralwidget)
        self.mainui.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.mainui.setText("")
        self.mainui.setPixmap(QtGui.QPixmap("../Weather Now.gif"))
        self.movie = QMovie("../Weather Now.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.mainui.setObjectName("mainui")
        self.Outputbox = QtWidgets.QFrame(self.centralwidget)
        self.Outputbox.setGeometry(QtCore.QRect(300, 230, 501, 271))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        self.Outputbox.setFont(font)
        self.Outputbox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Outputbox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Outputbox.setObjectName("Outputbox")
        self.Outputbox.connect(self.find_weather())
        self.Outputbox.show(self.find_weather())

        self.Outputbox.show(self.find_weather())
        self.calendarwd = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarwd.setGeometry(QtCore.QRect(930, 510, 341, 201))
        self.calendarwd.setObjectName("calendarwd")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(630, 160, 101, 41))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(10)
        self.search.setFont(font)
        self.search.setObjectName("search")
        self.search.clicked.connect(self.find_weather)
        self.cityinput = QtWidgets.QLineEdit(self.centralwidget)
        self.cityinput.setGeometry(QtCore.QRect(320, 160, 291, 41))
        self.cityinput.setObjectName("cityinput")
        self.cityinput.text(self.find_weather())
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def find_weather(self):
        city=self.cityinput
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=48b1e85d2f6587f009a9ffee21ef7f2b"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        final_info = condition + "\n" + str(temp) + "°C"
        final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(
            max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
            humidity) + "\n" + "Wind Speed: " + str(wind) + "\n"



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search.setText(_translate("MainWindow", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
