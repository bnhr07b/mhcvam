# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mhcvam_barangay_dialog.ui'
#
# Created: Mon Mar 20 02:09:24 2017
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_MHCVAMBarangayDialog(object):
    def setupUi(self, MHCVAMBarangayDialog):
        MHCVAMBarangayDialog.setObjectName(_fromUtf8("MHCVAMBarangayDialog"))
        MHCVAMBarangayDialog.resize(432, 385)
        MHCVAMBarangayDialog.setMinimumSize(QtCore.QSize(432, 385))
        MHCVAMBarangayDialog.setMaximumSize(QtCore.QSize(432, 385))
        self.tabWidget = QtGui.QTabWidget(MHCVAMBarangayDialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 431, 381))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.brgyQueryTab = QtGui.QWidget()
        self.brgyQueryTab.setObjectName(_fromUtf8("brgyQueryTab"))
        self.queryBrgyButtonBox = QtGui.QDialogButtonBox(self.brgyQueryTab)
        self.queryBrgyButtonBox.setGeometry(QtCore.QRect(10, 310, 411, 32))
        self.queryBrgyButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.queryBrgyButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Reset)
        self.queryBrgyButtonBox.setCenterButtons(False)
        self.queryBrgyButtonBox.setObjectName(_fromUtf8("queryBrgyButtonBox"))
        self.queryBrgyLabel = QtGui.QLabel(self.brgyQueryTab)
        self.queryBrgyLabel.setGeometry(QtCore.QRect(10, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.queryBrgyLabel.setFont(font)
        self.queryBrgyLabel.setAutoFillBackground(False)
        self.queryBrgyLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.queryBrgyLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.queryBrgyLabel.setWordWrap(True)
        self.queryBrgyLabel.setObjectName(_fromUtf8("queryBrgyLabel"))
        self.queryBrgyComboBox = gui.QgsMapLayerComboBox(self.brgyQueryTab)
        self.queryBrgyComboBox.setGeometry(QtCore.QRect(180, 10, 241, 27))
        self.queryBrgyComboBox.setFilters(gui.QgsMapLayerProxyModel.HasGeometry)
        self.queryBrgyComboBox.setObjectName(_fromUtf8("queryBrgyComboBox"))
        self.queryFieldComboBox = QtGui.QComboBox(self.brgyQueryTab)
        self.queryFieldComboBox.setGeometry(QtCore.QRect(180, 90, 171, 27))
        self.queryFieldComboBox.setObjectName(_fromUtf8("queryFieldComboBox"))
        self.queryTextEdit = QtGui.QPlainTextEdit(self.brgyQueryTab)
        self.queryTextEdit.setGeometry(QtCore.QRect(10, 210, 411, 91))
        self.queryTextEdit.setObjectName(_fromUtf8("queryTextEdit"))
        self.queryFunctionAdd = QtGui.QPushButton(self.brgyQueryTab)
        self.queryFunctionAdd.setGeometry(QtCore.QRect(360, 130, 61, 27))
        self.queryFunctionAdd.setObjectName(_fromUtf8("queryFunctionAdd"))
        self.queryAgencyComboBox = QtGui.QComboBox(self.brgyQueryTab)
        self.queryAgencyComboBox.setGeometry(QtCore.QRect(180, 50, 241, 27))
        self.queryAgencyComboBox.setObjectName(_fromUtf8("queryAgencyComboBox"))
        self.queryFieldLabel = QtGui.QLabel(self.brgyQueryTab)
        self.queryFieldLabel.setGeometry(QtCore.QRect(10, 90, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.queryFieldLabel.setFont(font)
        self.queryFieldLabel.setAutoFillBackground(False)
        self.queryFieldLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.queryFieldLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.queryFieldLabel.setWordWrap(True)
        self.queryFieldLabel.setObjectName(_fromUtf8("queryFieldLabel"))
        self.queryFunctionLabel = QtGui.QLabel(self.brgyQueryTab)
        self.queryFunctionLabel.setGeometry(QtCore.QRect(10, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.queryFunctionLabel.setFont(font)
        self.queryFunctionLabel.setAutoFillBackground(False)
        self.queryFunctionLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.queryFunctionLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.queryFunctionLabel.setWordWrap(True)
        self.queryFunctionLabel.setObjectName(_fromUtf8("queryFunctionLabel"))
        self.queryFieldAdd = QtGui.QPushButton(self.brgyQueryTab)
        self.queryFieldAdd.setGeometry(QtCore.QRect(360, 90, 61, 27))
        self.queryFieldAdd.setObjectName(_fromUtf8("queryFieldAdd"))
        self.queryAgencyLabel = QtGui.QLabel(self.brgyQueryTab)
        self.queryAgencyLabel.setGeometry(QtCore.QRect(10, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.queryAgencyLabel.setFont(font)
        self.queryAgencyLabel.setAutoFillBackground(False)
        self.queryAgencyLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.queryAgencyLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.queryAgencyLabel.setWordWrap(True)
        self.queryAgencyLabel.setObjectName(_fromUtf8("queryAgencyLabel"))
        self.queryLabel = QtGui.QLabel(self.brgyQueryTab)
        self.queryLabel.setGeometry(QtCore.QRect(10, 180, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.queryLabel.setFont(font)
        self.queryLabel.setAutoFillBackground(False)
        self.queryLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.queryLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.queryLabel.setWordWrap(True)
        self.queryLabel.setObjectName(_fromUtf8("queryLabel"))
        self.queryFunctionComboBox = QtGui.QComboBox(self.brgyQueryTab)
        self.queryFunctionComboBox.setGeometry(QtCore.QRect(180, 130, 171, 27))
        self.queryFunctionComboBox.setObjectName(_fromUtf8("queryFunctionComboBox"))
        self.queryFunctionComboBox.addItem(_fromUtf8(""))
        self.queryFunctionComboBox.addItem(_fromUtf8(""))
        self.queryFunctionComboBox.addItem(_fromUtf8(""))
        self.queryFunctionComboBox.addItem(_fromUtf8(""))
        self.queryFunctionComboBox.addItem(_fromUtf8(""))
        self.queryFunctionComboBox.addItem(_fromUtf8(""))
        self.queryFunctionComboBox.addItem(_fromUtf8(""))
        self.queryFunctionComboBox.addItem(_fromUtf8(""))
        self.queryFunctionComboBox.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.brgyQueryTab, _fromUtf8(""))
        self.brgySummarizeTab = QtGui.QWidget()
        self.brgySummarizeTab.setObjectName(_fromUtf8("brgySummarizeTab"))
        self.summBrgyButtonBox = QtGui.QDialogButtonBox(self.brgySummarizeTab)
        self.summBrgyButtonBox.setGeometry(QtCore.QRect(10, 300, 411, 32))
        self.summBrgyButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.summBrgyButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.summBrgyButtonBox.setCenterButtons(False)
        self.summBrgyButtonBox.setObjectName(_fromUtf8("summBrgyButtonBox"))
        self.summBrgyLabel = QtGui.QLabel(self.brgySummarizeTab)
        self.summBrgyLabel.setGeometry(QtCore.QRect(10, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.summBrgyLabel.setFont(font)
        self.summBrgyLabel.setAutoFillBackground(False)
        self.summBrgyLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.summBrgyLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.summBrgyLabel.setWordWrap(True)
        self.summBrgyLabel.setObjectName(_fromUtf8("summBrgyLabel"))
        self.summBrgyComboBox = gui.QgsMapLayerComboBox(self.brgySummarizeTab)
        self.summBrgyComboBox.setGeometry(QtCore.QRect(180, 10, 241, 27))
        self.summBrgyComboBox.setFilters(gui.QgsMapLayerProxyModel.HasGeometry)
        self.summBrgyComboBox.setObjectName(_fromUtf8("summBrgyComboBox"))
        self.muniFieldLabel = QtGui.QLabel(self.brgySummarizeTab)
        self.muniFieldLabel.setGeometry(QtCore.QRect(10, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.muniFieldLabel.setFont(font)
        self.muniFieldLabel.setAutoFillBackground(False)
        self.muniFieldLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.muniFieldLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.muniFieldLabel.setWordWrap(True)
        self.muniFieldLabel.setObjectName(_fromUtf8("muniFieldLabel"))
        self.muniFieldComboBox = gui.QgsFieldComboBox(self.brgySummarizeTab)
        self.muniFieldComboBox.setGeometry(QtCore.QRect(180, 50, 241, 27))
        self.muniFieldComboBox.setObjectName(_fromUtf8("muniFieldComboBox"))
        self.fieldComboBox = QtGui.QComboBox(self.brgySummarizeTab)
        self.fieldComboBox.setGeometry(QtCore.QRect(180, 130, 241, 27))
        self.fieldComboBox.setObjectName(_fromUtf8("fieldComboBox"))
        self.agencyLabel = QtGui.QLabel(self.brgySummarizeTab)
        self.agencyLabel.setGeometry(QtCore.QRect(10, 90, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.agencyLabel.setFont(font)
        self.agencyLabel.setAutoFillBackground(False)
        self.agencyLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.agencyLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.agencyLabel.setWordWrap(True)
        self.agencyLabel.setObjectName(_fromUtf8("agencyLabel"))
        self.agencyComboBox = QtGui.QComboBox(self.brgySummarizeTab)
        self.agencyComboBox.setGeometry(QtCore.QRect(180, 90, 241, 27))
        self.agencyComboBox.setObjectName(_fromUtf8("agencyComboBox"))
        self.fieldLabel = QtGui.QLabel(self.brgySummarizeTab)
        self.fieldLabel.setGeometry(QtCore.QRect(10, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fieldLabel.setFont(font)
        self.fieldLabel.setAutoFillBackground(False)
        self.fieldLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.fieldLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.fieldLabel.setWordWrap(True)
        self.fieldLabel.setObjectName(_fromUtf8("fieldLabel"))
        self.statLabel = QtGui.QLabel(self.brgySummarizeTab)
        self.statLabel.setGeometry(QtCore.QRect(10, 170, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statLabel.setFont(font)
        self.statLabel.setAutoFillBackground(False)
        self.statLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.statLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.statLabel.setWordWrap(True)
        self.statLabel.setObjectName(_fromUtf8("statLabel"))
        self.statComboBox = QtGui.QComboBox(self.brgySummarizeTab)
        self.statComboBox.setGeometry(QtCore.QRect(180, 170, 241, 27))
        self.statComboBox.setObjectName(_fromUtf8("statComboBox"))
        self.statComboBox.addItem(_fromUtf8(""))
        self.statComboBox.addItem(_fromUtf8(""))
        self.statComboBox.addItem(_fromUtf8(""))
        self.statComboBox.addItem(_fromUtf8(""))
        self.statComboBox.addItem(_fromUtf8(""))
        self.labelCheckBox = QtGui.QCheckBox(self.brgySummarizeTab)
        self.labelCheckBox.setGeometry(QtCore.QRect(10, 230, 151, 22))
        self.labelCheckBox.setObjectName(_fromUtf8("labelCheckBox"))
        self.symCheckBox = QtGui.QCheckBox(self.brgySummarizeTab)
        self.symCheckBox.setGeometry(QtCore.QRect(10, 250, 151, 22))
        self.symCheckBox.setObjectName(_fromUtf8("symCheckBox"))
        self.tabWidget.addTab(self.brgySummarizeTab, _fromUtf8(""))

        self.retranslateUi(MHCVAMBarangayDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MHCVAMBarangayDialog)

    def retranslateUi(self, MHCVAMBarangayDialog):
        MHCVAMBarangayDialog.setWindowTitle(_translate("MHCVAMBarangayDialog", "MHCVAMS for LGU", None))
        self.queryBrgyLabel.setText(_translate("MHCVAMBarangayDialog", "Barangay Layer", None))
        self.queryFunctionAdd.setText(_translate("MHCVAMBarangayDialog", "ADD", None))
        self.queryFieldLabel.setText(_translate("MHCVAMBarangayDialog", "Field", None))
        self.queryFunctionLabel.setText(_translate("MHCVAMBarangayDialog", "Function", None))
        self.queryFieldAdd.setText(_translate("MHCVAMBarangayDialog", "ADD", None))
        self.queryAgencyLabel.setText(_translate("MHCVAMBarangayDialog", "Limit By Agency", None))
        self.queryLabel.setText(_translate("MHCVAMBarangayDialog", "Expression", None))
        self.queryFunctionComboBox.setItemText(0, _translate("MHCVAMBarangayDialog", "equal to", None))
        self.queryFunctionComboBox.setItemText(1, _translate("MHCVAMBarangayDialog", "not equal to", None))
        self.queryFunctionComboBox.setItemText(2, _translate("MHCVAMBarangayDialog", "greater than", None))
        self.queryFunctionComboBox.setItemText(3, _translate("MHCVAMBarangayDialog", "less than", None))
        self.queryFunctionComboBox.setItemText(4, _translate("MHCVAMBarangayDialog", "greater than or equal to", None))
        self.queryFunctionComboBox.setItemText(5, _translate("MHCVAMBarangayDialog", "less than or equal to", None))
        self.queryFunctionComboBox.setItemText(6, _translate("MHCVAMBarangayDialog", "NOT NULL", None))
        self.queryFunctionComboBox.setItemText(7, _translate("MHCVAMBarangayDialog", "AND", None))
        self.queryFunctionComboBox.setItemText(8, _translate("MHCVAMBarangayDialog", "OR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.brgyQueryTab), _translate("MHCVAMBarangayDialog", "Query", None))
        self.summBrgyLabel.setText(_translate("MHCVAMBarangayDialog", "Barangay Layer with Indicators", None))
        self.muniFieldLabel.setText(_translate("MHCVAMBarangayDialog", "City/Municipality Field", None))
        self.agencyLabel.setText(_translate("MHCVAMBarangayDialog", "Limit By Agency", None))
        self.fieldLabel.setText(_translate("MHCVAMBarangayDialog", "Field to Summarize", None))
        self.statLabel.setText(_translate("MHCVAMBarangayDialog", "Summary Statistic", None))
        self.statComboBox.setItemText(0, _translate("MHCVAMBarangayDialog", "SUM", None))
        self.statComboBox.setItemText(1, _translate("MHCVAMBarangayDialog", "MEAN", None))
        self.statComboBox.setItemText(2, _translate("MHCVAMBarangayDialog", "MIN", None))
        self.statComboBox.setItemText(3, _translate("MHCVAMBarangayDialog", "MAX", None))
        self.statComboBox.setItemText(4, _translate("MHCVAMBarangayDialog", "PERCENTAGE", None))
        self.labelCheckBox.setText(_translate("MHCVAMBarangayDialog", "Add Labels", None))
        self.symCheckBox.setText(_translate("MHCVAMBarangayDialog", "Add Symbology", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.brgySummarizeTab), _translate("MHCVAMBarangayDialog", "Summarize", None))

from qgis import gui
