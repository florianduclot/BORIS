# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'observation.ui'
#
# Created: Tue Dec 15 14:23:01 2015
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(602, 632)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.leObservationId = QtGui.QLineEdit(Form)
        self.leObservationId.setObjectName(_fromUtf8("leObservationId"))
        self.horizontalLayout_2.addWidget(self.leObservationId)
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_2.addWidget(self.label_8)
        self.dteDate = QtGui.QDateTimeEdit(Form)
        self.dteDate.setCalendarPopup(True)
        self.dteDate.setObjectName(_fromUtf8("dteDate"))
        self.horizontalLayout_2.addWidget(self.dteDate)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_2.addWidget(self.label_9)
        self.teDescription = QtGui.QPlainTextEdit(Form)
        self.teDescription.setMaximumSize(QtCore.QSize(16777215, 50))
        self.teDescription.setObjectName(_fromUtf8("teDescription"))
        self.verticalLayout_2.addWidget(self.teDescription)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.twIndepVariables = QtGui.QTableWidget(Form)
        self.twIndepVariables.setObjectName(_fromUtf8("twIndepVariables"))
        self.twIndepVariables.setColumnCount(3)
        self.twIndepVariables.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.twIndepVariables.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.twIndepVariables.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.twIndepVariables.setHorizontalHeaderItem(2, item)
        self.verticalLayout_3.addWidget(self.twIndepVariables)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.lbTimeOffset = QtGui.QLabel(Form)
        self.lbTimeOffset.setObjectName(_fromUtf8("lbTimeOffset"))
        self.horizontalLayout_6.addWidget(self.lbTimeOffset)
        self.rbAdd = QtGui.QRadioButton(Form)
        self.rbAdd.setChecked(True)
        self.rbAdd.setObjectName(_fromUtf8("rbAdd"))
        self.horizontalLayout_6.addWidget(self.rbAdd)
        self.rbSubstract = QtGui.QRadioButton(Form)
        self.rbSubstract.setObjectName(_fromUtf8("rbSubstract"))
        self.horizontalLayout_6.addWidget(self.rbSubstract)
        self.leTimeOffset = QtGui.QLineEdit(Form)
        self.leTimeOffset.setObjectName(_fromUtf8("leTimeOffset"))
        self.horizontalLayout_6.addWidget(self.leTimeOffset)
        self.teTimeOffset = QtGui.QTimeEdit(Form)
        self.teTimeOffset.setObjectName(_fromUtf8("teTimeOffset"))
        self.horizontalLayout_6.addWidget(self.teTimeOffset)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.tabProjectType = QtGui.QTabWidget(Form)
        self.tabProjectType.setEnabled(True)
        self.tabProjectType.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabProjectType.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabProjectType.setUsesScrollButtons(False)
        self.tabProjectType.setDocumentMode(False)
        self.tabProjectType.setTabsClosable(False)
        self.tabProjectType.setMovable(False)
        self.tabProjectType.setObjectName(_fromUtf8("tabProjectType"))
        self.tabVideo = QtGui.QWidget()
        self.tabVideo.setObjectName(_fromUtf8("tabVideo"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tabVideo)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_5 = QtGui.QLabel(self.tabVideo)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_7.addWidget(self.label_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lwVideo = QtGui.QListWidget(self.tabVideo)
        self.lwVideo.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.lwVideo.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.lwVideo.setObjectName(_fromUtf8("lwVideo"))
        self.horizontalLayout_4.addWidget(self.lwVideo)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pbAddVideo = QtGui.QPushButton(self.tabVideo)
        self.pbAddVideo.setObjectName(_fromUtf8("pbAddVideo"))
        self.verticalLayout.addWidget(self.pbAddVideo)
        self.pbRemoveVideo = QtGui.QPushButton(self.tabVideo)
        self.pbRemoveVideo.setObjectName(_fromUtf8("pbRemoveVideo"))
        self.verticalLayout.addWidget(self.pbRemoveVideo)
        self.pbAddMediaFromDir = QtGui.QPushButton(self.tabVideo)
        self.pbAddMediaFromDir.setObjectName(_fromUtf8("pbAddMediaFromDir"))
        self.verticalLayout.addWidget(self.pbAddMediaFromDir)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.cbVisualizeSpectrogram = QtGui.QCheckBox(self.tabVideo)
        self.cbVisualizeSpectrogram.setObjectName(_fromUtf8("cbVisualizeSpectrogram"))
        self.verticalLayout_7.addWidget(self.cbVisualizeSpectrogram)
        self.cbCloseCurrentBehaviorsBetweenVideo = QtGui.QCheckBox(self.tabVideo)
        self.cbCloseCurrentBehaviorsBetweenVideo.setObjectName(_fromUtf8("cbCloseCurrentBehaviorsBetweenVideo"))
        self.verticalLayout_7.addWidget(self.cbCloseCurrentBehaviorsBetweenVideo)
        self.label_2 = QtGui.QLabel(self.tabVideo)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_7.addWidget(self.label_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lwVideo_2 = QtGui.QListWidget(self.tabVideo)
        self.lwVideo_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.lwVideo_2.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.lwVideo_2.setObjectName(_fromUtf8("lwVideo_2"))
        self.horizontalLayout_5.addWidget(self.lwVideo_2)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.pbAddVideo_2 = QtGui.QPushButton(self.tabVideo)
        self.pbAddVideo_2.setObjectName(_fromUtf8("pbAddVideo_2"))
        self.verticalLayout_6.addWidget(self.pbAddVideo_2)
        self.pbRemoveVideo_2 = QtGui.QPushButton(self.tabVideo)
        self.pbRemoveVideo_2.setObjectName(_fromUtf8("pbRemoveVideo_2"))
        self.verticalLayout_6.addWidget(self.pbRemoveVideo_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.lbTimeOffset_2 = QtGui.QLabel(self.tabVideo)
        self.lbTimeOffset_2.setObjectName(_fromUtf8("lbTimeOffset_2"))
        self.horizontalLayout_7.addWidget(self.lbTimeOffset_2)
        self.rbEarlier = QtGui.QRadioButton(self.tabVideo)
        self.rbEarlier.setChecked(True)
        self.rbEarlier.setObjectName(_fromUtf8("rbEarlier"))
        self.horizontalLayout_7.addWidget(self.rbEarlier)
        self.rbLater = QtGui.QRadioButton(self.tabVideo)
        self.rbLater.setObjectName(_fromUtf8("rbLater"))
        self.horizontalLayout_7.addWidget(self.rbLater)
        self.leTimeOffset_2 = QtGui.QLineEdit(self.tabVideo)
        self.leTimeOffset_2.setObjectName(_fromUtf8("leTimeOffset_2"))
        self.horizontalLayout_7.addWidget(self.leTimeOffset_2)
        self.teTimeOffset_2 = QtGui.QTimeEdit(self.tabVideo)
        self.teTimeOffset_2.setObjectName(_fromUtf8("teTimeOffset_2"))
        self.horizontalLayout_7.addWidget(self.teTimeOffset_2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.tabProjectType.addTab(self.tabVideo, _fromUtf8(""))
        self.tabLive = QtGui.QWidget()
        self.tabLive.setObjectName(_fromUtf8("tabLive"))
        self.tabProjectType.addTab(self.tabLive, _fromUtf8(""))
        self.verticalLayout_9.addWidget(self.tabProjectType)
        self.verticalLayout_3.addLayout(self.verticalLayout_9)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbMediaAnalysis = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbMediaAnalysis.setFont(font)
        self.lbMediaAnalysis.setObjectName(_fromUtf8("lbMediaAnalysis"))
        self.horizontalLayout.addWidget(self.lbMediaAnalysis)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pbCancel = QtGui.QPushButton(Form)
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.horizontalLayout.addWidget(self.pbCancel)
        self.pbOK = QtGui.QPushButton(Form)
        self.pbOK.setObjectName(_fromUtf8("pbOK"))
        self.horizontalLayout.addWidget(self.pbOK)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        self.tabProjectType.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "New observation", None))
        self.label.setText(_translate("Form", "Observation id", None))
        self.label_8.setText(_translate("Form", "Date", None))
        self.dteDate.setDisplayFormat(_translate("Form", "yyyy-MM-dd hh:mm", None))
        self.label_9.setText(_translate("Form", "Description", None))
        self.label_3.setText(_translate("Form", "Independent variables", None))
        item = self.twIndepVariables.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Variable", None))
        item = self.twIndepVariables.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Type", None))
        item = self.twIndepVariables.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Value", None))
        self.lbTimeOffset.setText(_translate("Form", "Time offset", None))
        self.rbAdd.setText(_translate("Form", "Add", None))
        self.rbSubstract.setText(_translate("Form", "Substract", None))
        self.leTimeOffset.setText(_translate("Form", "0", None))
        self.teTimeOffset.setDisplayFormat(_translate("Form", "hh:mm:ss.zzz", None))
        self.label_5.setText(_translate("Form", "Media file paths", None))
        self.pbAddVideo.setText(_translate("Form", "Add media", None))
        self.pbRemoveVideo.setText(_translate("Form", "Remove media", None))
        self.pbAddMediaFromDir.setText(_translate("Form", "Add all media\n"
"from directory", None))
        self.cbVisualizeSpectrogram.setText(_translate("Form", "Visualize spectrogram", None))
        self.cbCloseCurrentBehaviorsBetweenVideo.setText(_translate("Form", "Close current behaviors between videos", None))
        self.label_2.setText(_translate("Form", "Media file paths for second player (will be played simultaneously)", None))
        self.pbAddVideo_2.setText(_translate("Form", "Add media", None))
        self.pbRemoveVideo_2.setText(_translate("Form", "Remove media", None))
        self.lbTimeOffset_2.setText(_translate("Form", "Time offset for second player", None))
        self.rbEarlier.setText(_translate("Form", "Earlier", None))
        self.rbLater.setText(_translate("Form", "Later", None))
        self.leTimeOffset_2.setText(_translate("Form", "0", None))
        self.teTimeOffset_2.setDisplayFormat(_translate("Form", "hh:mm:ss.zzz", None))
        self.tabProjectType.setTabText(self.tabProjectType.indexOf(self.tabVideo), _translate("Form", "Media", None))
        self.tabProjectType.setTabText(self.tabProjectType.indexOf(self.tabLive), _translate("Form", "Live", None))
        self.lbMediaAnalysis.setText(_translate("Form", "BORIS", None))
        self.pbCancel.setText(_translate("Form", "Cancel", None))
        self.pbOK.setText(_translate("Form", "OK", None))

