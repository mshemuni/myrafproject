# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rotate.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormRotate(object):
    def setupUi(self, FormRotate):
        FormRotate.setObjectName("FormRotate")
        FormRotate.resize(792, 643)
        self.gridLayout_3 = QtWidgets.QGridLayout(FormRotate)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(FormRotate)
        self.groupBox.setMinimumSize(QtCore.QSize(437, 592))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(FormRotate)
        self.groupBox_2.setMinimumSize(QtCore.QSize(331, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(331, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidgetAmount = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidgetAmount.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetAmount.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidgetAmount.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetAmount.setObjectName("tableWidgetAmount")
        self.tableWidgetAmount.setColumnCount(2)
        self.tableWidgetAmount.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAmount.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAmount.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.tableWidgetAmount, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(519, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButtonGo = QtWidgets.QPushButton(FormRotate)
        self.pushButtonGo.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButtonGo.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButtonGo.setObjectName("pushButtonGo")
        self.gridLayout_2.addWidget(self.pushButtonGo, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 2)

        self.retranslateUi(FormRotate)
        QtCore.QMetaObject.connectSlotsByName(FormRotate)

    def retranslateUi(self, FormRotate):
        _translate = QtCore.QCoreApplication.translate
        FormRotate.setWindowTitle(_translate("FormRotate", "Rotate"))
        self.groupBox.setTitle(_translate("FormRotate", "Image"))
        self.groupBox_2.setTitle(_translate("FormRotate", "Amount"))
        item = self.tableWidgetAmount.horizontalHeaderItem(0)
        item.setText(_translate("FormRotate", "Image"))
        item = self.tableWidgetAmount.horizontalHeaderItem(1)
        item.setText(_translate("FormRotate", "Angle"))
        self.pushButtonGo.setText(_translate("FormRotate", ":go"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormRotate = QtWidgets.QWidget()
    ui = Ui_FormRotate()
    ui.setupUi(FormRotate)
    FormRotate.show()
    sys.exit(app.exec_())
