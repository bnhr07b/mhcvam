# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mhcvam_infrastructures_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MHCVAMInfrastructuresDialog(object):
    def setupUi(self, MHCVAMInfrastructuresDialog):
        MHCVAMInfrastructuresDialog.setObjectName(_fromUtf8("MHCVAMInfrastructuresDialog"))
        MHCVAMInfrastructuresDialog.resize(811, 426)
        MHCVAMInfrastructuresDialog.setMinimumSize(QtCore.QSize(811, 426))
        MHCVAMInfrastructuresDialog.setMaximumSize(QtCore.QSize(811, 426))
        self.tabWidget = QtGui.QTabWidget(MHCVAMInfrastructuresDialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 811, 361))
        self.tabWidget.setMinimumSize(QtCore.QSize(811, 361))
        self.tabWidget.setMaximumSize(QtCore.QSize(811, 361))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.infraInHazardTab = QtGui.QWidget()
        self.infraInHazardTab.setObjectName(_fromUtf8("infraInHazardTab"))
        self.hazardLayerLabel = QtGui.QLabel(self.infraInHazardTab)
        self.hazardLayerLabel.setGeometry(QtCore.QRect(10, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hazardLayerLabel.setFont(font)
        self.hazardLayerLabel.setAutoFillBackground(False)
        self.hazardLayerLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.hazardLayerLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.hazardLayerLabel.setWordWrap(True)
        self.hazardLayerLabel.setObjectName(_fromUtf8("hazardLayerLabel"))
        self.infraLayerComboBox = gui.QgsMapLayerComboBox(self.infraInHazardTab)
        self.infraLayerComboBox.setGeometry(QtCore.QRect(180, 10, 621, 27))
        self.infraLayerComboBox.setFilters(gui.QgsMapLayerProxyModel.HasGeometry)
        self.infraLayerComboBox.setObjectName(_fromUtf8("infraLayerComboBox"))
        self.outputNameLineEdit = QtGui.QLineEdit(self.infraInHazardTab)
        self.outputNameLineEdit.setGeometry(QtCore.QRect(180, 170, 621, 27))
        self.outputNameLineEdit.setObjectName(_fromUtf8("outputNameLineEdit"))
        self.hazardLevelLabel = QtGui.QLabel(self.infraInHazardTab)
        self.hazardLevelLabel.setGeometry(QtCore.QRect(10, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hazardLevelLabel.setFont(font)
        self.hazardLevelLabel.setAutoFillBackground(False)
        self.hazardLevelLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.hazardLevelLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.hazardLevelLabel.setWordWrap(True)
        self.hazardLevelLabel.setObjectName(_fromUtf8("hazardLevelLabel"))
        self.infraLayerLabel = QtGui.QLabel(self.infraInHazardTab)
        self.infraLayerLabel.setGeometry(QtCore.QRect(10, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.infraLayerLabel.setFont(font)
        self.infraLayerLabel.setAutoFillBackground(False)
        self.infraLayerLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.infraLayerLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.infraLayerLabel.setWordWrap(True)
        self.infraLayerLabel.setObjectName(_fromUtf8("infraLayerLabel"))
        self.summaryCheckBox = QtGui.QCheckBox(self.infraInHazardTab)
        self.summaryCheckBox.setGeometry(QtCore.QRect(10, 230, 401, 22))
        self.summaryCheckBox.setObjectName(_fromUtf8("summaryCheckBox"))
        self.hazardTypeLabel = QtGui.QLabel(self.infraInHazardTab)
        self.hazardTypeLabel.setGeometry(QtCore.QRect(10, 90, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hazardTypeLabel.setFont(font)
        self.hazardTypeLabel.setAutoFillBackground(False)
        self.hazardTypeLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.hazardTypeLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.hazardTypeLabel.setWordWrap(True)
        self.hazardTypeLabel.setObjectName(_fromUtf8("hazardTypeLabel"))
        self.hazardLevelComboBox = QtGui.QComboBox(self.infraInHazardTab)
        self.hazardLevelComboBox.setGeometry(QtCore.QRect(180, 130, 621, 27))
        self.hazardLevelComboBox.setObjectName(_fromUtf8("hazardLevelComboBox"))
        self.hazardLevelComboBox.addItem(_fromUtf8(""))
        self.hazardLevelComboBox.addItem(_fromUtf8(""))
        self.hazardLevelComboBox.addItem(_fromUtf8(""))
        self.hazardLevelComboBox.addItem(_fromUtf8(""))
        self.outputNameLabel = QtGui.QLabel(self.infraInHazardTab)
        self.outputNameLabel.setGeometry(QtCore.QRect(10, 170, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.outputNameLabel.setFont(font)
        self.outputNameLabel.setAutoFillBackground(False)
        self.outputNameLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.outputNameLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.outputNameLabel.setWordWrap(True)
        self.outputNameLabel.setObjectName(_fromUtf8("outputNameLabel"))
        self.infraInHazardButtonBox = QtGui.QDialogButtonBox(self.infraInHazardTab)
        self.infraInHazardButtonBox.setGeometry(QtCore.QRect(10, 290, 791, 32))
        self.infraInHazardButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.infraInHazardButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.infraInHazardButtonBox.setCenterButtons(False)
        self.infraInHazardButtonBox.setObjectName(_fromUtf8("infraInHazardButtonBox"))
        self.hazardLayerComboBox = gui.QgsMapLayerComboBox(self.infraInHazardTab)
        self.hazardLayerComboBox.setGeometry(QtCore.QRect(180, 50, 621, 27))
        self.hazardLayerComboBox.setFilters(gui.QgsMapLayerProxyModel.HasGeometry)
        self.hazardLayerComboBox.setObjectName(_fromUtf8("hazardLayerComboBox"))
        self.hazardTypeComboBox = gui.QgsFieldComboBox(self.infraInHazardTab)
        self.hazardTypeComboBox.setGeometry(QtCore.QRect(180, 90, 621, 27))
        self.hazardTypeComboBox.setObjectName(_fromUtf8("hazardTypeComboBox"))
        self.tabWidget.addTab(self.infraInHazardTab, _fromUtf8(""))
        self.infraInBrgyTab = QtGui.QWidget()
        self.infraInBrgyTab.setObjectName(_fromUtf8("infraInBrgyTab"))
        self.infraInBrgyButtonBox = QtGui.QDialogButtonBox(self.infraInBrgyTab)
        self.infraInBrgyButtonBox.setGeometry(QtCore.QRect(10, 290, 791, 32))
        self.infraInBrgyButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.infraInBrgyButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.infraInBrgyButtonBox.setCenterButtons(False)
        self.infraInBrgyButtonBox.setObjectName(_fromUtf8("infraInBrgyButtonBox"))
        self.infraWithHazardComboBox = gui.QgsMapLayerComboBox(self.infraInBrgyTab)
        self.infraWithHazardComboBox.setGeometry(QtCore.QRect(180, 10, 621, 27))
        self.infraWithHazardComboBox.setFilters(gui.QgsMapLayerProxyModel.HasGeometry)
        self.infraWithHazardComboBox.setObjectName(_fromUtf8("infraWithHazardComboBox"))
        self.infraWithHazardLayer = QtGui.QLabel(self.infraInBrgyTab)
        self.infraWithHazardLayer.setGeometry(QtCore.QRect(10, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.infraWithHazardLayer.setFont(font)
        self.infraWithHazardLayer.setAutoFillBackground(False)
        self.infraWithHazardLayer.setFrameShape(QtGui.QFrame.NoFrame)
        self.infraWithHazardLayer.setFrameShadow(QtGui.QFrame.Plain)
        self.infraWithHazardLayer.setWordWrap(True)
        self.infraWithHazardLayer.setObjectName(_fromUtf8("infraWithHazardLayer"))
        self.hazardTypeLabel_2 = QtGui.QLabel(self.infraInBrgyTab)
        self.hazardTypeLabel_2.setGeometry(QtCore.QRect(10, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hazardTypeLabel_2.setFont(font)
        self.hazardTypeLabel_2.setAutoFillBackground(False)
        self.hazardTypeLabel_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.hazardTypeLabel_2.setFrameShadow(QtGui.QFrame.Plain)
        self.hazardTypeLabel_2.setWordWrap(True)
        self.hazardTypeLabel_2.setObjectName(_fromUtf8("hazardTypeLabel_2"))
        self.brgyLayerLabel = QtGui.QLabel(self.infraInBrgyTab)
        self.brgyLayerLabel.setGeometry(QtCore.QRect(10, 90, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.brgyLayerLabel.setFont(font)
        self.brgyLayerLabel.setAutoFillBackground(False)
        self.brgyLayerLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.brgyLayerLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.brgyLayerLabel.setWordWrap(True)
        self.brgyLayerLabel.setObjectName(_fromUtf8("brgyLayerLabel"))
        self.brgyLayerComboBox = gui.QgsMapLayerComboBox(self.infraInBrgyTab)
        self.brgyLayerComboBox.setGeometry(QtCore.QRect(180, 90, 621, 27))
        self.brgyLayerComboBox.setFilters(gui.QgsMapLayerProxyModel.HasGeometry)
        self.brgyLayerComboBox.setObjectName(_fromUtf8("brgyLayerComboBox"))
        self.brgyNamesLabel = QtGui.QLabel(self.infraInBrgyTab)
        self.brgyNamesLabel.setGeometry(QtCore.QRect(10, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.brgyNamesLabel.setFont(font)
        self.brgyNamesLabel.setAutoFillBackground(False)
        self.brgyNamesLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.brgyNamesLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.brgyNamesLabel.setWordWrap(True)
        self.brgyNamesLabel.setObjectName(_fromUtf8("brgyNamesLabel"))
        self.brgyOutputNameLineEdit = QtGui.QLineEdit(self.infraInBrgyTab)
        self.brgyOutputNameLineEdit.setGeometry(QtCore.QRect(180, 210, 621, 27))
        self.brgyOutputNameLineEdit.setObjectName(_fromUtf8("brgyOutputNameLineEdit"))
        self.brgyOutputNameLabel = QtGui.QLabel(self.infraInBrgyTab)
        self.brgyOutputNameLabel.setGeometry(QtCore.QRect(10, 210, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.brgyOutputNameLabel.setFont(font)
        self.brgyOutputNameLabel.setAutoFillBackground(False)
        self.brgyOutputNameLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.brgyOutputNameLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.brgyOutputNameLabel.setWordWrap(True)
        self.brgyOutputNameLabel.setObjectName(_fromUtf8("brgyOutputNameLabel"))
        self.hazardLeveltoLabelLabel = QtGui.QLabel(self.infraInBrgyTab)
        self.hazardLeveltoLabelLabel.setGeometry(QtCore.QRect(10, 170, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hazardLeveltoLabelLabel.setFont(font)
        self.hazardLeveltoLabelLabel.setAutoFillBackground(False)
        self.hazardLeveltoLabelLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.hazardLeveltoLabelLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.hazardLeveltoLabelLabel.setWordWrap(True)
        self.hazardLeveltoLabelLabel.setObjectName(_fromUtf8("hazardLeveltoLabelLabel"))
        self.hazardLeveltoLabelComboBox = QtGui.QComboBox(self.infraInBrgyTab)
        self.hazardLeveltoLabelComboBox.setGeometry(QtCore.QRect(180, 170, 621, 27))
        self.hazardLeveltoLabelComboBox.setObjectName(_fromUtf8("hazardLeveltoLabelComboBox"))
        self.hazardLeveltoLabelComboBox.addItem(_fromUtf8(""))
        self.hazardLeveltoLabelComboBox.addItem(_fromUtf8(""))
        self.hazardLeveltoLabelComboBox.addItem(_fromUtf8(""))
        self.hazardLeveltoLabelComboBox.addItem(_fromUtf8(""))
        self.hazardTypeComboBox_2 = gui.QgsFieldComboBox(self.infraInBrgyTab)
        self.hazardTypeComboBox_2.setGeometry(QtCore.QRect(180, 50, 621, 27))
        self.hazardTypeComboBox_2.setObjectName(_fromUtf8("hazardTypeComboBox_2"))
        self.brgyNamesComboBox = gui.QgsFieldComboBox(self.infraInBrgyTab)
        self.brgyNamesComboBox.setGeometry(QtCore.QRect(180, 130, 621, 27))
        self.brgyNamesComboBox.setObjectName(_fromUtf8("brgyNamesComboBox"))
        self.labelCheckBox = QtGui.QCheckBox(self.infraInBrgyTab)
        self.labelCheckBox.setGeometry(QtCore.QRect(10, 250, 111, 22))
        self.labelCheckBox.setObjectName(_fromUtf8("labelCheckBox"))
        self.symCheckBox = QtGui.QCheckBox(self.infraInBrgyTab)
        self.symCheckBox.setGeometry(QtCore.QRect(10, 270, 131, 22))
        self.symCheckBox.setObjectName(_fromUtf8("symCheckBox"))
        self.tabWidget.addTab(self.infraInBrgyTab, _fromUtf8(""))
        self.label = QtGui.QLabel(MHCVAMInfrastructuresDialog)
        self.label.setGeometry(QtCore.QRect(10, 370, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(5)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.logopgs = QtGui.QLabel(MHCVAMInfrastructuresDialog)
        self.logopgs.setGeometry(QtCore.QRect(540, 370, 51, 51))
        self.logopgs.setText(_fromUtf8(""))
        self.logopgs.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/mhcvam/img/logos/pgs-logo.png")))
        self.logopgs.setObjectName(_fromUtf8("logopgs"))
        self.logounicef = QtGui.QLabel(MHCVAMInfrastructuresDialog)
        self.logounicef.setGeometry(QtCore.QRect(600, 370, 201, 51))
        self.logounicef.setText(_fromUtf8(""))
        self.logounicef.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/mhcvam/img/logos/unicef-logo.png")))
        self.logounicef.setObjectName(_fromUtf8("logounicef"))

        self.retranslateUi(MHCVAMInfrastructuresDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MHCVAMInfrastructuresDialog)

    def retranslateUi(self, MHCVAMInfrastructuresDialog):
        MHCVAMInfrastructuresDialog.setWindowTitle(_translate("MHCVAMInfrastructuresDialog", "MHCVAMS for LGU", None))
        self.hazardLayerLabel.setText(_translate("MHCVAMInfrastructuresDialog", "Hazard Layer", None))
        self.hazardLevelLabel.setText(_translate("MHCVAMInfrastructuresDialog", "Hazard Level to View", None))
        self.infraLayerLabel.setText(_translate("MHCVAMInfrastructuresDialog", "Infrastructure Layer", None))
        self.summaryCheckBox.setText(_translate("MHCVAMInfrastructuresDialog", "Show Summary Report", None))
        self.hazardTypeLabel.setText(_translate("MHCVAMInfrastructuresDialog", "Hazard Type", None))
        self.hazardLevelComboBox.setItemText(0, _translate("MHCVAMInfrastructuresDialog", "ALL", None))
        self.hazardLevelComboBox.setItemText(1, _translate("MHCVAMInfrastructuresDialog", "Low", None))
        self.hazardLevelComboBox.setItemText(2, _translate("MHCVAMInfrastructuresDialog", "Medium", None))
        self.hazardLevelComboBox.setItemText(3, _translate("MHCVAMInfrastructuresDialog", "High", None))
        self.outputNameLabel.setText(_translate("MHCVAMInfrastructuresDialog", "Output Name (in memory)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.infraInHazardTab), _translate("MHCVAMInfrastructuresDialog", "Infratructures in Hazard", None))
        self.infraWithHazardLayer.setText(_translate("MHCVAMInfrastructuresDialog", "Infrastructure with Hazard", None))
        self.hazardTypeLabel_2.setText(_translate("MHCVAMInfrastructuresDialog", "Hazard Type", None))
        self.brgyLayerLabel.setText(_translate("MHCVAMInfrastructuresDialog", "Barangay Layer", None))
        self.brgyNamesLabel.setText(_translate("MHCVAMInfrastructuresDialog", "Barangay Names Field", None))
        self.brgyOutputNameLabel.setText(_translate("MHCVAMInfrastructuresDialog", "Output Name (in memory)", None))
        self.hazardLeveltoLabelLabel.setText(_translate("MHCVAMInfrastructuresDialog", "Hazard Level", None))
        self.hazardLeveltoLabelComboBox.setItemText(0, _translate("MHCVAMInfrastructuresDialog", "ALL", None))
        self.hazardLeveltoLabelComboBox.setItemText(1, _translate("MHCVAMInfrastructuresDialog", "Low", None))
        self.hazardLeveltoLabelComboBox.setItemText(2, _translate("MHCVAMInfrastructuresDialog", "Medium", None))
        self.hazardLeveltoLabelComboBox.setItemText(3, _translate("MHCVAMInfrastructuresDialog", "High", None))
        self.labelCheckBox.setText(_translate("MHCVAMInfrastructuresDialog", "Add Labels", None))
        self.symCheckBox.setText(_translate("MHCVAMInfrastructuresDialog", "Add Symbology", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.infraInBrgyTab), _translate("MHCVAMInfrastructuresDialog", "Infrastructures in Barangay", None))
        self.label.setText(_translate("MHCVAMInfrastructuresDialog", "<html><head/><body><p><span style=\" font-size:6pt;\">This plugin was made possible due to the efforts of the United Nations Children\'s Fund (UNICEF) and the Philippine Geographical Society (PGS).</span></p></body></html>", None))

from qgis import gui
import resources_rc
