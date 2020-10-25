# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Notas_BTPLAN
                                 A QGIS plugin
 Mostra as anotações do BTPLAN em Barra de Mensagem.
                             -------------------
        begin                : 2019-09-11
        copyright            : (C) 2019 by Eulimar Cunha Tiburcio
        email                : eulimar.tiburcio@ibge.gov.br
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
    """Load Notas_BTPLAN class from file Notas_BTPLAN.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .Notas_BTPLAN import Notas_BTPLAN
    return Notas_BTPLAN(iface)
