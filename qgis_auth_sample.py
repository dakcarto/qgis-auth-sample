# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AuthSystemSample
                                 A QGIS plugin
 Sample plugin for working with authentication system
                              -------------------
        begin                : 2016-07-11
        copyright            : (C) 2016 by
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
import shutil

from qgis.core import *
from qgis.gui import *
from PyQt4.QtCore import QSettings, qVersion, QCoreApplication, pyqtSlot
from PyQt4.QtGui import QMainWindow, QAction, QIcon
# Initialize Qt resources from resources_rc.py (compiled from resources.qrc)
import resources_rc

from qgis_auth_sample_dialog import AuthSampleDialog


class AuthSystemSample:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        """:type : QgsInterface"""
        self.mw = iface.mainWindow()
        """:type : QMainWindow"""

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            '{0}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            if qVersion() > '4.3.3':
                # noinspection PyArgumentList
                QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.title = self.tr(u'Auth System Sample')
        self.action = None
        self.authdlg = None

        # Set up automated enacting of plugin at end of app launch
        self.iface.initializationCompleted.connect(self.app_initialized)

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('AuthSystemSample', message)

    # noinspection PyPep8Naming
    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/authsystemsample/icon.png'
        icon = QIcon(icon_path)
        self.action = QAction(icon, self.tr(u'Run'),
                              self.iface.mainWindow())
        self.action.triggered.connect(self.run_gui)

        self.iface.addPluginToMenu(self.title, self.action)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        self.iface.removePluginMenu(self.title, self.action)
        self.iface.removeToolBarIcon(self.action)

    @pyqtSlot()
    def app_initialized(self):
        """
        """
        pass

    @pyqtSlot()
    def run_gui(self):
        """
        """
        if self.authdlg is None:
            self.authdlg = AuthSampleDialog(parent=self.mw,
                                            qgis_iface=self.iface)
        self.authdlg.show()
        self.authdlg.raise_()
        self.authdlg.activateWindow()
