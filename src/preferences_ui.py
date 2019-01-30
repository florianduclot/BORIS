# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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

class Ui_prefDialog(object):
    def setupUi(self, prefDialog):
        prefDialog.setObjectName(_fromUtf8("prefDialog"))
        prefDialog.setWindowModality(QtCore.Qt.WindowModal)
        prefDialog.resize(596, 525)
        self.verticalLayout_5 = QtGui.QVBoxLayout(prefDialog)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(prefDialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.cbTimeFormat = QtGui.QComboBox(self.tab)
        self.cbTimeFormat.setObjectName(_fromUtf8("cbTimeFormat"))
        self.cbTimeFormat.addItem(_fromUtf8(""))
        self.cbTimeFormat.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cbTimeFormat)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.sbffSpeed = QtGui.QSpinBox(self.tab)
        self.sbffSpeed.setMinimum(0)
        self.sbffSpeed.setMaximum(10000)
        self.sbffSpeed.setProperty("value", 10)
        self.sbffSpeed.setObjectName(_fromUtf8("sbffSpeed"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.sbffSpeed)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.sbRepositionTimeOffset = QtGui.QSpinBox(self.tab)
        self.sbRepositionTimeOffset.setMinimum(-10000)
        self.sbRepositionTimeOffset.setMaximum(10000)
        self.sbRepositionTimeOffset.setProperty("value", -3)
        self.sbRepositionTimeOffset.setObjectName(_fromUtf8("sbRepositionTimeOffset"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.sbRepositionTimeOffset)
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.sbSpeedStep = QtGui.QDoubleSpinBox(self.tab)
        self.sbSpeedStep.setDecimals(1)
        self.sbSpeedStep.setMinimum(0.1)
        self.sbSpeedStep.setMaximum(1.0)
        self.sbSpeedStep.setSingleStep(0.1)
        self.sbSpeedStep.setProperty("value", 0.1)
        self.sbSpeedStep.setObjectName(_fromUtf8("sbSpeedStep"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.sbSpeedStep)
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.sbAutomaticBackup = QtGui.QSpinBox(self.tab)
        self.sbAutomaticBackup.setMinimum(-10000)
        self.sbAutomaticBackup.setMaximum(10000)
        self.sbAutomaticBackup.setProperty("value", 10)
        self.sbAutomaticBackup.setObjectName(_fromUtf8("sbAutomaticBackup"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.sbAutomaticBackup)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_3)
        self.leSeparator = QtGui.QLineEdit(self.tab)
        self.leSeparator.setObjectName(_fromUtf8("leSeparator"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.leSeparator)
        self.cbCloseSameEvent = QtGui.QCheckBox(self.tab)
        self.cbCloseSameEvent.setObjectName(_fromUtf8("cbCloseSameEvent"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.cbCloseSameEvent)
        self.cbConfirmSound = QtGui.QCheckBox(self.tab)
        self.cbConfirmSound.setObjectName(_fromUtf8("cbConfirmSound"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.cbConfirmSound)
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_8)
        self.sbBeepEvery = QtGui.QSpinBox(self.tab)
        self.sbBeepEvery.setObjectName(_fromUtf8("sbBeepEvery"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.sbBeepEvery)
        self.cbAlertNoFocalSubject = QtGui.QCheckBox(self.tab)
        self.cbAlertNoFocalSubject.setObjectName(_fromUtf8("cbAlertNoFocalSubject"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.cbAlertNoFocalSubject)
        self.cbTrackingCursorAboveEvent = QtGui.QCheckBox(self.tab)
        self.cbTrackingCursorAboveEvent.setObjectName(_fromUtf8("cbTrackingCursorAboveEvent"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.cbTrackingCursorAboveEvent)
        self.cbCheckForNewVersion = QtGui.QCheckBox(self.tab)
        self.cbCheckForNewVersion.setObjectName(_fromUtf8("cbCheckForNewVersion"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.LabelRole, self.cbCheckForNewVersion)
        self.cb_pause_before_addevent = QtGui.QCheckBox(self.tab)
        self.cb_pause_before_addevent.setObjectName(_fromUtf8("cb_pause_before_addevent"))
        self.formLayout.setWidget(13, QtGui.QFormLayout.LabelRole, self.cb_pause_before_addevent)
        self.cb_display_subtitles = QtGui.QCheckBox(self.tab)
        self.cb_display_subtitles.setObjectName(_fromUtf8("cb_display_subtitles"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.LabelRole, self.cb_display_subtitles)
        self.verticalLayout.addLayout(self.formLayout)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lbFFmpegPath = QtGui.QLabel(self.tab_2)
        self.lbFFmpegPath.setScaledContents(False)
        self.lbFFmpegPath.setWordWrap(True)
        self.lbFFmpegPath.setObjectName(_fromUtf8("lbFFmpegPath"))
        self.verticalLayout_3.addWidget(self.lbFFmpegPath)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lbFFmpegCacheDir = QtGui.QLabel(self.tab_2)
        self.lbFFmpegCacheDir.setObjectName(_fromUtf8("lbFFmpegCacheDir"))
        self.horizontalLayout_3.addWidget(self.lbFFmpegCacheDir)
        self.leFFmpegCacheDir = QtGui.QLineEdit(self.tab_2)
        self.leFFmpegCacheDir.setObjectName(_fromUtf8("leFFmpegCacheDir"))
        self.horizontalLayout_3.addWidget(self.leFFmpegCacheDir)
        self.pbBrowseFFmpegCacheDir = QtGui.QPushButton(self.tab_2)
        self.pbBrowseFFmpegCacheDir.setObjectName(_fromUtf8("pbBrowseFFmpegCacheDir"))
        self.horizontalLayout_3.addWidget(self.pbBrowseFFmpegCacheDir)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lbFFmpegCacheDirMaxSize = QtGui.QLabel(self.tab_2)
        self.lbFFmpegCacheDirMaxSize.setObjectName(_fromUtf8("lbFFmpegCacheDirMaxSize"))
        self.horizontalLayout_4.addWidget(self.lbFFmpegCacheDirMaxSize)
        self.sbFFmpegCacheDirMaxSize = QtGui.QSpinBox(self.tab_2)
        self.sbFFmpegCacheDirMaxSize.setMaximum(10000)
        self.sbFFmpegCacheDirMaxSize.setSingleStep(10)
        self.sbFFmpegCacheDirMaxSize.setObjectName(_fromUtf8("sbFFmpegCacheDirMaxSize"))
        self.horizontalLayout_4.addWidget(self.sbFFmpegCacheDirMaxSize)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lbResize = QtGui.QLabel(self.tab_3)
        self.lbResize.setWordWrap(True)
        self.lbResize.setObjectName(_fromUtf8("lbResize"))
        self.horizontalLayout_5.addWidget(self.lbResize)
        self.sbFrameResize = QtGui.QSpinBox(self.tab_3)
        self.sbFrameResize.setMaximum(1920)
        self.sbFrameResize.setSingleStep(10)
        self.sbFrameResize.setObjectName(_fromUtf8("sbFrameResize"))
        self.horizontalLayout_5.addWidget(self.sbFrameResize)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_9 = QtGui.QLabel(self.tab_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_8.addWidget(self.label_9)
        self.cbFrameBitmapFormat = QtGui.QComboBox(self.tab_3)
        self.cbFrameBitmapFormat.setObjectName(_fromUtf8("cbFrameBitmapFormat"))
        self.cbFrameBitmapFormat.addItem(_fromUtf8(""))
        self.cbFrameBitmapFormat.addItem(_fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.cbFrameBitmapFormat)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_11 = QtGui.QLabel(self.tab_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_9.addWidget(self.label_11)
        self.sb_fbf_cache_size = QtGui.QSpinBox(self.tab_3)
        self.sb_fbf_cache_size.setMinimum(1)
        self.sb_fbf_cache_size.setMaximum(3600)
        self.sb_fbf_cache_size.setObjectName(_fromUtf8("sb_fbf_cache_size"))
        self.horizontalLayout_9.addWidget(self.sb_fbf_cache_size)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_7 = QtGui.QLabel(self.tab_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_7.addWidget(self.label_7)
        self.cbSpectrogramColorMap = QtGui.QComboBox(self.tab_4)
        self.cbSpectrogramColorMap.setObjectName(_fromUtf8("cbSpectrogramColorMap"))
        self.horizontalLayout_7.addWidget(self.cbSpectrogramColorMap)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_12 = QtGui.QLabel(self.tab_4)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_10.addWidget(self.label_12)
        self.sb_time_interval = QtGui.QSpinBox(self.tab_4)
        self.sb_time_interval.setMinimum(2)
        self.sb_time_interval.setMaximum(360)
        self.sb_time_interval.setProperty("value", 10)
        self.sb_time_interval.setObjectName(_fromUtf8("sb_time_interval"))
        self.horizontalLayout_10.addWidget(self.sb_time_interval)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        spacerItem2 = QtGui.QSpacerItem(20, 319, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout_11.setMargin(0)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_10 = QtGui.QLabel(self.tab_5)
        self.label_10.setOpenExternalLinks(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_10.addWidget(self.label_10)
        self.te_plot_colors = QtGui.QPlainTextEdit(self.tab_5)
        self.te_plot_colors.setObjectName(_fromUtf8("te_plot_colors"))
        self.verticalLayout_10.addWidget(self.te_plot_colors)
        self.pb_reset_colors = QtGui.QPushButton(self.tab_5)
        self.pb_reset_colors.setObjectName(_fromUtf8("pb_reset_colors"))
        self.verticalLayout_10.addWidget(self.pb_reset_colors)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(241, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pb_refresh = QtGui.QPushButton(prefDialog)
        self.pb_refresh.setObjectName(_fromUtf8("pb_refresh"))
        self.horizontalLayout_2.addWidget(self.pb_refresh)
        self.pbCancel = QtGui.QPushButton(prefDialog)
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.horizontalLayout_2.addWidget(self.pbCancel)
        self.pbOK = QtGui.QPushButton(prefDialog)
        self.pbOK.setObjectName(_fromUtf8("pbOK"))
        self.horizontalLayout_2.addWidget(self.pbOK)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.retranslateUi(prefDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(prefDialog)

    def retranslateUi(self, prefDialog):
        prefDialog.setWindowTitle(_translate("prefDialog", "Preferences", None))
        self.label.setText(_translate("prefDialog", "Default project time format", None))
        self.cbTimeFormat.setItemText(0, _translate("prefDialog", "seconds", None))
        self.cbTimeFormat.setItemText(1, _translate("prefDialog", "hh:mm:ss.mss", None))
        self.label_4.setText(_translate("prefDialog", "Fast forward/backward speed (seconds)", None))
        self.label_2.setText(_translate("prefDialog", "Time offset for video/audio reposition (seconds)", None))
        self.label_5.setText(_translate("prefDialog", "Playback speed step value", None))
        self.label_6.setText(_translate("prefDialog", "Automatic backup every (minutes)", None))
        self.label_3.setText(_translate("prefDialog", "Separator for behavioural strings (events export)", None))
        self.leSeparator.setText(_translate("prefDialog", "|", None))
        self.cbCloseSameEvent.setText(_translate("prefDialog", "Close the same current event independently of modifiers", None))
        self.cbConfirmSound.setText(_translate("prefDialog", "Play sound when a key is pressed", None))
        self.label_8.setText(_translate("prefDialog", "Beep every (seconds)", None))
        self.cbAlertNoFocalSubject.setText(_translate("prefDialog", "Alert if focal subject is not set", None))
        self.cbTrackingCursorAboveEvent.setText(_translate("prefDialog", "Tracking cursor above current event", None))
        self.cbCheckForNewVersion.setText(_translate("prefDialog", "Check for new version and news", None))
        self.cb_pause_before_addevent.setText(_translate("prefDialog", "Pause media before \"Add event\" command", None))
        self.cb_display_subtitles.setText(_translate("prefDialog", "Display subtitles", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("prefDialog", "Project", None))
        self.lbFFmpegPath.setText(_translate("prefDialog", "FFmpeg path:", None))
        self.lbFFmpegCacheDir.setText(_translate("prefDialog", "FFmpeg cache directory", None))
        self.pbBrowseFFmpegCacheDir.setText(_translate("prefDialog", "...", None))
        self.lbFFmpegCacheDirMaxSize.setText(_translate("prefDialog", "FFmpeg cache directory max size (Mb)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("prefDialog", "FFmpeg framework", None))
        self.lbResize.setText(_translate("prefDialog", "Resize frame (horizontal number of pixels). The aspect ratio will be maintained", None))
        self.label_9.setText(_translate("prefDialog", "Frame bitmap format (JPG: Low quality  PNG: High quality)", None))
        self.cbFrameBitmapFormat.setItemText(0, _translate("prefDialog", "JPG", None))
        self.cbFrameBitmapFormat.setItemText(1, _translate("prefDialog", "PNG", None))
        self.label_11.setText(_translate("prefDialog", "Cache size (in seconds)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("prefDialog", "Frame-by-frame mode", None))
        self.label_7.setText(_translate("prefDialog", "Color map", None))
        self.label_12.setText(_translate("prefDialog", "Default time interval (s)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("prefDialog", "Spectrogram", None))
        self.label_10.setText(_translate("prefDialog", "List of colors to be used in plot. See <a href=\"https://matplotlib.org/api/colors_api.html\">matplotlib colors</a>", None))
        self.pb_reset_colors.setText(_translate("prefDialog", "Reset colors to default", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("prefDialog", "Plot colors", None))
        self.pb_refresh.setText(_translate("prefDialog", "Refresh", None))
        self.pbCancel.setText(_translate("prefDialog", "Cancel", None))
        self.pbOK.setText(_translate("prefDialog", "OK", None))

