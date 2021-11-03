import sys
from panel import *
from readPanel import *
from qtpy import QtWidgets, QtGui, QtCore
from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):
    __currentTab = 0
    iFpanel = []  # List of all Pannels
    p = {}  # dictionary of Panels

    def __init__(self, parent=None):
        super().__init__(parent)
        self.fname = "FilePath"
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("I/F Panel Creator")

        self.connect()

    def currentTab(self, tab):
        self.__currentTab = tab
        tabTxt = self.ui.tabWidget.tabText(tab)
        self.ui.groupName.setPlainText(tabTxt)

        # RECONNECT WHEN TAB CHANGED
        self.ui.name1.textChanged.connect(self.iFpanel[self.__currentTab].changeName1)
        self.ui.name1.textChanged.disconnect()  # this disconnect all
        self.ui.name1.textChanged.connect(self.iFpanel[self.__currentTab].changeName1)

        self.ui.name2.textChanged.connect(self.iFpanel[self.__currentTab].changeName2)
        self.ui.name2.textChanged.disconnect()  # this disconnect all
        self.ui.name2.textChanged.connect(self.iFpanel[self.__currentTab].changeName2)

        self.ui.name3.textChanged.connect(self.iFpanel[self.__currentTab].changeName3)
        self.ui.name3.textChanged.disconnect()  # this disconnect all
        self.ui.name3.textChanged.connect(self.iFpanel[self.__currentTab].changeName3)

        self.ui.cbARrange.currentTextChanged.connect(self.iFpanel[self.__currentTab].currentRange)
        self.ui.cbARrange.currentTextChanged.disconnect()  # this disconnect all
        self.ui.cbARrange.currentTextChanged.connect(self.iFpanel[self.__currentTab].currentRange)

        self.iFpanel[self.__currentTab].currentRange()  # update name1,2,3

    def changeGroupName(self):
        self.ui.tabWidget.setTabText(self.__currentTab, self.ui.groupName.toPlainText())

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
            self.p = readFile(self.fname)
            # self.iFpanel[0].setText(self.p[1].panel["1A"][5], self.p[1].panel["1A"][6], self.p[1].panel["1A"][7], "1A")
            for e in PanelDiscripition.elements:
                self.iFpanel[0].setText(self.p[1].panel[e][5], self.p[1].panel[e][6], self.p[1].panel[e][7], e)
                self.iFpanel[1].setText(self.p[2].panel[e][5], self.p[2].panel[e][6], self.p[2].panel[e][7], e)
                self.iFpanel[2].setText(self.p[3].panel[e][5], self.p[3].panel[e][6], self.p[3].panel[e][7], e)
                self.iFpanel[3].setText(self.p[4].panel[e][5], self.p[4].panel[e][6], self.p[4].panel[e][7], e)
                self.iFpanel[4].setText(self.p[5].panel[e][5], self.p[5].panel[e][6], self.p[5].panel[e][7], e)

            #print(self.p[1].panel["NAME"][0])
            self.ui.tabWidget.setTabText(0, self.p[1].panel["NAME"][1])
            self.ui.tabWidget.setTabText(1, self.p[2].panel["NAME"][1])
            self.ui.tabWidget.setTabText(2, self.p[3].panel["NAME"][1])
            self.ui.tabWidget.setTabText(3, self.p[4].panel["NAME"][1])
            self.ui.tabWidget.setTabText(4, self.p[5].panel["NAME"][1])

    def connect(self):
        self.ui.tabWidget.tabBarClicked.connect(self.currentTab)
        self.ui.groupName.textChanged.connect(self.changeGroupName)

        self.ui.actionLoad.triggered.connect(self.getfile)

        # self.ui.btn1.clicked.connect(self.on_button_click)
        # self.ui.btnSave.clicked.connect(self.on_button_clickSave)

    def setUpPanel(self, lbl_type, up, mid, dw, x, y):
        lbl_type.setPixmap(QtGui.QPixmap("UI/untitled/pic/Circle.png"))
        lbl_type.setStyleSheet("QLabel { background-color : blue;}")
        lbl_type.setGeometry(x, y, 100, 100)

        up.setGeometry(QtCore.QRect(0 + x, 1 + y, 100, 10))
        up.setText("test up")
        up.setAlignment(QtCore.Qt.AlignCenter)

        mid.setGeometry(QtCore.QRect(0 + x, 10 + y, 100, 10))
        mid.setText("test middle")
        mid.setAlignment(QtCore.Qt.AlignCenter)

        dw.setGeometry(QtCore.QRect(0 + x, 20 + y, 100, 10))
        dw.setText("test down")
        dw.setAlignment(QtCore.Qt.AlignCenter)


class testClass():
    def __init__(self, dest):
        self.dest = dest
        self.lbl_name4Gdw = QtWidgets.QLabel(dest)

        self.setText("init")

    def setText(self, txt):
        self.lbl_name4Gdw.setGeometry(QtCore.QRect(100, 10, 100, 10))
        self.lbl_name4Gdw.setText(txt)
        self.lbl_name4Gdw.setAlignment(QtCore.Qt.AlignCenter)


window = MainWindow()
iFpanel = Panel(window.ui.tab_1, window)
iFpanel1 = Panel(window.ui.tab_2, window)
iFpanel2 = Panel(window.ui.tab_3, window)
iFpanel3 = Panel(window.ui.tab_4, window)
iFpanel4 = Panel(window.ui.tab_5, window)

# window.iFpanel.append(iFpanel) #add Oject for Connecting, window to current Panel
# window.iFpanel.append(iFpanel1) #add Oject for Connecting, window to current Panel

# test1 = testClass(window.ui.tab)
# test2 = testClass(window.ui.tab_2)

# test1.setText("tabulator 1")
# test2.setText("tabulator 2")

#iFpanel.setText("Tab1", "Tab1", "Tab1", "1A")
#iFpanel1.setText("Tab2", "Tab2", "Tab22", "1A")

# iFpanel.setText(p[1].panel["1A"][5], p[1].panel["1A"][6], p[1].panel["1A"][7], "1A")

# iFpanel.lbl_name1Aup.setText("Hallo")

# iFpanel.setTextUp("Hallo Michael", 1)

# window.ui.lbl_type1A.setPixmap(QtGui.QPixmap("UI/untitled/pic/Circle.png"))
# window.ui.lbl_type1A.setStyleSheet("QLabel { background-color : red;}")


# Panelx ausgeben
# for element in elements:
#    print(p[1].panel[element])



# print(p[10].panel["IFPANEL"])
#print(p[1].panel["2B"][5])
#print(p[1].panel["2B"][6])
#print(p[1].panel["2B"][7])


window.show()

sys.exit(app.exec())
