#main.py - Main entry point
#Copyright (C) 2021  Michael Neumann <michael-n@gmx.net>

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.
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

        self.p = readFile("IFPANELempty.DAT")  # init with empty datas

        self.connect()

    def currentTab(self, tab):
        self.__currentTab = tab
        tabTxt = self.ui.tabWidget.tabText(tab)
        self.ui.groupName.setPlainText(tabTxt)

        # RECONNECT WHEN TAB CHANGED
        self.ui.cbARrange.currentTextChanged.connect(self.currentRange)
        self.ui.cbLanguage.currentIndexChanged.connect(self.currentRange)
        self.ui.cbARrange.currentTextChanged.disconnect()  # this disconnect all
        self.ui.cbARrange.currentTextChanged.connect(self.currentRange)
        self.ui.cbLanguage.currentIndexChanged.connect(self.currentRange)



        self.iFpanel[self.__currentTab].currentRange(self.__currentTab)  # update name1,2,3

    def changeName1(self):
        #call Panel instance
        self.iFpanel[self.__currentTab].changeName1(self.__currentTab)

    def changeName2(self):
        #call Panel instance
        self.iFpanel[self.__currentTab].changeName2(self.__currentTab)

    def changeName3(self):
        #call Panel instance
        self.iFpanel[self.__currentTab].changeName3(self.__currentTab)

    def changeInput(self):
        #call Panel instance
        self.iFpanel[self.__currentTab].changeInput(self.__currentTab)

    def changeOutput1(self):
        #call Panel instance
        self.iFpanel[self.__currentTab].changeOutput1(self.__currentTab)

    def changeOutput2(self):
        #call Panel instance
        self.iFpanel[self.__currentTab].changeOutput2(self.__currentTab)

    def currentRange(self, event):
        #disconect while setting up cBoxes
        self.ui.name1.textChanged.connect(self.changeName1)
        self.ui.name1_2.textChanged.connect(self.changeName1)
        self.ui.name1.textChanged.disconnect()  # this disconnect all
        self.ui.name2.textChanged.connect(self.changeName2)
        self.ui.name2_2.textChanged.connect(self.changeName2)
        self.ui.name2.textChanged.disconnect()  # this disconnect all
        self.ui.name3.textChanged.connect(self.changeName3)
        self.ui.name3_2.textChanged.connect(self.changeName3)
        self.ui.name3.textChanged.disconnect()  # this disconnect all
        self.ui.cbColor.currentIndexChanged.connect(self.changeCBoxes)
        self.ui.cbColor.currentIndexChanged.disconnect()
        self.ui.cbInterlock.currentIndexChanged.connect(self.changeCBoxes)
        self.ui.cbInterlock.currentIndexChanged.disconnect()
        self.ui.cbSecurity.currentIndexChanged.connect(self.changeCBoxes)
        self.ui.cbSecurity.currentIndexChanged.disconnect()
        self.ui.cbSetup.currentIndexChanged.connect(self.changeCBoxes)
        self.ui.cbSetup.currentIndexChanged.disconnect()
        self.ui.cbTextColor.currentIndexChanged.connect(self.changeCBoxes)
        self.ui.cbTextColor.currentIndexChanged.disconnect()
        self.ui.cbType.currentIndexChanged.connect(self.changeCBoxes)
        self.ui.cbType.currentIndexChanged.disconnect()

        self.ui.cbInput.currentIndexChanged.connect(self.changeCBoxes)
        self.ui.txtInputNumber.textChanged.connect(self.changeInput)
        self.ui.cbContactIn.currentIndexChanged.connect(self.changeCBoxes)

        self.ui.cbOutput.currentIndexChanged.connect(self.changeCBoxes)
        self.ui.txtOutputNumber.textChanged.connect(self.changeOutput1)
        self.ui.cbContactOut.currentIndexChanged.connect(self.changeCBoxes)

        self.ui.cbOutput_2.currentIndexChanged.connect(self.changeCBoxes)
        self.ui.txtOutputNumber_2.textChanged.connect(self.changeOutput2)
        self.ui.cbContactOut_2.currentIndexChanged.connect(self.changeCBoxes)

        self.ui.cbInput.currentIndexChanged.disconnect()
        self.ui.txtInputNumber.textChanged.disconnect()
        self.ui.cbContactIn.currentIndexChanged.disconnect()
        self.ui.cbOutput.currentIndexChanged.disconnect()
        self.ui.txtOutputNumber.textChanged.disconnect()
        self.ui.cbContactOut.currentIndexChanged.disconnect()
        self.ui.cbOutput_2.currentIndexChanged.disconnect()
        self.ui.txtOutputNumber_2.textChanged.disconnect()
        self.ui.cbContactOut_2.currentIndexChanged.disconnect()

        #update all
        for e in PanelDiscripition.elements:
            for i in range(9):
                if self.p[i + 1].panel[e][1] == "1":  # VALID DATA
                    if (self.ui.cbLanguage.currentText() == "first Language"):
                        self.iFpanel[i].setText(self.p[i + 1].panel[e][5], self.p[i + 1].panel[e][6],self.p[i + 1].panel[e][7], e)
                    else:
                        self.iFpanel[i].setText(self.p[i + 1].panel[e][19], self.p[i + 1].panel[e][20],self.p[i + 1].panel[e][21], e)

                    self.iFpanel[i].setPixmap(PanelDiscripition.panelType[self.p[i + 1].panel[e][2]], e)
                    self.iFpanel[i].setColour(PanelDiscripition.PanelColor[self.p[i + 1].panel[e][3]], e)
                    self.iFpanel[i].setTextColour(PanelDiscripition.TextColor[self.p[i + 1].panel[e][4]], e)

        #call Panel instance
        self.iFpanel[self.__currentTab].currentRange(self.__currentTab)

        #reconnect after set up Boxes
        self.ui.name1.textChanged.connect(self.changeName1)
        self.ui.name1_2.textChanged.connect(self.changeName1)
        self.ui.name2.textChanged.connect(self.changeName2)
        self.ui.name2_2.textChanged.connect(self.changeName2)
        self.ui.name3.textChanged.connect(self.changeName3)
        self.ui.name3_2.textChanged.connect(self.changeName3)
        self.ui.cbColor.currentIndexChanged.connect(self.changeCBoxes)
        self.ui.cbInterlock.currentIndexChanged.connect(self.changeCBoxes)
        self.ui.cbSecurity.currentIndexChanged.connect(self.changeCBoxes)
        self.ui.cbSetup.currentIndexChanged.connect(self.changeCBoxes)
        self.ui.cbTextColor.currentIndexChanged.connect(self.changeCBoxes)
        self.ui.cbType.currentIndexChanged.connect(self.changeCBoxes)

        self.ui.cbInput.currentIndexChanged.connect(self.changeCBoxes)
        self.ui.txtInputNumber.textChanged.connect(self.changeInput)
        self.ui.cbContactIn.currentIndexChanged.connect(self.changeCBoxes)

        self.ui.cbOutput.currentIndexChanged.connect(self.changeCBoxes)
        self.ui.txtOutputNumber.textChanged.connect(self.changeOutput1)
        self.ui.cbContactOut.currentIndexChanged.connect(self.changeCBoxes)

        self.ui.cbOutput_2.currentIndexChanged.connect(self.changeCBoxes)
        self.ui.txtOutputNumber_2.textChanged.connect(self.changeOutput2)
        self.ui.cbContactOut_2.currentIndexChanged.connect(self.changeCBoxes)

    def changeCBoxes(self, event):
        #call Panel instance
        self.iFpanel[self.__currentTab].changeCBoxes(self.__currentTab)

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
                for i in range(9):
                    if self.p[i+1].panel[e][1] == "1": #VALID DATA
                        self.iFpanel[i].setText(self.p[i+1].panel[e][5], self.p[i+1].panel[e][6], self.p[i+1].panel[e][7], e)
                        self.iFpanel[i].setPixmap(PanelDiscripition.panelType[self.p[i+1].panel[e][2]], e)
                        self.iFpanel[i].setColour(PanelDiscripition.PanelColor[self.p[i+1].panel[e][3]], e)
                        self.iFpanel[i].setTextColour(PanelDiscripition.TextColor[self.p[i + 1].panel[e][4]], e)


            self.ui.tabWidget.setTabText(0, self.p[1].panel["NAME"][1])
            self.ui.tabWidget.setTabText(1, self.p[2].panel["NAME"][1])
            self.ui.tabWidget.setTabText(2, self.p[3].panel["NAME"][1])
            self.ui.tabWidget.setTabText(3, self.p[4].panel["NAME"][1])
            self.ui.tabWidget.setTabText(4, self.p[5].panel["NAME"][1])
            self.ui.tabWidget.setTabText(5, self.p[6].panel["NAME"][1])
            self.ui.tabWidget.setTabText(6, self.p[7].panel["NAME"][1])
            self.ui.tabWidget.setTabText(7, self.p[8].panel["NAME"][1])
            self.ui.tabWidget.setTabText(8, self.p[9].panel["NAME"][1])
            self.ui.tabWidget.setTabText(9, self.p[10].panel["NAME"][1])

    def savefile(self):
        writeFile(self.fname, self.p)

    def savefile_as(self):
        eeg_cap_dir = QtCore.QDir.currentPath()
        dialog = QtWidgets.QFileDialog(self)
        dialog.setWindowTitle('Open EEG Position file')
        dialog.setNameFilter('(*.DAT)')
        dialog.setDirectory(eeg_cap_dir)
        dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        filename = None
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            filename = dialog.selectedFiles()
        if filename:
            self.fname = str(filename[0])
            writeFile(self.fname, self.p)

    def connect(self):
        self.ui.tabWidget.tabBarClicked.connect(self.currentTab)
        self.ui.groupName.textChanged.connect(self.changeGroupName)

        self.ui.actionLoad.triggered.connect(self.getfile)
        self.ui.actionSave.triggered.connect(self.savefile)
        self.ui.actionSave_as.triggered.connect(self.savefile_as)


window = MainWindow()


iFpanel = Panel(window.ui.tab_1, window)
iFpanel1 = Panel(window.ui.tab_2, window)
iFpanel2 = Panel(window.ui.tab_3, window)
iFpanel3 = Panel(window.ui.tab_4, window)
iFpanel4 = Panel(window.ui.tab_5, window)
iFpanel5 = Panel(window.ui.tab_6, window)
iFpanel6 = Panel(window.ui.tab_7, window)
iFpanel7 = Panel(window.ui.tab_8, window)
iFpanel8 = Panel(window.ui.tab_9, window)
iFpanel9 = Panel(window.ui.tab_10, window)

app.aboutQt( )


window.show()

sys.exit(app.exec())
