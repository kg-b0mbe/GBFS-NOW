"""
Compatibility helpers for QGIS 3.38+.

QGIS 3.38 (Qt 6) replaced QVariant-based field types with QMetaType.Type.
This module exposes unified constants so the rest of the plugin can import
FIELD_STRING / FIELD_INT / FIELD_DOUBLE / FIELD_BOOL / DIALOG_ACCEPTED
without worrying about which QGIS version is running.
"""

from qgis.core import Qgis
from qgis.PyQt import QtWidgets

if Qgis.versionInt() >= 33800:
    # QGIS 3.38+ / Qt 6
    from qgis.PyQt.QtCore import QMetaType

    FIELD_STRING   = QMetaType.Type.QString
    FIELD_INT      = QMetaType.Type.Int
    FIELD_DOUBLE   = QMetaType.Type.Double
    FIELD_BOOL     = QMetaType.Type.Bool

    DIALOG_ACCEPTED = QtWidgets.QDialog.DialogCode.Accepted

else:
    # QGIS < 3.38 / Qt 5
    from qgis.PyQt.QtCore import QVariant

    FIELD_STRING   = QVariant.String
    FIELD_INT      = QVariant.Int
    FIELD_DOUBLE   = QVariant.Double
    FIELD_BOOL     = QVariant.Bool

    DIALOG_ACCEPTED = QtWidgets.QDialog.Accepted
