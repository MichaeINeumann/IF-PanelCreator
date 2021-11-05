import csv


class PanelDiscripition:
    elements = [
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
    ]

    elementsForWrite = [
        "IFPANEL",
        "NAME",
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
    ]

    panelType = {
        "0": "ui/pic/Circle.png",
        "1": "ui/pic/Circle.png",
        "2": "ui/pic/Circle.png",
        "3": "ui/pic/Square1.png",
        "4": "ui/pic/Square1.png",
        "5": "ui/pic/Square1.png",
        "6": "ui/pic/Square2.png",
        "7": "ui/pic/Square2.png",
        "8": "ui/pic/Square2.png",
        "9": "ui/pic/SwitchLeftOn.png",
        "10": "ui/pic/SwitchLeftOn.png",
        "11": "ui/pic/SwitchRightOn.png",
        "12": "ui/pic/SwitchRightOn.png",
        "13": "ui/pic/Empty.png",
        "14": "ui/pic/Empty.png",
        "15": "ui/pic/Empty.png",
        "16": "ui/pic/Counter3dw.png",
        "17": "ui/pic/Counter6dw.png",
        "18": "ui/pic/Counter3dg.png",
        "19": "ui/pic/Counter6dg.png"
    }

    PanelColor = {
        "0": "QLabel { background-color : Black;}",
        "1": "QLabel { background-color : Blue;}",
        "2": "QLabel { background-color : Green;}",
        "3": "QLabel { background-color : LightSkyBlue ;}",
        "4": "QLabel { background-color : Red;}",
        "5": "QLabel { background-color : Purple;}",
        "6": "QLabel { background-color : Yellow;}",
        "7": "QLabel { background-color : White;}",
        "8": "QLabel { background-color : LightGray;}",
        "9": "QLabel { background-color : DarkBlue;}",
        "10": "QLabel { background-color : DarkGreen;}",
        "11": "QLabel { background-color : DeepSkyBlue ;}",
        "12": "QLabel { background-color : DarkRed;}",
        "13": "QLabel { background-color : DarkPurple;}",
        "14": "QLabel { background-color : DarkYellow;}",
        "15": "QLabel { background-color : DarkGray;}",
        "16": "QLabel { background-color : Orange;}"
    }

    TextColor = {
        "0": "QLabel { font: bold 14px; color: Black;}",
        "1": "QLabel { font: bold 14px; color: Blue;}",
        "2": "QLabel { font: bold 14px; color: Green;}",
        "3": "QLabel { font: bold 14px; color: LightSkyBlue ;}",
        "4": "QLabel { font: bold 14px; color: Red;}",
        "5": "QLabel { font: bold 14px; color: Purple;}",
        "6": "QLabel { font: bold 14px; color: Yellow;}",
        "7": "QLabel { font: bold 14px; color: White;}",
        "8": "QLabel { font: bold 14px; color: LightGray;}",
        "9": "QLabel { font: bold 14px; color: DarkBlue;}",
        "10": "QLabel { font: bold 14px; color: DarkGreen;}",
        "11": "QLabel { font: bold 14px; color: DeepSkyBlue ;}",
        "12": "QLabel { font: bold 14px; color: DarkRed;}",
        "13": "QLabel { font: bold 14px; color: DarkPurple;}",
        "14": "QLabel { font: bold 14px; color: DarkYellow;}",
        "15": "QLabel { font: bold 14px; color: DarkGray;}",
        "16": "QLabel { font: bold 14px; color: Orange;}"
    }


    color = {
        "Black": "0",
        "Blue": "1",
        "Green": "2",
        "Sky Blue": "3",
        "Red": "4",
        "Purple": "5",
        "Yellow": "6",
        "White": "7",
        "Light Gray": "8",
        "Dark Blue": "9",
        "Dark Green": "10",
        "Dark Sky Blue": "11",
        "Dark Red": "12",
        "Dark Purple": "13",
        "Dark Yellow": "14",
        "Dark Gray": "15",
        "Orange": "16"
    }

    type = {
        "Circle indication light (display only)": "0",
        "Circle indication light (push button)": "1",
        "Circle indication light (push-lock/push-release button)": "2",
        "Square indication light 1 (display only)": "3",
        "Square indication light 1 (push button)": "4",
        "Square indication light 1 (push-lock/push-release button)": "5",
        "Square indication light 2 (display only)": "6",
        "Square indication light 2 (push button)": "7",
        "Square indication light 2 (push-lock/push-release button)": "8",
        "Selector switch (left: ON)": "9",
        "Selector switch (right: ON)": "10",
        "Selector switch (2-point output)": "11",
        "Selector switch (panel operation)": "12",
        "undef1": "13",
        "undef2": "14",
        "undef3": "15",
        "Counter (3-digit display)": "16",
        "Counter (6-digit display)": "17",
        "Preset counter (3-digit display)": "18",
        "Preset counter (6-digit display)": "19"
    }

    input_Type = {
        "None": "0",
        "Signal (numbers are 5-digit)": "1",
        "B-variable (B000 to B099: numbers are 3-digit)": "2",
        "I-variable (I000 to I099: numbers are 3-digit)": "3",
        "Register (M000 to M999: numbers are 3-digit)": "4"
    }

    def __init__(self):
        self.panel = {
            "IFPANEL": "0",
            "NAME": "1",
            "1A": "2",
            "1B": "3",
            "1C": "4",
            "1D": "5",
            "1E": "6",
            "1F": "7",
            "1G": "8",
            "1H": "9",
            "2A": "2",
            "2B": "3",
            "2C": "4",
            "2D": "5",
            "2E": "6",
            "2F": "7",
            "2G": "8",
            "2H": "9",
            "3A": "2",
            "3B": "3",
            "3C": "4",
            "3D": "5",
            "3E": "6",
            "3F": "7",
            "3G": "8",
            "3H": "9",
            "4A": "2",
            "4B": "3",
            "4C": "4",
            "4D": "5",
            "4E": "6",
            "4F": "7",
            "4G": "8",
            "4H": "9"
        }


def readFile(path):
    i = int(0)
    p = {}  # dictionary of Panels

    with open(path, 'r', encoding='utf-8-sig') as csvfile:
        panelreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in panelreader:

            if row[0].find("IFPANEL") != -1:  # first line of new panel
                # Interface panel data: //IFPANEL <N1>
                nP = int(row[0].lstrip("/IFPANEL"))
                p[nP] = PanelDiscripition()
                p[nP].panel["IFPANEL"] = row

            elif row[0].find("NAME") != -1:
                p[nP].panel["NAME"] = row

            else:
                p[nP].panel[row[0]] = row

    return p

def writeFile(path, p):
    i = int(0)
    #print(p[1].panel["1A"])


    with open(path, 'w', encoding='utf-8-sig', newline='') as csvfile:
        panelwriter = csv.writer(csvfile, delimiter=',', quotechar='"')
        for i in range(15):
            for e in PanelDiscripition.elementsForWrite:
                panelwriter.writerow(p[i+1].panel[e])






