# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statics.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormStatics(object):
    def setupUi(self, FormStatics):
        FormStatics.setObjectName("FormStatics")
        FormStatics.resize(818, 221)
        self.gridLayout = QtWidgets.QGridLayout(FormStatics)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidgetStats = QtWidgets.QTableWidget(FormStatics)
        self.tableWidgetStats.setMinimumSize(QtCore.QSize(800, 0))
        self.tableWidgetStats.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetStats.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidgetStats.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetStats.setObjectName("tableWidgetStats")
        self.tableWidgetStats.setColumnCount(8)
        self.tableWidgetStats.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetStats.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetStats.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetStats.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetStats.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetStats.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetStats.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetStats.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetStats.setHorizontalHeaderItem(7, item)
        self.gridLayout.addWidget(self.tableWidgetStats, 0, 0, 1, 1)

        self.retranslateUi(FormStatics)
        QtCore.QMetaObject.connectSlotsByName(FormStatics)

    def retranslateUi(self, FormStatics):
        _translate = QtCore.QCoreApplication.translate
        FormStatics.setWindowTitle(_translate("FormStatics", "Statics"))
        item = self.tableWidgetStats.horizontalHeaderItem(0)
        item.setText(_translate("FormStatics", "File"))
        item = self.tableWidgetStats.horizontalHeaderItem(1)
        item.setText(_translate("FormStatics", "Size"))
        item = self.tableWidgetStats.horizontalHeaderItem(2)
        item.setText(_translate("FormStatics", "Width"))
        item = self.tableWidgetStats.horizontalHeaderItem(3)
        item.setText(_translate("FormStatics", "Height"))
        item = self.tableWidgetStats.horizontalHeaderItem(4)
        item.setText(_translate("FormStatics", "Min"))
        item = self.tableWidgetStats.horizontalHeaderItem(5)
        item.setText(_translate("FormStatics", "Mean"))
        item = self.tableWidgetStats.horizontalHeaderItem(6)
        item.setText(_translate("FormStatics", "Std"))
        item = self.tableWidgetStats.horizontalHeaderItem(7)
        item.setText(_translate("FormStatics", "Max"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormStatics = QtWidgets.QWidget()
    ui = Ui_FormStatics()
    ui.setupUi(FormStatics)
    FormStatics.show()
    sys.exit(app.exec_())
