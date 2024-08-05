# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovImportExportPanelWidgetPIUfEo.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_ImportExportPanelWidget(object):
    def setupUi(self, ImportExportPanelWidget):
        if not ImportExportPanelWidget.objectName():
            ImportExportPanelWidget.setObjectName(u"ImportExportPanelWidget")
        ImportExportPanelWidget.resize(484, 153)
        self.importExportLoadImageButton = QPushButton(ImportExportPanelWidget)
        self.importExportLoadImageButton.setObjectName(u"importExportLoadImageButton")
        self.importExportLoadImageButton.setGeometry(QRect(20, 10, 121, 24))
        self.importExportImportDICOMButton = QPushButton(ImportExportPanelWidget)
        self.importExportImportDICOMButton.setObjectName(u"importExportImportDICOMButton")
        self.importExportImportDICOMButton.setGeometry(QRect(20, 100, 121, 24))
        self.importExportSaveImageButton = QPushButton(ImportExportPanelWidget)
        self.importExportSaveImageButton.setObjectName(u"importExportSaveImageButton")
        self.importExportSaveImageButton.setGeometry(QRect(180, 10, 121, 24))
        self.importExportSaveSceneButton = QPushButton(ImportExportPanelWidget)
        self.importExportSaveSceneButton.setObjectName(u"importExportSaveSceneButton")
        self.importExportSaveSceneButton.setGeometry(QRect(180, 40, 121, 24))
        self.importExportLoadSceneButton = QPushButton(ImportExportPanelWidget)
        self.importExportLoadSceneButton.setObjectName(u"importExportLoadSceneButton")
        self.importExportLoadSceneButton.setGeometry(QRect(20, 40, 121, 24))
        self.importExportSaveOverlayButton = QPushButton(ImportExportPanelWidget)
        self.importExportSaveOverlayButton.setObjectName(u"importExportSaveOverlayButton")
        self.importExportSaveOverlayButton.setGeometry(QRect(180, 70, 121, 24))
        self.importExportSaveVTKModelsButton = QPushButton(ImportExportPanelWidget)
        self.importExportSaveVTKModelsButton.setObjectName(u"importExportSaveVTKModelsButton")
        self.importExportSaveVTKModelsButton.setGeometry(QRect(340, 40, 121, 24))
        self.importExportLoadOverlayButton = QPushButton(ImportExportPanelWidget)
        self.importExportLoadOverlayButton.setObjectName(u"importExportLoadOverlayButton")
        self.importExportLoadOverlayButton.setGeometry(QRect(20, 70, 121, 24))

        self.retranslateUi(ImportExportPanelWidget)

        QMetaObject.connectSlotsByName(ImportExportPanelWidget)
    # setupUi

    def retranslateUi(self, ImportExportPanelWidget):
        ImportExportPanelWidget.setWindowTitle(QCoreApplication.translate("ImportExportPanelWidget", u"Form", None))
        self.importExportLoadImageButton.setText(QCoreApplication.translate("ImportExportPanelWidget", u"Load Image", None))
        self.importExportImportDICOMButton.setText(QCoreApplication.translate("ImportExportPanelWidget", u"Import DICOM Data", None))
        self.importExportSaveImageButton.setText(QCoreApplication.translate("ImportExportPanelWidget", u"Save Image", None))
        self.importExportSaveSceneButton.setText(QCoreApplication.translate("ImportExportPanelWidget", u"Save Scene", None))
        self.importExportLoadSceneButton.setText(QCoreApplication.translate("ImportExportPanelWidget", u"Load Scene", None))
        self.importExportSaveOverlayButton.setText(QCoreApplication.translate("ImportExportPanelWidget", u"Save Overlay", None))
        self.importExportSaveVTKModelsButton.setText(QCoreApplication.translate("ImportExportPanelWidget", u"Save VTK Models", None))
        self.importExportLoadOverlayButton.setText(QCoreApplication.translate("ImportExportPanelWidget", u"Load Overlay", None))
    # retranslateUi

