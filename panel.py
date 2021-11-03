from qtpy import QtWidgets, QtCore, QtGui


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
            self.lbl_type[e].mouseReleaseEvent = self.typeEvent[e]
            self.lbl_nameUp[e] = QtWidgets.QLabel(self.dest)
            self.lbl_nameMiddle[e] = QtWidgets.QLabel(self.dest)
            self.lbl_nameDown[e] = QtWidgets.QLabel(self.dest)

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

    def changeName1(self):
        # SET TEXT 1 ON PANEL FROM UI
        for e in self.elements:
            if self.window.ui.cbARrange.currentText() == e:
                self.lbl_nameUp[e].setText(self.window.ui.name1.toPlainText())
                break

    def changeName2(self):
        # SET TEXT 2 ON PANEL FROM UI
        for e in self.elements:
            if self.window.ui.cbARrange.currentText() == e:
                self.lbl_nameMiddle[e].setText(self.window.ui.name2.toPlainText())
                break

    def changeName3(self):
        # SET TEXT 3 ON PANEL FROM UI
        for e in self.elements:
            if self.window.ui.cbARrange.currentText() == e:
                self.lbl_nameDown[e].setText(self.window.ui.name3.toPlainText())
                break

    def currentRange(self):
        # SET TEXT 123 ON UI FROM PANEL
        for e in self.elements:
            if self.window.ui.cbARrange.currentText() == e:
                self.window.ui.name1.setPlainText(self.lbl_nameUp[e].text())
                self.window.ui.name2.setPlainText(self.lbl_nameMiddle[e].text())
                self.window.ui.name3.setPlainText(self.lbl_nameDown[e].text())
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
