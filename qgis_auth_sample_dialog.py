# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AuthSampleDialog

 Sample dialog for testing authentication system selector widget
                             -------------------
        begin                : 2016-07-11
        copyright            : (C) 2016  by
                               Larry Shaffer/Boundless Spatial Inc.
        email                : lshaffer@boundlessgeo.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from PyQt4.QtWebKit import *

import resources_rc

# from PyQt4 import uic
# FormClass, _ = uic.loadUiType(os.path.join(
#     os.path.dirname(__file__), 'qgis_auth_sample_dialog.ui'))

from ui_qgis_auth_sample_dialog import Ui_AuthSampleDialog as FormClass

BUTTON_BKGRD = "background-color: rgb(185, 216, 255);"


# noinspection PyPep8Naming,PyArgumentList
class AuthSampleDialog(QDialog, FormClass):

    def __init__(self, parent=None, qgis_iface=None):
        """Constructor."""
        super(AuthSampleDialog, self).__init__(parent)
        self.iface = qgis_iface

        self.loaded = False
        self.reply = None

        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        # self.msgbar = QgsMessageBar(self)
        # self.frameMsgBar.layout().addWidget(self.msgbar)

        self.comboBox.lineEdit().setAlignment(Qt.AlignLeft)
        url_list = [
            "http://127.0.0.1",
            "http://localhost",
            "http://boundless.test:8080",
            "http://boundless.test:8080/geoserver/web/",
            "https://boundless.test:8443",
            "https://boundless.test:8443/geoserver/web/",
            "https://qgis.boundless.com",
            "http://www.google.com",
            "http://boundless.test:8080/geoserver/opengeo/wms?"
            "service=WMS&version=1.1.0"
            "&request=GetMap&layers=opengeo:countries&styles="
            "&bbox=-180.0,-89.99892578124998,"
            "180.00000000000003,83.59960937500006"
            "&width=768&height=370&srs=EPSG:4326&format=application/openlayers",
            "https://boundless.test:8443/geoserver/opengeo/wms?"
            "service=WMS&version=1.1.0"
            "&request=GetMap&layers=opengeo:countries&styles="
            "&bbox=-180.0,-89.99892578124998,"
            "180.00000000000003,83.59960937500006"
            "&width=768&height=370&srs=EPSG:4326&format=application/openlayers",
        ]
        self.comboBox.addItems(url_list)

        self.setWebPage()

        self.webView.linkClicked[QUrl].connect(self.loadQUrl)
        self.webView.urlChanged[QUrl].connect(self.setLocation)
        self.webView.titleChanged.connect(self.updateTitle)

        # these don't work with a side-loaded (i.e. setContent) web view
        self.backButton.clicked.connect(self.webView.back)
        self.forwardButton.clicked.connect(self.webView.forward)

        self.reloadButton.clicked.connect(self.webView.reload)
        self.stopButton.clicked.connect(self.webView.stop)

        self.comboBox.lineEdit().returnPressed.connect(self.enterUrl)
        self.comboBox.activated[str].connect(self.loadUrl)
        self.clearButton.clicked.connect(self.clearLog)

        self.resize(800, 600)

    @pyqtSlot(str)
    def updateTitle(self, title):
        self.setWindowTitle(title)

    @pyqtSlot("QUrl")
    def setLocation(self, url):
        self.comboBox.lineEdit().setText(url.toString())
        self.backButton.setEnabled(self.webView.history().canGoBack())
        self.backButton.setStyleSheet(
            BUTTON_BKGRD if self.webView.history().canGoBack() else "")
        self.forwardButton.setEnabled(self.webView.history().canGoForward())
        self.forwardButton.setStyleSheet(
            BUTTON_BKGRD if self.webView.history().canGoForward() else "")

    @pyqtSlot(str)
    def appendLog(self, msg):
        self.plainTextEdit.appendPlainText(msg)

    @pyqtSlot()
    def clearLog(self):
        self.plainTextEdit.clear()

    # @pyqtSlot()
    # def showEvent(self, e):
    #     if not self.loaded:
    #         self.loadUrl("")
    #         self.loaded = True
    #     QDialog.showEvent(self, e)

    @pyqtSlot()
    def enterUrl(self):
        self.loadUrl(self.comboBox.lineEdit().text())

    @pyqtSlot(str)
    def loadUrl(self, url):
        curtxt = self.comboBox.lineEdit().text()
        if not url and not curtxt:
            return

        cururl = curtxt if not url else url
        # self.appendLog("cururl={0}".format(cururl))
        self.loadQUrl(QUrl(cururl))

    @pyqtSlot("QUrl")
    def loadQUrl(self, url):
        if url.isEmpty() or not url.isValid():
            return

        req = QNetworkRequest()
        req.setUrl(url)
        req.setRawHeader("User-Agent",
                         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0)"
                         " Gecko/20100101 Firefox/32.0")

        authcfg = self.leAuthId.text()

        if authcfg:
            self.appendLog("update request w/ authcfg: {0}".format(authcfg))
            QgsAuthManager.instance().updateNetworkRequest(req, authcfg)

        # TODO: why doesn't it recongnize ssl cert/key in request?
        # self.webView.load(req, QNetworkAccessManager.GetOperation)

        if self.reply is not None and self.reply.isRunning():
            self.reply.close()
        self.reply = None

        self.reply = QgsNetworkAccessManager.instance().get(req)

        if authcfg:
            self.appendLog("update reply w/ authcfg: {0}".format(authcfg))
            QgsAuthManager.instance().updateNetworkReply(self.reply, authcfg)

        self.clearWebView()
        self.webView.urlChanged.emit(self.reply.request().url())
        self.webView.setFocus()
        self.reply.readyRead.connect(self.loadReply)
        self.reply.finished.connect(self.replyFinished)
        self.reply.error.connect(self.replyError)

    @pyqtSlot()
    def loadReply(self):
        url = self.reply.url()
        self.webView.setContent(self.reply.readAll(), "", url)

    @pyqtSlot()
    def setWebPage(self):
        # self.webView.page().deleteLater()
        page = QWebPage(self)
        page.setNetworkAccessManager(QgsNetworkAccessManager.instance())
        self.webView.setPage(page)
        if not self.loaded:
            self.webView.load(QUrl("http://127.0.0.1"))
            self.loaded = True

    @pyqtSlot()
    def clearWebView(self):
        self.webView.setContent("")

    @pyqtSlot()
    def replyFinished(self):
        self.reply.deleteLater()
        self.reply = None

    @pyqtSlot(int)
    def replyError(self, err):
        if err != int(QNetworkReply.NoError):
            self.appendLog("Network error #{0}: {1}".format(
                self.reply.error(), self.reply.errorString()))

    @pyqtSlot()
    def on_btnAuthSelect_clicked(self):
        dlg = QDialog(None)
        dlg.setWindowTitle(self.tr("Select Authentication"))
        layout = QVBoxLayout(dlg)

        acs = QgsAuthConfigSelect(dlg)
        if self.leAuthId.text():
            acs.setConfigId(self.leAuthId.text())
        layout.addWidget(acs)

        buttonbox = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, dlg
        )
        layout.addWidget(buttonbox)
        buttonbox.accepted.connect(dlg.accept)
        buttonbox.rejected.connect(dlg.close)

        dlg.setLayout(layout)
        dlg.setWindowModality(Qt.WindowModal)
        if dlg.exec_():
            self.leAuthId.setText(acs.configId())
        del dlg

    @pyqtSlot()
    def on_btnClearID_clicked(self):
        self.leAuthId.clear()
