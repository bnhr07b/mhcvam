# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mhcvam_household_dialog.ui'
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

class Ui_MHCVAMHouseholdDialog(object):
    def setupUi(self, MHCVAMHouseholdDialog):
        MHCVAMHouseholdDialog.setObjectName(_fromUtf8("MHCVAMHouseholdDialog"))
        MHCVAMHouseholdDialog.resize(823, 568)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MHCVAMHouseholdDialog.sizePolicy().hasHeightForWidth())
        MHCVAMHouseholdDialog.setSizePolicy(sizePolicy)
        MHCVAMHouseholdDialog.setMinimumSize(QtCore.QSize(823, 565))
        MHCVAMHouseholdDialog.setMaximumSize(QtCore.QSize(823, 568))
        self.tabWidget = QtGui.QTabWidget(MHCVAMHouseholdDialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 821, 501))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.hhSelectTab = QtGui.QWidget()
        self.hhSelectTab.setObjectName(_fromUtf8("hhSelectTab"))
        self.selectHazardLevelComboBox = QtGui.QComboBox(self.hhSelectTab)
        self.selectHazardLevelComboBox.setGeometry(QtCore.QRect(180, 130, 631, 27))
        self.selectHazardLevelComboBox.setObjectName(_fromUtf8("selectHazardLevelComboBox"))
        self.selectHazardLevelComboBox.addItem(_fromUtf8(""))
        self.selectHazardLevelComboBox.addItem(_fromUtf8(""))
        self.selectHazardLevelComboBox.addItem(_fromUtf8(""))
        self.selectHazardLevelComboBox.addItem(_fromUtf8(""))
        self.selectHazardLevelComboBox.addItem(_fromUtf8(""))
        self.selectHazardComboBox = gui.QgsMapLayerComboBox(self.hhSelectTab)
        self.selectHazardComboBox.setGeometry(QtCore.QRect(180, 50, 631, 27))
        self.selectHazardComboBox.setFilters(gui.QgsMapLayerProxyModel.HasGeometry)
        self.selectHazardComboBox.setObjectName(_fromUtf8("selectHazardComboBox"))
        self.selectHazardLevelLabel = QtGui.QLabel(self.hhSelectTab)
        self.selectHazardLevelLabel.setGeometry(QtCore.QRect(10, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectHazardLevelLabel.setFont(font)
        self.selectHazardLevelLabel.setAutoFillBackground(False)
        self.selectHazardLevelLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.selectHazardLevelLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.selectHazardLevelLabel.setWordWrap(True)
        self.selectHazardLevelLabel.setObjectName(_fromUtf8("selectHazardLevelLabel"))
        self.selectSummaryCheckBox = QtGui.QCheckBox(self.hhSelectTab)
        self.selectSummaryCheckBox.setGeometry(QtCore.QRect(10, 230, 401, 22))
        self.selectSummaryCheckBox.setObjectName(_fromUtf8("selectSummaryCheckBox"))
        self.selectOutputNameLineEdit = QtGui.QLineEdit(self.hhSelectTab)
        self.selectOutputNameLineEdit.setGeometry(QtCore.QRect(180, 170, 631, 27))
        self.selectOutputNameLineEdit.setObjectName(_fromUtf8("selectOutputNameLineEdit"))
        self.selectHazardTypeComboBox = gui.QgsFieldComboBox(self.hhSelectTab)
        self.selectHazardTypeComboBox.setGeometry(QtCore.QRect(180, 90, 631, 27))
        self.selectHazardTypeComboBox.setObjectName(_fromUtf8("selectHazardTypeComboBox"))
        self.selectOutputNameLabel = QtGui.QLabel(self.hhSelectTab)
        self.selectOutputNameLabel.setGeometry(QtCore.QRect(10, 170, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectOutputNameLabel.setFont(font)
        self.selectOutputNameLabel.setAutoFillBackground(False)
        self.selectOutputNameLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.selectOutputNameLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.selectOutputNameLabel.setWordWrap(True)
        self.selectOutputNameLabel.setObjectName(_fromUtf8("selectOutputNameLabel"))
        self.selectHHButtonBox = QtGui.QDialogButtonBox(self.hhSelectTab)
        self.selectHHButtonBox.setGeometry(QtCore.QRect(520, 430, 291, 32))
        self.selectHHButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.selectHHButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.selectHHButtonBox.setCenterButtons(False)
        self.selectHHButtonBox.setObjectName(_fromUtf8("selectHHButtonBox"))
        self.selectHHComboBox = gui.QgsMapLayerComboBox(self.hhSelectTab)
        self.selectHHComboBox.setGeometry(QtCore.QRect(180, 10, 631, 27))
        self.selectHHComboBox.setFilters(gui.QgsMapLayerProxyModel.HasGeometry)
        self.selectHHComboBox.setObjectName(_fromUtf8("selectHHComboBox"))
        self.selectHazardTypeLabel = QtGui.QLabel(self.hhSelectTab)
        self.selectHazardTypeLabel.setGeometry(QtCore.QRect(10, 90, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectHazardTypeLabel.setFont(font)
        self.selectHazardTypeLabel.setAutoFillBackground(False)
        self.selectHazardTypeLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.selectHazardTypeLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.selectHazardTypeLabel.setWordWrap(True)
        self.selectHazardTypeLabel.setObjectName(_fromUtf8("selectHazardTypeLabel"))
        self.selectHHLabel = QtGui.QLabel(self.hhSelectTab)
        self.selectHHLabel.setGeometry(QtCore.QRect(10, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectHHLabel.setFont(font)
        self.selectHHLabel.setAutoFillBackground(False)
        self.selectHHLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.selectHHLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.selectHHLabel.setWordWrap(True)
        self.selectHHLabel.setObjectName(_fromUtf8("selectHHLabel"))
        self.selectHazardLabel = QtGui.QLabel(self.hhSelectTab)
        self.selectHazardLabel.setGeometry(QtCore.QRect(10, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectHazardLabel.setFont(font)
        self.selectHazardLabel.setAutoFillBackground(False)
        self.selectHazardLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.selectHazardLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.selectHazardLabel.setWordWrap(True)
        self.selectHazardLabel.setObjectName(_fromUtf8("selectHazardLabel"))
        self.tabWidget.addTab(self.hhSelectTab, _fromUtf8(""))
        self.hhQueryTab = QtGui.QWidget()
        self.hhQueryTab.setObjectName(_fromUtf8("hhQueryTab"))
        self.queryHHButtonBox = QtGui.QDialogButtonBox(self.hhQueryTab)
        self.queryHHButtonBox.setGeometry(QtCore.QRect(10, 430, 801, 32))
        self.queryHHButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.queryHHButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Reset)
        self.queryHHButtonBox.setCenterButtons(False)
        self.queryHHButtonBox.setObjectName(_fromUtf8("queryHHButtonBox"))
        self.queryHHLabel = QtGui.QLabel(self.hhQueryTab)
        self.queryHHLabel.setGeometry(QtCore.QRect(10, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.queryHHLabel.setFont(font)
        self.queryHHLabel.setAutoFillBackground(False)
        self.queryHHLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.queryHHLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.queryHHLabel.setWordWrap(True)
        self.queryHHLabel.setObjectName(_fromUtf8("queryHHLabel"))
        self.queryHHComboBox = gui.QgsMapLayerComboBox(self.hhQueryTab)
        self.queryHHComboBox.setGeometry(QtCore.QRect(180, 10, 631, 27))
        self.queryHHComboBox.setFilters(gui.QgsMapLayerProxyModel.HasGeometry)
        self.queryHHComboBox.setObjectName(_fromUtf8("queryHHComboBox"))
        self.queryFieldLabel = QtGui.QLabel(self.hhQueryTab)
        self.queryFieldLabel.setGeometry(QtCore.QRect(10, 90, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.queryFieldLabel.setFont(font)
        self.queryFieldLabel.setAutoFillBackground(False)
        self.queryFieldLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.queryFieldLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.queryFieldLabel.setWordWrap(True)
        self.queryFieldLabel.setObjectName(_fromUtf8("queryFieldLabel"))
        self.queryAgencyComboBox = QtGui.QComboBox(self.hhQueryTab)
        self.queryAgencyComboBox.setGeometry(QtCore.QRect(180, 50, 631, 27))
        self.queryAgencyComboBox.setObjectName(_fromUtf8("queryAgencyComboBox"))
        self.queryAgencyLabel = QtGui.QLabel(self.hhQueryTab)
        self.queryAgencyLabel.setGeometry(QtCore.QRect(10, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.queryAgencyLabel.setFont(font)
        self.queryAgencyLabel.setAutoFillBackground(False)
        self.queryAgencyLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.queryAgencyLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.queryAgencyLabel.setWordWrap(True)
        self.queryAgencyLabel.setObjectName(_fromUtf8("queryAgencyLabel"))
        self.queryFieldComboBox = QtGui.QComboBox(self.hhQueryTab)
        self.queryFieldComboBox.setGeometry(QtCore.QRect(180, 90, 531, 27))
        self.queryFieldComboBox.setObjectName(_fromUtf8("queryFieldComboBox"))
        self.queryFieldAdd = QtGui.QPushButton(self.hhQueryTab)
        self.queryFieldAdd.setGeometry(QtCore.QRect(720, 90, 91, 27))
        self.queryFieldAdd.setObjectName(_fromUtf8("queryFieldAdd"))
        self.queryFunctionComboBox = QtGui.QComboBox(self.hhQueryTab)
        self.queryFunctionComboBox.setGeometry(QtCore.QRect(180, 250, 531, 27))
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
        self.queryFunctionLabel = QtGui.QLabel(self.hhQueryTab)
        self.queryFunctionLabel.setGeometry(QtCore.QRect(10, 250, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.queryFunctionLabel.setFont(font)
        self.queryFunctionLabel.setAutoFillBackground(False)
        self.queryFunctionLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.queryFunctionLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.queryFunctionLabel.setWordWrap(True)
        self.queryFunctionLabel.setObjectName(_fromUtf8("queryFunctionLabel"))
        self.queryFunctionAdd = QtGui.QPushButton(self.hhQueryTab)
        self.queryFunctionAdd.setGeometry(QtCore.QRect(720, 250, 91, 27))
        self.queryFunctionAdd.setObjectName(_fromUtf8("queryFunctionAdd"))
        self.queryTextEdit = QtGui.QPlainTextEdit(self.hhQueryTab)
        self.queryTextEdit.setGeometry(QtCore.QRect(10, 310, 801, 111))
        self.queryTextEdit.setObjectName(_fromUtf8("queryTextEdit"))
        self.queryLabel = QtGui.QLabel(self.hhQueryTab)
        self.queryLabel.setGeometry(QtCore.QRect(10, 280, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.queryLabel.setFont(font)
        self.queryLabel.setAutoFillBackground(False)
        self.queryLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.queryLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.queryLabel.setWordWrap(True)
        self.queryLabel.setObjectName(_fromUtf8("queryLabel"))
        self.uniqueValuesButton = QtGui.QPushButton(self.hhQueryTab)
        self.uniqueValuesButton.setGeometry(QtCore.QRect(10, 130, 161, 27))
        self.uniqueValuesButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.uniqueValuesButton.setObjectName(_fromUtf8("uniqueValuesButton"))
        self.uniqueValuesListWidget = QtGui.QListWidget(self.hhQueryTab)
        self.uniqueValuesListWidget.setGeometry(QtCore.QRect(180, 130, 531, 111))
        self.uniqueValuesListWidget.setObjectName(_fromUtf8("uniqueValuesListWidget"))
        self.queryValueAdd = QtGui.QPushButton(self.hhQueryTab)
        self.queryValueAdd.setGeometry(QtCore.QRect(720, 130, 91, 27))
        self.queryValueAdd.setObjectName(_fromUtf8("queryValueAdd"))
        self.tabWidget.addTab(self.hhQueryTab, _fromUtf8(""))
        self.hhSummarizeTab = QtGui.QWidget()
        self.hhSummarizeTab.setObjectName(_fromUtf8("hhSummarizeTab"))
        self.summHHButtonBox = QtGui.QDialogButtonBox(self.hhSummarizeTab)
        self.summHHButtonBox.setGeometry(QtCore.QRect(10, 430, 801, 32))
        self.summHHButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.summHHButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.summHHButtonBox.setCenterButtons(False)
        self.summHHButtonBox.setObjectName(_fromUtf8("summHHButtonBox"))
        self.summHHLabel = QtGui.QLabel(self.hhSummarizeTab)
        self.summHHLabel.setGeometry(QtCore.QRect(10, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.summHHLabel.setFont(font)
        self.summHHLabel.setAutoFillBackground(False)
        self.summHHLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.summHHLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.summHHLabel.setWordWrap(True)
        self.summHHLabel.setObjectName(_fromUtf8("summHHLabel"))
        self.summHHComboBox = gui.QgsMapLayerComboBox(self.hhSummarizeTab)
        self.summHHComboBox.setGeometry(QtCore.QRect(180, 10, 631, 27))
        self.summHHComboBox.setFilters(gui.QgsMapLayerProxyModel.HasGeometry)
        self.summHHComboBox.setObjectName(_fromUtf8("summHHComboBox"))
        self.brgyFieldLabel = QtGui.QLabel(self.hhSummarizeTab)
        self.brgyFieldLabel.setGeometry(QtCore.QRect(10, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.brgyFieldLabel.setFont(font)
        self.brgyFieldLabel.setAutoFillBackground(False)
        self.brgyFieldLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.brgyFieldLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.brgyFieldLabel.setWordWrap(True)
        self.brgyFieldLabel.setObjectName(_fromUtf8("brgyFieldLabel"))
        self.brgyFieldComboBox = gui.QgsFieldComboBox(self.hhSummarizeTab)
        self.brgyFieldComboBox.setGeometry(QtCore.QRect(180, 90, 631, 27))
        self.brgyFieldComboBox.setObjectName(_fromUtf8("brgyFieldComboBox"))
        self.fieldComboBox = QtGui.QComboBox(self.hhSummarizeTab)
        self.fieldComboBox.setGeometry(QtCore.QRect(180, 170, 631, 27))
        self.fieldComboBox.setObjectName(_fromUtf8("fieldComboBox"))
        self.agencyLabel = QtGui.QLabel(self.hhSummarizeTab)
        self.agencyLabel.setGeometry(QtCore.QRect(10, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.agencyLabel.setFont(font)
        self.agencyLabel.setAutoFillBackground(False)
        self.agencyLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.agencyLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.agencyLabel.setWordWrap(True)
        self.agencyLabel.setObjectName(_fromUtf8("agencyLabel"))
        self.agencyComboBox = QtGui.QComboBox(self.hhSummarizeTab)
        self.agencyComboBox.setGeometry(QtCore.QRect(180, 130, 631, 27))
        self.agencyComboBox.setObjectName(_fromUtf8("agencyComboBox"))
        self.fieldLabel = QtGui.QLabel(self.hhSummarizeTab)
        self.fieldLabel.setGeometry(QtCore.QRect(10, 170, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fieldLabel.setFont(font)
        self.fieldLabel.setAutoFillBackground(False)
        self.fieldLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.fieldLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.fieldLabel.setWordWrap(True)
        self.fieldLabel.setObjectName(_fromUtf8("fieldLabel"))
        self.statLabel = QtGui.QLabel(self.hhSummarizeTab)
        self.statLabel.setGeometry(QtCore.QRect(10, 210, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statLabel.setFont(font)
        self.statLabel.setAutoFillBackground(False)
        self.statLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.statLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.statLabel.setWordWrap(True)
        self.statLabel.setObjectName(_fromUtf8("statLabel"))
        self.statComboBox = QtGui.QComboBox(self.hhSummarizeTab)
        self.statComboBox.setGeometry(QtCore.QRect(180, 210, 631, 27))
        self.statComboBox.setObjectName(_fromUtf8("statComboBox"))
        self.statComboBox.addItem(_fromUtf8(""))
        self.statComboBox.addItem(_fromUtf8(""))
        self.statComboBox.addItem(_fromUtf8(""))
        self.statComboBox.addItem(_fromUtf8(""))
        self.statComboBox.addItem(_fromUtf8(""))
        self.statComboBox.addItem(_fromUtf8(""))
        self.statComboBox.addItem(_fromUtf8(""))
        self.statComboBox.addItem(_fromUtf8(""))
        self.statComboBox.addItem(_fromUtf8(""))
        self.summHHBrgyLabel = QtGui.QLabel(self.hhSummarizeTab)
        self.summHHBrgyLabel.setGeometry(QtCore.QRect(10, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.summHHBrgyLabel.setFont(font)
        self.summHHBrgyLabel.setAutoFillBackground(False)
        self.summHHBrgyLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.summHHBrgyLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.summHHBrgyLabel.setWordWrap(True)
        self.summHHBrgyLabel.setObjectName(_fromUtf8("summHHBrgyLabel"))
        self.summHHBrgyComboBox = gui.QgsMapLayerComboBox(self.hhSummarizeTab)
        self.summHHBrgyComboBox.setGeometry(QtCore.QRect(180, 50, 631, 27))
        self.summHHBrgyComboBox.setFilters(gui.QgsMapLayerProxyModel.HasGeometry)
        self.summHHBrgyComboBox.setObjectName(_fromUtf8("summHHBrgyComboBox"))
        self.labelCheckBox = QtGui.QCheckBox(self.hhSummarizeTab)
        self.labelCheckBox.setGeometry(QtCore.QRect(10, 250, 151, 22))
        self.labelCheckBox.setObjectName(_fromUtf8("labelCheckBox"))
        self.symCheckBox = QtGui.QCheckBox(self.hhSummarizeTab)
        self.symCheckBox.setGeometry(QtCore.QRect(10, 280, 151, 22))
        self.symCheckBox.setObjectName(_fromUtf8("symCheckBox"))
        self.tabWidget.addTab(self.hhSummarizeTab, _fromUtf8(""))
        self.logounicef = QtGui.QLabel(MHCVAMHouseholdDialog)
        self.logounicef.setGeometry(QtCore.QRect(610, 510, 201, 51))
        self.logounicef.setText(_fromUtf8(""))
        self.logounicef.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/mhcvam/img/logos/unicef-logo.png")))
        self.logounicef.setObjectName(_fromUtf8("logounicef"))
        self.logopgs = QtGui.QLabel(MHCVAMHouseholdDialog)
        self.logopgs.setGeometry(QtCore.QRect(550, 510, 51, 51))
        self.logopgs.setText(_fromUtf8(""))
        self.logopgs.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/mhcvam/img/logos/pgs-logo.png")))
        self.logopgs.setObjectName(_fromUtf8("logopgs"))
        self.label = QtGui.QLabel(MHCVAMHouseholdDialog)
        self.label.setGeometry(QtCore.QRect(10, 510, 201, 51))
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

        self.retranslateUi(MHCVAMHouseholdDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MHCVAMHouseholdDialog)

    def retranslateUi(self, MHCVAMHouseholdDialog):
        MHCVAMHouseholdDialog.setWindowTitle(_translate("MHCVAMHouseholdDialog", "MHCVAMS for LGU", None))
        self.selectHazardLevelComboBox.setItemText(0, _translate("MHCVAMHouseholdDialog", "ALL", None))
        self.selectHazardLevelComboBox.setItemText(1, _translate("MHCVAMHouseholdDialog", "Low", None))
        self.selectHazardLevelComboBox.setItemText(2, _translate("MHCVAMHouseholdDialog", "Medium", None))
        self.selectHazardLevelComboBox.setItemText(3, _translate("MHCVAMHouseholdDialog", "High", None))
        self.selectHazardLevelComboBox.setItemText(4, _translate("MHCVAMHouseholdDialog", "Very High", None))
        self.selectHazardLevelLabel.setText(_translate("MHCVAMHouseholdDialog", "Hazard Level to View", None))
        self.selectSummaryCheckBox.setText(_translate("MHCVAMHouseholdDialog", "Show Summary Report", None))
        self.selectOutputNameLabel.setText(_translate("MHCVAMHouseholdDialog", "Output Name [in memory] (max 10 characters)", None))
        self.selectHazardTypeLabel.setText(_translate("MHCVAMHouseholdDialog", "Hazard Type", None))
        self.selectHHLabel.setText(_translate("MHCVAMHouseholdDialog", "Household Layer", None))
        self.selectHazardLabel.setText(_translate("MHCVAMHouseholdDialog", "Hazard Layer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hhSelectTab), _translate("MHCVAMHouseholdDialog", "Select", None))
        self.queryHHLabel.setText(_translate("MHCVAMHouseholdDialog", "Household Layer", None))
        self.queryFieldLabel.setText(_translate("MHCVAMHouseholdDialog", "Field", None))
        self.queryAgencyLabel.setText(_translate("MHCVAMHouseholdDialog", "Limit By Agency", None))
        self.queryFieldAdd.setText(_translate("MHCVAMHouseholdDialog", "ADD", None))
        self.queryFunctionComboBox.setItemText(0, _translate("MHCVAMHouseholdDialog", "equal to", None))
        self.queryFunctionComboBox.setItemText(1, _translate("MHCVAMHouseholdDialog", "not equal to", None))
        self.queryFunctionComboBox.setItemText(2, _translate("MHCVAMHouseholdDialog", "greater than", None))
        self.queryFunctionComboBox.setItemText(3, _translate("MHCVAMHouseholdDialog", "less than", None))
        self.queryFunctionComboBox.setItemText(4, _translate("MHCVAMHouseholdDialog", "greater than or equal to", None))
        self.queryFunctionComboBox.setItemText(5, _translate("MHCVAMHouseholdDialog", "less than or equal to", None))
        self.queryFunctionComboBox.setItemText(6, _translate("MHCVAMHouseholdDialog", "NOT NULL", None))
        self.queryFunctionComboBox.setItemText(7, _translate("MHCVAMHouseholdDialog", "AND", None))
        self.queryFunctionComboBox.setItemText(8, _translate("MHCVAMHouseholdDialog", "OR", None))
        self.queryFunctionLabel.setText(_translate("MHCVAMHouseholdDialog", "Function", None))
        self.queryFunctionAdd.setText(_translate("MHCVAMHouseholdDialog", "ADD", None))
        self.queryLabel.setText(_translate("MHCVAMHouseholdDialog", "Expression", None))
        self.uniqueValuesButton.setText(_translate("MHCVAMHouseholdDialog", "GET UNIQUE VALUES", None))
        self.queryValueAdd.setText(_translate("MHCVAMHouseholdDialog", "ADD", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hhQueryTab), _translate("MHCVAMHouseholdDialog", "Query", None))
        self.summHHLabel.setText(_translate("MHCVAMHouseholdDialog", "Household Layer with Indicators", None))
        self.brgyFieldLabel.setText(_translate("MHCVAMHouseholdDialog", "Admin Boundaries Name Field", None))
        self.agencyLabel.setText(_translate("MHCVAMHouseholdDialog", "Limit By Agency", None))
        self.fieldLabel.setText(_translate("MHCVAMHouseholdDialog", "Field to Summarize", None))
        self.statLabel.setText(_translate("MHCVAMHouseholdDialog", "Summary Statistic", None))
        self.statComboBox.setItemText(0, _translate("MHCVAMHouseholdDialog", "SUM", None))
        self.statComboBox.setItemText(1, _translate("MHCVAMHouseholdDialog", "MEAN", None))
        self.statComboBox.setItemText(2, _translate("MHCVAMHouseholdDialog", "MIN", None))
        self.statComboBox.setItemText(3, _translate("MHCVAMHouseholdDialog", "MAX", None))
        self.statComboBox.setItemText(4, _translate("MHCVAMHouseholdDialog", "PERCENTAGE", None))
        self.statComboBox.setItemText(5, _translate("MHCVAMHouseholdDialog", "COUNT [LOW]", None))
        self.statComboBox.setItemText(6, _translate("MHCVAMHouseholdDialog", "COUNT [MEDIUM]", None))
        self.statComboBox.setItemText(7, _translate("MHCVAMHouseholdDialog", "COUNT [HIGH]", None))
        self.statComboBox.setItemText(8, _translate("MHCVAMHouseholdDialog", "COUNT [VERY HIGH]", None))
        self.summHHBrgyLabel.setText(_translate("MHCVAMHouseholdDialog", "Admin Boundaries", None))
        self.labelCheckBox.setText(_translate("MHCVAMHouseholdDialog", "Add Labels", None))
        self.symCheckBox.setText(_translate("MHCVAMHouseholdDialog", "Add Symbology", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hhSummarizeTab), _translate("MHCVAMHouseholdDialog", "Summarize", None))
        self.label.setText(_translate("MHCVAMHouseholdDialog", "<html><head/><body><p><span style=\" font-size:6pt;\">This plugin was made possible due to the efforts of the United Nations Children\'s Fund (UNICEF) and the Philippine Geographical Society (PGS).</span></p></body></html>", None))

from qgis import gui
import resources_rc
