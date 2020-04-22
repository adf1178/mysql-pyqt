from PyQt5 import QtGui, QtCore,QtWidgets
import sys, os


from PyQt5.QtWidgets import QComboBox,QLineEdit,QListWidget,QCheckBox,QListWidgetItem

class ComboCheckBox(QComboBox):
    def __init__(self):  # items==[str,str...]
        super(ComboCheckBox, self).__init__()
        self.items = ["1","2"]
        self.qCheckBox = []
        self.qLineEdit = QLineEdit()
        self.qLineEdit.setReadOnly(True)
        qListWidget = QListWidget()

        self.row_num = len(self.items)
        for i in range(self.row_num):
            self.qCheckBox.append(QCheckBox())
            qItem = QListWidgetItem(qListWidget)
            self.qCheckBox[i].setText(self.items[i])
            qListWidget.setItemWidget(qItem, self.qCheckBox[i])
            self.qCheckBox[i].stateChanged.connect(self.show)

        self.setLineEdit(self.qLineEdit)
        self.setModel(qListWidget.model())
        self.setView(qListWidget)

    def Selectlist(self):
        Outputlist = []
        for i in range(self.row_num):
            if self.qCheckBox[i].isChecked() == True:
                Outputlist.append(self.qCheckBox[i].text())
        return Outputlist

    def show(self):
        show = ''
        self.qLineEdit.setReadOnly(False)
        self.qLineEdit.clear()
        for i in self.Selectlist():
            show += i + ';'
        self.qLineEdit.setText(show)


class myWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow,self).__init__()
        self.setWindowTitle("custom_combobox")
        myQWidget = QtWidgets.QWidget()
        myBoxLayout = QtWidgets.QVBoxLayout()
        myQWidget.setLayout(myBoxLayout)
        self.setCentralWidget(myQWidget)
        self.ComboBox = ComboCheckBox()
        self.ComboBox.setGeometry(QtCore.QRect(43, 11, 200, 70))
        myBoxLayout.addWidget(self.ComboBox)
        self.resize(260,120)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ap = myWindow()
    ap.show()
    sys.exit(app.exec_())