# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_qgis_auth_sample_dialog.ui'
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

class Ui_AuthSampleDialog(object):
    def setupUi(self, AuthSampleDialog):
        AuthSampleDialog.setObjectName(_fromUtf8("AuthSampleDialog"))
        AuthSampleDialog.resize(900, 720)
        self.verticalLayout = QtGui.QVBoxLayout(AuthSampleDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(AuthSampleDialog)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.backButton = QtGui.QToolButton(self.frame)
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.horizontalLayout.addWidget(self.backButton)
        self.forwardButton = QtGui.QToolButton(self.frame)
        self.forwardButton.setObjectName(_fromUtf8("forwardButton"))
        self.horizontalLayout.addWidget(self.forwardButton)
        self.reloadButton = QtGui.QToolButton(self.frame)
        self.reloadButton.setObjectName(_fromUtf8("reloadButton"))
        self.horizontalLayout.addWidget(self.reloadButton)
        self.stopButton = QtGui.QToolButton(self.frame)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.horizontalLayout.addWidget(self.stopButton)
        self.comboBox = QtGui.QComboBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox.setEditable(True)
        self.comboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox.setMinimumContentsLength(200)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frameMsgBar = QtGui.QFrame(AuthSampleDialog)
        self.frameMsgBar.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameMsgBar.setFrameShadow(QtGui.QFrame.Raised)
        self.frameMsgBar.setObjectName(_fromUtf8("frameMsgBar"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frameMsgBar)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2.addWidget(self.frameMsgBar)
        self.vertSplitter = QtGui.QSplitter(AuthSampleDialog)
        self.vertSplitter.setOrientation(QtCore.Qt.Vertical)
        self.vertSplitter.setChildrenCollapsible(False)
        self.vertSplitter.setObjectName(_fromUtf8("vertSplitter"))
        self.webView = QtWebKit.QWebView(self.vertSplitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.vertSplitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_2.addWidget(self.vertSplitter)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.frame1 = QtGui.QFrame(AuthSampleDialog)
        self.frame1.setMaximumSize(QtCore.QSize(16777215, 24))
        self.frame1.setObjectName(_fromUtf8("frame1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.clearButton = QtGui.QToolButton(self.frame1)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout_2.addWidget(self.clearButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnAuthSelect = QtGui.QToolButton(self.frame1)
        self.btnAuthSelect.setObjectName(_fromUtf8("btnAuthSelect"))
        self.horizontalLayout_2.addWidget(self.btnAuthSelect)
        self.horizontalFrame = QtGui.QFrame(self.frame1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalFrame.setObjectName(_fromUtf8("horizontalFrame"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.leAuthId = QtGui.QLineEdit(self.horizontalFrame)
        self.leAuthId.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leAuthId.setObjectName(_fromUtf8("leAuthId"))
        self.horizontalLayout_3.addWidget(self.leAuthId)
        self.btnClearID = QtGui.QToolButton(self.horizontalFrame)
        self.btnClearID.setObjectName(_fromUtf8("btnClearID"))
        self.horizontalLayout_3.addWidget(self.btnClearID)
        self.horizontalLayout_2.addWidget(self.horizontalFrame)
        self.verticalLayout.addWidget(self.frame1)

        self.retranslateUi(AuthSampleDialog)
        QtCore.QMetaObject.connectSlotsByName(AuthSampleDialog)

    def retranslateUi(self, AuthSampleDialog):
        AuthSampleDialog.setWindowTitle(_translate("AuthSampleDialog", "Dialog", None))
        self.backButton.setText(_translate("AuthSampleDialog", "<", None))
        self.forwardButton.setText(_translate("AuthSampleDialog", ">", None))
        self.reloadButton.setText(_translate("AuthSampleDialog", "Reload", None))
        self.stopButton.setText(_translate("AuthSampleDialog", "Stop", None))
        self.clearButton.setText(_translate("AuthSampleDialog", "Clear log", None))
        self.btnAuthSelect.setText(_translate("AuthSampleDialog", "Auth ID select (prior to connection)", None))
        self.btnClearID.setText(_translate("AuthSampleDialog", "x", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AuthSampleDialog = QtGui.QDialog()
    ui = Ui_AuthSampleDialog()
    ui.setupUi(AuthSampleDialog)
    AuthSampleDialog.show()
    sys.exit(app.exec_())

