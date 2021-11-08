from qtpy import QtWidgets, QtCore, QtGui
from readPanel import *

# https://stackoverflow.com/questions/45575626/make-qlabel-clickable
# https://wiki.python.org/moin/PyQt/Making%20non-clickable%20widgets%20clickable



class Panel:
    def __init__(self, dest, window):
        self.dest = dest
        self.window = window

        self.lbl_type = {}
        self.lbl_nameUp = {}
        self.lbl_nameMiddle = {}
        self.lbl_nameDown = {}
        self.lbl_grid = {
            "1A": (0, 0),
            "1B": (100, 0),
            "1C": (200, 0),
            "1D": (300, 0),
            "1E": (400, 0),
            "1F": (500, 0),
            "1G": (600, 0),
            "1H": (700, 0),
            "2A": (0, 100),
            "2B": (100, 100),
            "2C": (200, 100),
            "2D": (300, 100),
            "2E": (400, 100),
            "2F": (500, 100),
            "2G": (600, 100),
            "2H": (700, 100),
            "3A": (0, 200),
            "3B": (100, 200),
            "3C": (200, 200),
            "3D": (300, 200),
            "3E": (400, 200),
            "3F": (500, 200),
            "3G": (600, 200),
            "3H": (700, 200),
            "4A": (0, 300),
            "4B": (100, 300),
            "4C": (200, 300),
            "4D": (300, 300),
            "4E": (400, 300),
            "4F": (500, 300),
            "4G": (600, 300),
            "4H": (700, 300),
        }
        self.elements = (
            "1A",
            "1B",
            "1C",
            "1D",
            "1E",
            "1F",
            "1G",
            "1H",
            "2A",
            "2B",
            "2C",
            "2D",
            "2E",
            "2F",
            "2G",
            "2H",
            "3A",
            "3B",
            "3C",
            "3D",
            "3E",
            "3F",
            "3G",
            "3H",
            "4A",
            "4B",
            "4C",
            "4D",
            "4E",
            "4F",
            "4G",
            "4H"
        )
        self.typeEvent = {
            "1A": self.typeEvent1A,
            "1B": self.typeEvent1B,
            "1C": self.typeEvent1C,
            "1D": self.typeEvent1D,
            "1E": self.typeEvent1E,
            "1F": self.typeEvent1F,
            "1G": self.typeEvent1G,
            "1H": self.typeEvent1H,
            "2A": self.typeEvent2A,
            "2B": self.typeEvent2B,
            "2C": self.typeEvent2C,
            "2D": self.typeEvent2D,
            "2E": self.typeEvent2E,
            "2F": self.typeEvent2F,
            "2G": self.typeEvent2G,
            "2H": self.typeEvent2H,
            "3A": self.typeEvent3A,
            "3B": self.typeEvent3B,
            "3C": self.typeEvent3C,
            "3D": self.typeEvent3D,
            "3E": self.typeEvent3E,
            "3F": self.typeEvent3F,
            "3G": self.typeEvent3G,
            "3H": self.typeEvent3H,
            "4A": self.typeEvent4A,
            "4B": self.typeEvent4B,
            "4C": self.typeEvent4C,
            "4D": self.typeEvent4D,
            "4E": self.typeEvent4E,
            "4F": self.typeEvent4F,
            "4G": self.typeEvent4G,
            "4H": self.typeEvent4H,
        }

        for e in self.elements:
            self.lbl_type[e] = QtWidgets.QLabel(self.dest)
            self.lbl_type[e].mousePressEvent = self.typeEvent[e]

            self.lbl_nameUp[e] = QtWidgets.QLabel(self.dest)
            self.lbl_nameMiddle[e] = QtWidgets.QLabel(self.dest)
            self.lbl_nameDown[e] = QtWidgets.QLabel(self.dest)

            self.lbl_nameUp[e].mousePressEvent = self.typeEvent[e]
            self.lbl_nameMiddle[e].mousePressEvent = self.typeEvent[e]
            self.lbl_nameDown[e].mousePressEvent = self.typeEvent[e]

            self.setUpPanel(self.lbl_type[e], self.lbl_nameUp[e], self.lbl_nameMiddle[e], self.lbl_nameDown[e],
                            self.lbl_grid[e])

        self.window.iFpanel.append(self)  # add Oject for Connecting, window to current Panel
        self.window.currentTab(0)  # init Connections

    def setUpPanel(self, type: object, up: object, mid: object, dw: object, grid: tuple):
        (x, y) = grid
        type.setPixmap(QtGui.QPixmap("UI/pic/Empty.png"))
        # type.setStyleSheet("QLabel { background-color : blue;}")
        type.setGeometry(x, y, 100, 100)

        up.setGeometry(QtCore.QRect(0 + x, 1 + y, 100, 15))
        up.setText("")
        up.setAlignment(QtCore.Qt.AlignCenter)
        up.setStyleSheet("QLabel { font: bold 14px;}")

        mid.setGeometry(QtCore.QRect(0 + x, 16 + y, 100, 15))
        mid.setText("")
        mid.setAlignment(QtCore.Qt.AlignCenter)
        mid.setStyleSheet("QLabel { font: bold 14px;}")

        dw.setGeometry(QtCore.QRect(0 + x, 31 + y, 100, 15))
        dw.setText("")
        dw.setAlignment(QtCore.Qt.AlignCenter)
        dw.setStyleSheet("QLabel { font: bold 14px;}")

    def setText(self, txt1: str, txt2: str, txt3: str, dest: str):
        # SET TEXT 123 ON PANEL FROM FILE
        for e in self.elements:
            if dest == e:
                self.lbl_nameUp[e].setText(txt1)
                self.lbl_nameMiddle[e].setText(txt2)
                self.lbl_nameDown[e].setText(txt3)
                break

    def setPixmap(self, path, dest: str):
        # SET Pic ON PANEL FROM FILE
        for e in self.elements:
            if dest == e:
                self.lbl_type[e].setPixmap(QtGui.QPixmap(path))
                break

    def setColour(self, style: str, dest: str):
        # SET Colour ON PANEL FROM FILE
        # style = "QLabel { background-color : blue;}"
        for e in self.elements:
            if dest == e:
                self.lbl_type[e].setStyleSheet(style)
                break

    def setTextColour(self, style: str, dest: str):
        # SET TEXT Colour FROM FILE
        # style = QLabel { font: bold 14px; color: Black;}"
        for e in self.elements:
            if dest == e:
                self.lbl_nameUp[e].setStyleSheet(style)
                self.lbl_nameMiddle[e].setStyleSheet(style)
                self.lbl_nameDown[e].setStyleSheet(style)
                break

    def changeName1(self, panel):
        # write data from UI in PanelFile - Update lbl
        for e in self.elements:
            if self.window.ui.cbARrange.currentText() == e: #Data cames when event.select cbARrange, default select is not in the element list
                if (len(self.window.ui.name1.toPlainText().strip()) < 11) and (self.window.ui.cbLanguage.currentText() == "first Language"):  # only 11 characters and 1 line
                    #second name fields, display in Panel depending cbLanguage
                    #saving ever both fields independent of cbLanguage
                    #p has empty datas, when no file loaded
                    self.window.p[panel+1].panel[e][5] = self.window.ui.name1.toPlainText()
                    self.window.p[panel+1].panel[e][19] = self.window.ui.name1_2.toPlainText()
                    self.lbl_nameUp[e].setText(self.window.p[panel+1].panel[e][5])
                    break
                elif (len(self.window.ui.name1_2.toPlainText().strip()) < 11) and (self.window.ui.cbLanguage.currentText() == "second Language"):
                    #second name fields, display in Panel depending cbLanguage
                    #saving ever both fields independent of cbLanguage
                    #p has empty datas, when no file loaded
                    self.window.p[panel+1].panel[e][5] = self.window.ui.name1.toPlainText()
                    self.window.p[panel+1].panel[e][19] = self.window.ui.name1_2.toPlainText()
                    self.lbl_nameUp[e].setText(self.window.p[panel+1].panel[e][19])
                    break

    def changeName2(self, panel):
        # write data from UI in PanelFile - Update lbl
        for e in self.elements:
            if self.window.ui.cbARrange.currentText() == e: #Data cames when event.select cbARrange, default select is not in the element list
                if (len(self.window.ui.name2.toPlainText().strip()) < 11) and (self.window.ui.cbLanguage.currentText() == "first Language"):  # only 11 characters and 1 line
                    #second name fields, display in Panel depending cbLanguage
                    #saving ever both fields independent of cbLanguage
                    #p has empty datas, when no file loaded
                    self.window.p[panel+1].panel[e][6] = self.window.ui.name2.toPlainText()
                    self.window.p[panel+1].panel[e][20] = self.window.ui.name2_2.toPlainText()
                    self.lbl_nameMiddle[e].setText(self.window.p[panel+1].panel[e][6])
                    break
                elif (len(self.window.ui.name2_2.toPlainText().strip()) < 11) and (self.window.ui.cbLanguage.currentText() == "second Language"):
                    #second name fields, display in Panel depending cbLanguage
                    #saving ever both fields independent of cbLanguage
                    #p has empty datas, when no file loaded
                    self.window.p[panel+1].panel[e][6] = self.window.ui.name2.toPlainText()
                    self.window.p[panel+1].panel[e][20] = self.window.ui.name2_2.toPlainText()
                    self.lbl_nameMiddle[e].setText(self.window.p[panel+1].panel[e][20])
                    break

    def changeName3(self, panel):
        # write data from UI in PanelFile - Update lbl
        for e in self.elements:
            if self.window.ui.cbARrange.currentText() == e: #Data cames when event.select cbARrange, default select is not in the element list
                if (len(self.window.ui.name3.toPlainText().strip()) < 11) and (self.window.ui.cbLanguage.currentText() == "first Language"):  # only 11 characters and 1 line
                    #second name fields, display in Panel depending cbLanguage
                    #saving ever both fields independent of cbLanguage
                    #p has empty datas, when no file loaded
                    self.window.p[panel+1].panel[e][7] = self.window.ui.name3.toPlainText()
                    self.window.p[panel+1].panel[e][21] = self.window.ui.name3_2.toPlainText()
                    self.lbl_nameDown[e].setText(self.window.p[panel+1].panel[e][7])
                    break
                elif (len(self.window.ui.name3_2.toPlainText().strip()) < 11) and (self.window.ui.cbLanguage.currentText() == "second Language"):
                    #second name fields, display in Panel depending cbLanguage
                    #saving ever both fields independent of cbLanguage
                    #p has empty datas, when no file loaded
                    self.window.p[panel+1].panel[e][7] = self.window.ui.name3.toPlainText()
                    self.window.p[panel+1].panel[e][21] = self.window.ui.name3_2.toPlainText()
                    self.lbl_nameDown[e].setText(self.window.p[panel+1].panel[e][21])
                    break

    def changeInput(self, panel):
        # write data from UI in PanelFile - Update lbl
        for e in self.elements:
            if self.window.ui.cbARrange.currentText() == e:
                self.window.p[panel + 1].panel[e][11] = self.tryParseInt(self.window.ui.txtInputNumber.toPlainText(), 0)
                self.setEnable(panel)
                break

    def changeOutput1(self, panel):
        # write data from UI in PanelFile - Update lbl
        for e in self.elements:
            if self.window.ui.cbARrange.currentText() == e:
                self.window.p[panel + 1].panel[e][14] = self.tryParseInt(self.window.ui.txtOutputNumber.toPlainText(), 0)
                self.setEnable(panel)
                break

    def changeOutput2(self, panel):
        # write data from UI in PanelFile - Update lbl
        for e in self.elements:
            if self.window.ui.cbARrange.currentText() == e:
                self.window.p[panel + 1].panel[e][17] = self.tryParseInt(self.window.ui.txtOutputNumber_2.toPlainText(), 0)
                self.setEnable(panel)
                break

    def changeCBoxes(self, panel):
        # write data from UI in PanelFile - Update lbl
        for e in self.elements:
            if self.window.ui.cbARrange.currentText() == e: #Data cames when event.select cbARrange, default select is not in the element list
                self.window.p[panel + 1].panel[e][3] = self.window.ui.cbColor.currentIndex()
                self.window.p[panel + 1].panel[e][9] = self.window.ui.cbInterlock.currentIndex()
                self.window.p[panel + 1].panel[e][8] = self.window.ui.cbSecurity.currentIndex()
                self.window.p[panel + 1].panel[e][1] = self.window.ui.cbSetup.currentIndex()
                self.window.p[panel + 1].panel[e][4] = self.window.ui.cbTextColor.currentIndex()
                self.window.p[panel + 1].panel[e][2] = self.window.ui.cbType.currentIndex()

                self.window.p[panel + 1].panel[e][10] = self.window.ui.cbInput.currentIndex()
                self.window.p[panel + 1].panel[e][12] = self.window.ui.cbContactIn.currentIndex()
                self.window.p[panel + 1].panel[e][13] = self.window.ui.cbOutput.currentIndex()
                self.window.p[panel + 1].panel[e][15] = self.window.ui.cbContactOut.currentIndex()
                self.window.p[panel + 1].panel[e][16] = self.window.ui.cbOutput_2.currentIndex()
                self.window.p[panel + 1].panel[e][18] = self.window.ui.cbContactOut_2.currentIndex()

                #update Panel - only 3 relevance options
                self.setPixmap(PanelDiscripition.panelType[str(self.window.p[panel + 1].panel[e][2])], e)
                self.setColour(PanelDiscripition.PanelColor[str(self.window.p[panel + 1].panel[e][3])], e)
                self.setTextColour(PanelDiscripition.TextColor[str(self.window.p[panel + 1].panel[e][4])], e)
                self.setEnable(panel)
                break

    def currentRange(self, panel):
        #cbARrange.currentTextChanged - 1A -> 1B
        for e in self.elements:
            if self.window.ui.cbARrange.currentText() == e:
                    self.window.ui.name1.setPlainText(self.window.p[panel + 1].panel[e][5])
                    self.window.ui.name2.setPlainText(self.window.p[panel + 1].panel[e][6])
                    self.window.ui.name3.setPlainText(self.window.p[panel + 1].panel[e][7])
                    self.window.ui.name1_2.setPlainText(self.window.p[panel + 1].panel[e][19])
                    self.window.ui.name2_2.setPlainText(self.window.p[panel + 1].panel[e][20])
                    self.window.ui.name3_2.setPlainText(self.window.p[panel + 1].panel[e][21])
                    self.window.ui.cbColor.setCurrentIndex(int(self.window.p[panel + 1].panel[e][3]))
                    self.window.ui.cbInterlock.setCurrentIndex(int(self.window.p[panel + 1].panel[e][9]))
                    self.window.ui.cbSecurity.setCurrentIndex(int(self.window.p[panel + 1].panel[e][8]))
                    self.window.ui.cbSetup.setCurrentIndex(int(self.window.p[panel + 1].panel[e][1]))
                    self.window.ui.cbTextColor.setCurrentIndex(int(self.window.p[panel + 1].panel[e][4]))
                    self.window.ui.cbType.setCurrentIndex(int(self.window.p[panel + 1].panel[e][2]))

                    self.window.ui.cbInput.setCurrentIndex(int(self.window.p[panel + 1].panel[e][10]))
                    self.window.ui.txtInputNumber.setPlainText(str(self.window.p[panel + 1].panel[e][11]))
                    self.window.ui.cbContactIn.setCurrentIndex(int(self.window.p[panel + 1].panel[e][12]))
                    self.window.ui.cbOutput.setCurrentIndex(int(self.window.p[panel + 1].panel[e][13]))
                    self.window.ui.txtOutputNumber.setPlainText(str(self.window.p[panel + 1].panel[e][14]))
                    self.window.ui.cbContactOut.setCurrentIndex(int(self.window.p[panel + 1].panel[e][15]))
                    self.window.ui.cbOutput_2.setCurrentIndex(int(self.window.p[panel + 1].panel[e][16]))
                    self.window.ui.txtOutputNumber_2.setPlainText(str(self.window.p[panel + 1].panel[e][17]))
                    self.window.ui.cbContactOut_2.setCurrentIndex(int(self.window.p[panel + 1].panel[e][18]))
                    self.setEnable(panel)
                    break

    def setEnable(self, panel):
        for e in self.elements:
            if self.window.ui.cbARrange.currentText() == e:
                self.window.ui.cbOutput.setEnabled(self.enableOutput(int(self.window.p[panel + 1].panel[e][2]), self.tryParseInt(self.window.p[panel + 1].panel[e][11], 0)))
                self.window.ui.cbOutput_2.setEnabled(self.enableOutput(int(self.window.p[panel + 1].panel[e][2]), self.tryParseInt(self.window.p[panel + 1].panel[e][11], 0)))
                self.window.ui.cbContactOut.setEnabled(self.enableOutput(int(self.window.p[panel + 1].panel[e][2]), self.tryParseInt(self.window.p[panel + 1].panel[e][11], 0)))
                self.window.ui.cbContactOut_2.setEnabled(self.enableOutput(int(self.window.p[panel + 1].panel[e][2]), self.tryParseInt(self.window.p[panel + 1].panel[e][11], 0)))
                self.window.ui.txtOutputNumber.setEnabled(self.enableOutput(int(self.window.p[panel + 1].panel[e][2]), self.tryParseInt(self.window.p[panel + 1].panel[e][11], 0)))
                self.window.ui.txtOutputNumber_2.setEnabled(self.enableOutput(int(self.window.p[panel + 1].panel[e][2]), self.tryParseInt(self.window.p[panel + 1].panel[e][11], 0)))
                break

    def typeEvent1A(self, event):
        self.window.ui.cbARrange.setCurrentIndex(1)

    def typeEvent1B(self, event):
        self.window.ui.cbARrange.setCurrentIndex(2)

    def typeEvent1C(self, event):
        self.window.ui.cbARrange.setCurrentIndex(3)

    def typeEvent1D(self, event):
        self.window.ui.cbARrange.setCurrentIndex(4)

    def typeEvent1E(self, event):
        self.window.ui.cbARrange.setCurrentIndex(5)

    def typeEvent1F(self, event):
        self.window.ui.cbARrange.setCurrentIndex(6)

    def typeEvent1G(self, event):
        self.window.ui.cbARrange.setCurrentIndex(7)

    def typeEvent1H(self, event):
        self.window.ui.cbARrange.setCurrentIndex(8)

    def typeEvent2A(self, event):
        self.window.ui.cbARrange.setCurrentIndex(9)

    def typeEvent2B(self, event):
        self.window.ui.cbARrange.setCurrentIndex(10)

    def typeEvent2C(self, event):
        self.window.ui.cbARrange.setCurrentIndex(11)

    def typeEvent2D(self, event):
        self.window.ui.cbARrange.setCurrentIndex(12)

    def typeEvent2E(self, event):
        self.window.ui.cbARrange.setCurrentIndex(13)

    def typeEvent2F(self, event):
        self.window.ui.cbARrange.setCurrentIndex(14)

    def typeEvent2G(self, event):
        self.window.ui.cbARrange.setCurrentIndex(15)

    def typeEvent2H(self, event):
        self.window.ui.cbARrange.setCurrentIndex(16)

    def typeEvent3A(self, event):
        self.window.ui.cbARrange.setCurrentIndex(17)

    def typeEvent3B(self, event):
        self.window.ui.cbARrange.setCurrentIndex(18)

    def typeEvent3C(self, event):
        self.window.ui.cbARrange.setCurrentIndex(19)

    def typeEvent3D(self, event):
        self.window.ui.cbARrange.setCurrentIndex(20)

    def typeEvent3E(self, event):
        self.window.ui.cbARrange.setCurrentIndex(21)

    def typeEvent3F(self, event):
        self.window.ui.cbARrange.setCurrentIndex(22)

    def typeEvent3G(self, event):
        self.window.ui.cbARrange.setCurrentIndex(23)

    def typeEvent3H(self, event):
        self.window.ui.cbARrange.setCurrentIndex(24)

    def typeEvent4A(self, event):
        self.window.ui.cbARrange.setCurrentIndex(25)

    def typeEvent4B(self, event):
        self.window.ui.cbARrange.setCurrentIndex(26)

    def typeEvent4C(self, event):
        self.window.ui.cbARrange.setCurrentIndex(27)

    def typeEvent4D(self, event):
        self.window.ui.cbARrange.setCurrentIndex(28)

    def typeEvent4E(self, event):
        self.window.ui.cbARrange.setCurrentIndex(29)

    def typeEvent4F(self, event):
        self.window.ui.cbARrange.setCurrentIndex(30)

    def typeEvent4G(self, event):
        self.window.ui.cbARrange.setCurrentIndex(31)

    def typeEvent4H(self, event):
        self.window.ui.cbARrange.setCurrentIndex(32)

    def tryParseInt(self, s, val=None):
        try:
            return int(s)
        except ValueError:
            return val

    def chkRange(self, input: str, Range: tuple):
        (min, max) = Range

        input = self.tryParseInt(input, 0)

        if input >= min and input <= max:
            return True
        else:
            return False

    def enableOutput(self, iconType, Range :int):
        if (self.window.ui.cbInput.currentIndex() == 1) and (iconType < 13) :
            if self.chkRange(Range, (10, 12567)):  # 10010 to #12567 (2048 signals) enable
                return True
            elif self.chkRange(Range, (30010, 32567)):  # 30010 to #32567 (2048 signals) enable
                return True
            elif self.chkRange(Range, (60010, 60647)):  # 60010 to #60647 (512 signals) enable
                return True
            elif self.chkRange(Range, (35010, 37567)):  # 35010 to #37567 (2048 signals) enable
                return True
            else:
                # 00010 to #02567 (2048 signals) disable
                # 20010 to #22567 (2048 signals) disable
                # 40010 to #41607 (1280 signals) disable
                # 50010 to #52007 (1600 signals) disable
                # 70010 to #79997 (7992 signals) disable
                # 80010 to #80647 (512 signals) disable
                # 82010 to #82207 (160 signals) disable
                # 25010 to #27567 (2048 signals) disable
                return False
        elif iconType == 16 or iconType == 17:
            return self.chkRange(Range, (0, 1000))
        else:
            return False
