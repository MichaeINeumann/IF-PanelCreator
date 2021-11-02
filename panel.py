from qtpy import QtWidgets, QtCore, QtGui


class Panel:
    def __init__(self, dest):
        self.dest = dest
        self.lbl_type1A = QtWidgets.QLabel(self.dest)
        self.lbl_type2A = QtWidgets.QLabel(self.dest)
        self.lbl_type3A = QtWidgets.QLabel(self.dest)
        self.lbl_type4A = QtWidgets.QLabel(self.dest)
        self.lbl_type1B = QtWidgets.QLabel(self.dest)
        self.lbl_type2B = QtWidgets.QLabel(self.dest)
        self.lbl_type3B = QtWidgets.QLabel(self.dest)
        self.lbl_type4B = QtWidgets.QLabel(self.dest)
        self.lbl_type1C = QtWidgets.QLabel(self.dest)
        self.lbl_type2C = QtWidgets.QLabel(self.dest)
        self.lbl_type3C = QtWidgets.QLabel(self.dest)
        self.lbl_type4C = QtWidgets.QLabel(self.dest)
        self.lbl_type1D = QtWidgets.QLabel(self.dest)
        self.lbl_type2D = QtWidgets.QLabel(self.dest)
        self.lbl_type3D = QtWidgets.QLabel(self.dest)
        self.lbl_type4D = QtWidgets.QLabel(self.dest)
        self.lbl_type1E = QtWidgets.QLabel(self.dest)
        self.lbl_type2E = QtWidgets.QLabel(self.dest)
        self.lbl_type3E = QtWidgets.QLabel(self.dest)
        self.lbl_type4E = QtWidgets.QLabel(self.dest)
        self.lbl_type1F = QtWidgets.QLabel(self.dest)
        self.lbl_type2F = QtWidgets.QLabel(self.dest)
        self.lbl_type3F = QtWidgets.QLabel(self.dest)
        self.lbl_type4F = QtWidgets.QLabel(self.dest)
        self.lbl_type1G = QtWidgets.QLabel(self.dest)
        self.lbl_type2G = QtWidgets.QLabel(self.dest)
        self.lbl_type3G = QtWidgets.QLabel(self.dest)
        self.lbl_type4G = QtWidgets.QLabel(self.dest)
        self.lbl_type1H = QtWidgets.QLabel(self.dest)
        self.lbl_type2H = QtWidgets.QLabel(self.dest)
        self.lbl_type3H = QtWidgets.QLabel(self.dest)
        self.lbl_type4H = QtWidgets.QLabel(self.dest)

        self.lbl_name1Aup = QtWidgets.QLabel(self.dest)
        self.lbl_name1Amid = QtWidgets.QLabel(self.dest)
        self.lbl_name1Adw = QtWidgets.QLabel(self.dest)
        self.lbl_name1Bup = QtWidgets.QLabel(self.dest)
        self.lbl_name1Bmid = QtWidgets.QLabel(self.dest)
        self.lbl_name1Bdw = QtWidgets.QLabel(self.dest)
        self.lbl_name1Cup = QtWidgets.QLabel(self.dest)
        self.lbl_name1Cmid = QtWidgets.QLabel(self.dest)
        self.lbl_name1Cdw = QtWidgets.QLabel(self.dest)
        self.lbl_name1Dup = QtWidgets.QLabel(self.dest)
        self.lbl_name1Dmid = QtWidgets.QLabel(self.dest)
        self.lbl_name1Ddw = QtWidgets.QLabel(self.dest)
        self.lbl_name1Eup = QtWidgets.QLabel(self.dest)
        self.lbl_name1Emid = QtWidgets.QLabel(self.dest)
        self.lbl_name1Edw = QtWidgets.QLabel(self.dest)
        self.lbl_name1Fup = QtWidgets.QLabel(self.dest)
        self.lbl_name1Fmid = QtWidgets.QLabel(self.dest)
        self.lbl_name1Fdw = QtWidgets.QLabel(self.dest)
        self.lbl_name1Gup = QtWidgets.QLabel(self.dest)
        self.lbl_name1Gmid = QtWidgets.QLabel(self.dest)
        self.lbl_name1Gdw = QtWidgets.QLabel(self.dest)
        self.lbl_name1Hup = QtWidgets.QLabel(self.dest)
        self.lbl_name1Hmid = QtWidgets.QLabel(self.dest)
        self.lbl_name1Hdw = QtWidgets.QLabel(self.dest)

        self.lbl_name2Aup = QtWidgets.QLabel(self.dest)
        self.lbl_name2Amid = QtWidgets.QLabel(self.dest)
        self.lbl_name2Adw = QtWidgets.QLabel(self.dest)
        self.lbl_name2Bup = QtWidgets.QLabel(self.dest)
        self.lbl_name2Bmid = QtWidgets.QLabel(self.dest)
        self.lbl_name2Bdw = QtWidgets.QLabel(self.dest)
        self.lbl_name2Cup = QtWidgets.QLabel(self.dest)
        self.lbl_name2Cmid = QtWidgets.QLabel(self.dest)
        self.lbl_name2Cdw = QtWidgets.QLabel(self.dest)
        self.lbl_name2Dup = QtWidgets.QLabel(self.dest)
        self.lbl_name2Dmid = QtWidgets.QLabel(self.dest)
        self.lbl_name2Ddw = QtWidgets.QLabel(self.dest)
        self.lbl_name2Eup = QtWidgets.QLabel(self.dest)
        self.lbl_name2Emid = QtWidgets.QLabel(self.dest)
        self.lbl_name2Edw = QtWidgets.QLabel(self.dest)
        self.lbl_name2Fup = QtWidgets.QLabel(self.dest)
        self.lbl_name2Fmid = QtWidgets.QLabel(self.dest)
        self.lbl_name2Fdw = QtWidgets.QLabel(self.dest)
        self.lbl_name2Gup = QtWidgets.QLabel(self.dest)
        self.lbl_name2Gmid = QtWidgets.QLabel(self.dest)
        self.lbl_name2Gdw = QtWidgets.QLabel(self.dest)
        self.lbl_name2Hup = QtWidgets.QLabel(self.dest)
        self.lbl_name2Hmid = QtWidgets.QLabel(self.dest)
        self.lbl_name2Hdw = QtWidgets.QLabel(self.dest)

        self.lbl_name3Aup = QtWidgets.QLabel(self.dest)
        self.lbl_name3Amid = QtWidgets.QLabel(self.dest)
        self.lbl_name3Adw = QtWidgets.QLabel(self.dest)
        self.lbl_name3Bup = QtWidgets.QLabel(self.dest)
        self.lbl_name3Bmid = QtWidgets.QLabel(self.dest)
        self.lbl_name3Bdw = QtWidgets.QLabel(self.dest)
        self.lbl_name3Cup = QtWidgets.QLabel(self.dest)
        self.lbl_name3Cmid = QtWidgets.QLabel(self.dest)
        self.lbl_name3Cdw = QtWidgets.QLabel(self.dest)
        self.lbl_name3Dup = QtWidgets.QLabel(self.dest)
        self.lbl_name3Dmid = QtWidgets.QLabel(self.dest)
        self.lbl_name3Ddw = QtWidgets.QLabel(self.dest)
        self.lbl_name3Eup = QtWidgets.QLabel(self.dest)
        self.lbl_name3Emid = QtWidgets.QLabel(self.dest)
        self.lbl_name3Edw = QtWidgets.QLabel(self.dest)
        self.lbl_name3Fup = QtWidgets.QLabel(self.dest)
        self.lbl_name3Fmid = QtWidgets.QLabel(self.dest)
        self.lbl_name3Fdw = QtWidgets.QLabel(self.dest)
        self.lbl_name3Gup = QtWidgets.QLabel(self.dest)
        self.lbl_name3Gmid = QtWidgets.QLabel(self.dest)
        self.lbl_name3Gdw = QtWidgets.QLabel(self.dest)
        self.lbl_name3Hup = QtWidgets.QLabel(self.dest)
        self.lbl_name3Hmid = QtWidgets.QLabel(self.dest)
        self.lbl_name3Hdw = QtWidgets.QLabel(self.dest)

        self.lbl_name4Aup = QtWidgets.QLabel(self.dest)
        self.lbl_name4Amid = QtWidgets.QLabel(self.dest)
        self.lbl_name4Adw = QtWidgets.QLabel(self.dest)
        self.lbl_name4Bup = QtWidgets.QLabel(self.dest)
        self.lbl_name4Bmid = QtWidgets.QLabel(self.dest)
        self.lbl_name4Bdw = QtWidgets.QLabel(self.dest)
        self.lbl_name4Cup = QtWidgets.QLabel(self.dest)
        self.lbl_name4Cmid = QtWidgets.QLabel(self.dest)
        self.lbl_name4Cdw = QtWidgets.QLabel(self.dest)
        self.lbl_name4Dup = QtWidgets.QLabel(self.dest)
        self.lbl_name4Dmid = QtWidgets.QLabel(self.dest)
        self.lbl_name4Ddw = QtWidgets.QLabel(self.dest)
        self.lbl_name4Eup = QtWidgets.QLabel(self.dest)
        self.lbl_name4Emid = QtWidgets.QLabel(self.dest)
        self.lbl_name4Edw = QtWidgets.QLabel(self.dest)
        self.lbl_name4Fup = QtWidgets.QLabel(self.dest)
        self.lbl_name4Fmid = QtWidgets.QLabel(self.dest)
        self.lbl_name4Fdw = QtWidgets.QLabel(self.dest)
        self.lbl_name4Gup = QtWidgets.QLabel(self.dest)
        self.lbl_name4Gmid = QtWidgets.QLabel(self.dest)
        self.lbl_name4Gdw = QtWidgets.QLabel(self.dest)
        self.lbl_name4Hup = QtWidgets.QLabel(self.dest)
        self.lbl_name4Hmid = QtWidgets.QLabel(self.dest)
        self.lbl_name4Hdw = QtWidgets.QLabel(self.dest)

        self.setUpPanel(self.lbl_type1A, self.lbl_name1Aup, self.lbl_name1Amid, self.lbl_name1Adw, 0, 0)
        self.setUpPanel(self.lbl_type1B, self.lbl_name1Bup, self.lbl_name1Bmid, self.lbl_name1Bdw, 100, 0)
        self.setUpPanel(self.lbl_type1C, self.lbl_name1Cup, self.lbl_name1Cmid, self.lbl_name1Cdw, 200, 0)
        self.setUpPanel(self.lbl_type1D, self.lbl_name1Dup, self.lbl_name1Dmid, self.lbl_name1Ddw, 300, 0)
        self.setUpPanel(self.lbl_type1E, self.lbl_name1Eup, self.lbl_name1Emid, self.lbl_name1Edw, 400, 0)
        self.setUpPanel(self.lbl_type1F, self.lbl_name1Fup, self.lbl_name1Fmid, self.lbl_name1Fdw, 500, 0)
        self.setUpPanel(self.lbl_type1G, self.lbl_name1Gup, self.lbl_name1Gmid, self.lbl_name1Gdw, 600, 0)
        self.setUpPanel(self.lbl_type1H, self.lbl_name1Hup, self.lbl_name1Hmid, self.lbl_name1Hdw, 700, 0)

        self.setUpPanel(self.lbl_type2A, self.lbl_name2Aup, self.lbl_name2Amid, self.lbl_name2Adw, 0, 100)
        self.setUpPanel(self.lbl_type2B, self.lbl_name2Bup, self.lbl_name2Bmid, self.lbl_name2Bdw, 100, 100)
        self.setUpPanel(self.lbl_type2C, self.lbl_name2Cup, self.lbl_name2Cmid, self.lbl_name2Cdw, 200, 100)
        self.setUpPanel(self.lbl_type2D, self.lbl_name2Dup, self.lbl_name2Dmid, self.lbl_name2Ddw, 300, 100)
        self.setUpPanel(self.lbl_type2E, self.lbl_name2Eup, self.lbl_name2Emid, self.lbl_name2Edw, 400, 100)
        self.setUpPanel(self.lbl_type2F, self.lbl_name2Fup, self.lbl_name2Fmid, self.lbl_name2Fdw, 500, 100)
        self.setUpPanel(self.lbl_type2G, self.lbl_name2Gup, self.lbl_name2Gmid, self.lbl_name2Gdw, 600, 100)
        self.setUpPanel(self.lbl_type2H, self.lbl_name2Hup, self.lbl_name2Hmid, self.lbl_name2Hdw, 700, 100)

        self.setUpPanel(self.lbl_type3A, self.lbl_name3Aup, self.lbl_name3Amid, self.lbl_name3Adw, 0, 200)
        self.setUpPanel(self.lbl_type3B, self.lbl_name3Bup, self.lbl_name3Bmid, self.lbl_name3Bdw, 100, 200)
        self.setUpPanel(self.lbl_type3C, self.lbl_name3Cup, self.lbl_name3Cmid, self.lbl_name3Cdw, 200, 200)
        self.setUpPanel(self.lbl_type3D, self.lbl_name3Dup, self.lbl_name3Dmid, self.lbl_name3Ddw, 300, 200)
        self.setUpPanel(self.lbl_type3E, self.lbl_name3Eup, self.lbl_name3Emid, self.lbl_name3Edw, 400, 200)
        self.setUpPanel(self.lbl_type3F, self.lbl_name3Fup, self.lbl_name3Fmid, self.lbl_name3Fdw, 500, 200)
        self.setUpPanel(self.lbl_type3G, self.lbl_name3Gup, self.lbl_name3Gmid, self.lbl_name3Gdw, 600, 200)
        self.setUpPanel(self.lbl_type3H, self.lbl_name3Hup, self.lbl_name3Hmid, self.lbl_name3Hdw, 700, 200)

        self.setUpPanel(self.lbl_type4A, self.lbl_name4Aup, self.lbl_name4Amid, self.lbl_name4Adw, 0, 300)
        self.setUpPanel(self.lbl_type4B, self.lbl_name4Bup, self.lbl_name4Bmid, self.lbl_name4Bdw, 100, 300)
        self.setUpPanel(self.lbl_type4C, self.lbl_name4Cup, self.lbl_name4Cmid, self.lbl_name4Cdw, 200, 300)
        self.setUpPanel(self.lbl_type4D, self.lbl_name4Dup, self.lbl_name4Dmid, self.lbl_name4Ddw, 300, 300)
        self.setUpPanel(self.lbl_type4E, self.lbl_name4Eup, self.lbl_name4Emid, self.lbl_name4Edw, 400, 300)
        self.setUpPanel(self.lbl_type4F, self.lbl_name4Fup, self.lbl_name4Fmid, self.lbl_name4Fdw, 500, 300)
        self.setUpPanel(self.lbl_type4G, self.lbl_name4Gup, self.lbl_name4Gmid, self.lbl_name4Gdw, 600, 300)
        self.setUpPanel(self.lbl_type4H, self.lbl_name4Hup, self.lbl_name4Hmid, self.lbl_name4Hdw, 700, 300)

        #self.setText("init")

    def setUpPanel(self, lbl_type, up, mid, dw, x, y):
        lbl_type.setPixmap(QtGui.QPixmap("ui/pic/Circle.png"))
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

    def setText(self, txt1, txt2, txt3, dest):
        if dest == "1A":
            self.lbl_name1Aup.setText(txt1)
            self.lbl_name1Amid.setText(txt2)
            self.lbl_name1Adw.setText(txt3)
