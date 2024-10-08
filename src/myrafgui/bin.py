# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bin.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormBin(object):
    def setupUi(self, FormBin):
        FormBin.setObjectName("FormBin")
        FormBin.resize(288, 127)
        self.gridLayout_3 = QtWidgets.QGridLayout(FormBin)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButtonGo = QtWidgets.QPushButton(FormBin)
        self.pushButtonGo.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButtonGo.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButtonGo.setObjectName("pushButtonGo")
        self.gridLayout_3.addWidget(self.pushButtonGo, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(519, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(FormBin)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 72))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setMinimumSize(QtCore.QSize(0, 18))
        self.label.setMaximumSize(QtCore.QSize(16, 18))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spinBoxXAmount = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBoxXAmount.setMinimumSize(QtCore.QSize(100, 25))
        self.spinBoxXAmount.setMaximumSize(QtCore.QSize(16777215, 25))
        self.spinBoxXAmount.setMinimum(1)
        self.spinBoxXAmount.setMaximum(65535)
        self.spinBoxXAmount.setObjectName("spinBoxXAmount")
        self.gridLayout.addWidget(self.spinBoxXAmount, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_2)
        self.line.setMinimumSize(QtCore.QSize(0, 27))
        self.line.setMaximumSize(QtCore.QSize(16, 27))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setMinimumSize(QtCore.QSize(0, 18))
        self.label_2.setMaximumSize(QtCore.QSize(16, 18))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.spinBoxYAmount = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBoxYAmount.setEnabled(True)
        self.spinBoxYAmount.setMinimumSize(QtCore.QSize(100, 25))
        self.spinBoxYAmount.setMaximumSize(QtCore.QSize(16777215, 25))
        self.spinBoxYAmount.setMinimum(1)
        self.spinBoxYAmount.setMaximum(65535)
        self.spinBoxYAmount.setObjectName("spinBoxYAmount")
        self.gridLayout.addWidget(self.spinBoxYAmount, 0, 4, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 2)

        self.retranslateUi(FormBin)
        QtCore.QMetaObject.connectSlotsByName(FormBin)

    def retranslateUi(self, FormBin):
        _translate = QtCore.QCoreApplication.translate
        FormBin.setWindowTitle(_translate("FormBin", "Bin"))
        self.pushButtonGo.setText(_translate("FormBin", ":go"))
        self.groupBox_2.setTitle(_translate("FormBin", "Amount"))
        self.label.setText(_translate("FormBin", "X"))
        self.label_2.setText(_translate("FormBin", "Y"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormBin = QtWidgets.QWidget()
    ui = Ui_FormBin()
    ui.setupUi(FormBin)
    FormBin.show()
    sys.exit(app.exec_())
