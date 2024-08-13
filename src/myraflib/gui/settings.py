# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormSettings(object):
    def setupUi(self, FormSettings):
        FormSettings.setObjectName("FormSettings")
        FormSettings.resize(385, 118)
        self.gridLayout_2 = QtWidgets.QGridLayout(FormSettings)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(FormSettings)
        self.label.setMinimumSize(QtCore.QSize(101, 0))
        self.label.setMaximumSize(QtCore.QSize(101, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spinBoxDisplayInterval = QtWidgets.QSpinBox(FormSettings)
        self.spinBoxDisplayInterval.setMaximum(10000)
        self.spinBoxDisplayInterval.setProperty("value", 100)
        self.spinBoxDisplayInterval.setObjectName("spinBoxDisplayInterval")
        self.gridLayout.addWidget(self.spinBoxDisplayInterval, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(FormSettings)
        self.label_2.setMinimumSize(QtCore.QSize(101, 0))
        self.label_2.setMaximumSize(QtCore.QSize(101, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.doubleSpinBoxZMag = QtWidgets.QDoubleSpinBox(FormSettings)
        self.doubleSpinBoxZMag.setMinimum(-1e+39)
        self.doubleSpinBoxZMag.setMaximum(1e+39)
        self.doubleSpinBoxZMag.setProperty("value", 25.0)
        self.doubleSpinBoxZMag.setObjectName("doubleSpinBoxZMag")
        self.gridLayout.addWidget(self.doubleSpinBoxZMag, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 2)

        self.retranslateUi(FormSettings)
        QtCore.QMetaObject.connectSlotsByName(FormSettings)

    def retranslateUi(self, FormSettings):
        _translate = QtCore.QCoreApplication.translate
        FormSettings.setWindowTitle(_translate("FormSettings", "Settings"))
        self.label.setText(_translate("FormSettings", "Display Interval"))
        self.label_2.setText(_translate("FormSettings", "ZMag"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormSettings = QtWidgets.QWidget()
    ui = Ui_FormSettings()
    ui.setupUi(FormSettings)
    FormSettings.show()
    sys.exit(app.exec_())
