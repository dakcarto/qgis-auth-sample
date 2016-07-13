# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AuthSystemSample
                                 A QGIS plugin
 Init for a sample plugin for working with authentication system
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
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load AuthSystemSample class from file PopulateAuthSystem.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .qgis_auth_sample import AuthSystemSample
    return AuthSystemSample(iface)
