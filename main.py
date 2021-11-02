import sys
from panel import *
from qtpy import QtWidgets, QtGui, QtCore
from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)



class MainWindow(QtWidgets.QMainWindow):
    __currentTab = 0
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("I/F Panel Creator")






        self.connect()

    def currentRange(self):
        if self.ui.cbARrange.currentText() == "1A":
            self.ui.name1.setPlainText(iFpanel.lbl_name1Aup.text())
            self.ui.name2.setPlainText(iFpanel.lbl_name1Amid.text())
            self.ui.name3.setPlainText(iFpanel.lbl_name1Adw.text())
        elif self.ui.cbARrange.currentText() == "1B":
            self.ui.name1.setPlainText(iFpanel.lbl_name1Bup.text())
            self.ui.name2.setPlainText(iFpanel.lbl_name1Bmid.text())
            self.ui.name3.setPlainText(iFpanel.lbl_name1Bdw.text())
        elif self.ui.cbARrange.currentText() == "1C":
            pass
        elif self.ui.cbARrange.currentText() == "1D":
            pass
        elif self.ui.cbARrange.currentText() == "1E":
            pass
        elif self.ui.cbARrange.currentText() == "1F":
            pass
        elif self.ui.cbARrange.currentText() == "1G":
            pass
        elif self.ui.cbARrange.currentText() == "1H":
            pass


    def currentTab(self, tab):
        self.__currentTab = tab
        tabTxt = self.ui.tabWidget.tabText(tab)
        self.ui.groupName.setPlainText(tabTxt)

    def changeGroupName(self):
        self.ui.tabWidget.setTabText(self.__currentTab, self.ui.groupName.toPlainText())

    def changeName1(self):
        if self.ui.cbARrange.currentText() == "1A":
            iFpanel.lbl_name1Aup.setText(self.ui.name1.toPlainText())
        elif self.ui.cbARrange.currentText() == "1B":
            iFpanel.lbl_name1Bup.setText(self.ui.name1.toPlainText())
        elif self.ui.cbARrange.currentText() == "1C":
            pass
        elif self.ui.cbARrange.currentText() == "1D":
            pass
        elif self.ui.cbARrange.currentText() == "1E":
            pass
        elif self.ui.cbARrange.currentText() == "1F":
            pass
        elif self.ui.cbARrange.currentText() == "1G":
            pass
        elif self.ui.cbARrange.currentText() == "1H":
            pass


    def changeName2(self):
        if self.ui.cbARrange.currentText() == "1A":
            iFpanel.lbl_name1Amid.setText(self.ui.name2.toPlainText())
        elif self.ui.cbARrange.currentText() == "1B":
            iFpanel.lbl_name1Bmid.setText(self.ui.name2.toPlainText())
        elif self.ui.cbARrange.currentText() == "1C":
            pass
        elif self.ui.cbARrange.currentText() == "1D":
            pass
        elif self.ui.cbARrange.currentText() == "1E":
            pass
        elif self.ui.cbARrange.currentText() == "1F":
            pass
        elif self.ui.cbARrange.currentText() == "1G":
            pass
        elif self.ui.cbARrange.currentText() == "1H":
            pass

    def changeName3(self):
        if self.ui.cbARrange.currentText() == "1A":
            iFpanel.lbl_name1Adw.setText(self.ui.name3.toPlainText())
        elif self.ui.cbARrange.currentText() == "1B":
            iFpanel.lbl_name1Bdw.setText(self.ui.name3.toPlainText())
        elif self.ui.cbARrange.currentText() == "1C":
            pass
        elif self.ui.cbARrange.currentText() == "1D":
            pass
        elif self.ui.cbARrange.currentText() == "1E":
            pass
        elif self.ui.cbARrange.currentText() == "1F":
            pass
        elif self.ui.cbARrange.currentText() == "1G":
            pass
        elif self.ui.cbARrange.currentText() == "1H":
            pass


    def on_button_click(self):
        print("test")
        sys.exit(app.exec())

    def on_button_clickSave(self):
        print(self.ui.input.text())
        window.ui.lbl1.setStyleSheet("QLabel { background-color : blue;}")

    def on_label_clickSave(self):
        print("Click label")

    def getfile(self):
        eeg_cap_dir = QtCore.QDir.currentPath()
        dialog = QtWidgets.QFileDialog(self)
        dialog.setWindowTitle('Open EEG Position file')
        dialog.setNameFilter('(*.*)')
        dialog.setDirectory(eeg_cap_dir)
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        filename = None
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            filename = dialog.selectedFiles()
        if filename:
            self.fname = str(filename[0])
            print(self.fname)

    def connect(self):
        self.ui.tabWidget.tabBarClicked.connect(self.currentTab)
        self.ui.groupName.textChanged.connect(self.changeGroupName)
        self.ui.cbARrange.currentTextChanged.connect(self.currentRange)
        self.ui.name1.textChanged.connect(self.changeName1)
        self.ui.name2.textChanged.connect(self.changeName2)
        self.ui.name3.textChanged.connect(self.changeName3)
        self.ui.actionLoad.triggered.connect(self.getfile)

        #self.ui.btn1.clicked.connect(self.on_button_click)
        #self.ui.btnSave.clicked.connect(self.on_button_clickSave)

    def setUpPanel(self, lbl_type, up, mid, dw, x, y):
        lbl_type.setPixmap(QtGui.QPixmap("UI/untitled/pic/Circle.png"))
        lbl_type.setStyleSheet("QLabel { background-color : blue;}")
        lbl_type.setGeometry(x, y, 100, 100)

        up.setGeometry(QtCore.QRect(0+x, 1+y, 100, 10))
        up.setText("test up")
        up.setAlignment(QtCore.Qt.AlignCenter)

        mid.setGeometry(QtCore.QRect(0+x, 10+y, 100, 10))
        mid.setText("test middle")
        mid.setAlignment(QtCore.Qt.AlignCenter)

        dw.setGeometry(QtCore.QRect(0+x, 20+y, 100, 10))
        dw.setText("test down")
        dw.setAlignment(QtCore.Qt.AlignCenter)






class testClass( ):
    def __init__(self, dest):
        self.dest = dest
        self.lbl_name4Gdw = QtWidgets.QLabel(dest)


        self.setText("init")

    def setText(self, txt):
        self.lbl_name4Gdw.setGeometry(QtCore.QRect(100, 10, 100, 10))
        self.lbl_name4Gdw.setText(txt)
        self.lbl_name4Gdw.setAlignment(QtCore.Qt.AlignCenter)


window = MainWindow()
iFpanel = Panel(window.ui.tab_1)
iFpanel1 = Panel(window.ui.tab_2)



#test1 = testClass(window.ui.tab)
#test2 = testClass(window.ui.tab_2)

#test1.setText("tabulator 1")
#test2.setText("tabulator 2")

iFpanel.setText("Tab1", "Tab1", "Tab1", "1A")
iFpanel1.setText("Tab2", "Tab2", "Tab22", "1A")
#iFpanel.lbl_name1Aup.setText("Hallo")

#iFpanel.setTextUp("Hallo Michael", 1)

#window.ui.lbl_type1A.setPixmap(QtGui.QPixmap("UI/untitled/pic/Circle.png"))
#window.ui.lbl_type1A.setStyleSheet("QLabel { background-color : red;}")



window.show()


sys.exit(app.exec())
