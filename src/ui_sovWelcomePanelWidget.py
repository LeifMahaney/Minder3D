# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovWelcomePanelWidgetwVsLfD.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QTextBrowser,
    QWidget)

class Ui_WelcomePanelWidget(object):
    def setupUi(self, WelcomePanelWidget):
        if not WelcomePanelWidget.objectName():
            WelcomePanelWidget.setObjectName(u"WelcomePanelWidget")
        WelcomePanelWidget.resize(667, 153)
        self.welcomeTextBrowser = QTextBrowser(WelcomePanelWidget)
        self.welcomeTextBrowser.setObjectName(u"welcomeTextBrowser")
        self.welcomeTextBrowser.setGeometry(QRect(20, 10, 301, 131))
        self.welcomeLoadImageButton = QPushButton(WelcomePanelWidget)
        self.welcomeLoadImageButton.setObjectName(u"welcomeLoadImageButton")
        self.welcomeLoadImageButton.setGeometry(QRect(360, 20, 121, 24))
        self.welcomeLoadDICOMButton = QPushButton(WelcomePanelWidget)
        self.welcomeLoadDICOMButton.setObjectName(u"welcomeLoadDICOMButton")
        self.welcomeLoadDICOMButton.setGeometry(QRect(360, 50, 121, 24))
        self.welcomeSaveImageButton = QPushButton(WelcomePanelWidget)
        self.welcomeSaveImageButton.setObjectName(u"welcomeSaveImageButton")
        self.welcomeSaveImageButton.setGeometry(QRect(520, 20, 121, 24))
        self.welcomeSaveSceneButton = QPushButton(WelcomePanelWidget)
        self.welcomeSaveSceneButton.setObjectName(u"welcomeSaveSceneButton")
        self.welcomeSaveSceneButton.setGeometry(QRect(520, 80, 121, 24))
        self.welcomeLoadSceneButton = QPushButton(WelcomePanelWidget)
        self.welcomeLoadSceneButton.setObjectName(u"welcomeLoadSceneButton")
        self.welcomeLoadSceneButton.setGeometry(QRect(360, 80, 121, 24))
        self.welcomeSaveOverlayButton = QPushButton(WelcomePanelWidget)
        self.welcomeSaveOverlayButton.setObjectName(u"welcomeSaveOverlayButton")
        self.welcomeSaveOverlayButton.setGeometry(QRect(520, 50, 121, 24))
        self.welcomeSaveVTKModelsButton = QPushButton(WelcomePanelWidget)
        self.welcomeSaveVTKModelsButton.setObjectName(u"welcomeSaveVTKModelsButton")
        self.welcomeSaveVTKModelsButton.setGeometry(QRect(520, 110, 121, 24))

        self.retranslateUi(WelcomePanelWidget)

        QMetaObject.connectSlotsByName(WelcomePanelWidget)
    # setupUi

    def retranslateUi(self, WelcomePanelWidget):
        WelcomePanelWidget.setWindowTitle(QCoreApplication.translate("WelcomePanelWidget", u"Form", None))
        self.welcomeTextBrowser.setHtml(QCoreApplication.translate("WelcomePanelWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome to PyMIDAS_AI!</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To get started, load data using the buttons to the right or the &quot;File&quot; menu at th"
                        "e top.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Then, switch to the &quot;+&quot; tab to select a task to run.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Once you're done, switch back to this tab or use the &quot;File&quot; menu to save your results.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-in"
                        "dent:0px;\">For support, email </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">stephen@aylward.org</p></body></html>", None))
        self.welcomeLoadImageButton.setText(QCoreApplication.translate("WelcomePanelWidget", u"Load Image", None))
        self.welcomeLoadDICOMButton.setText(QCoreApplication.translate("WelcomePanelWidget", u"Load DICOM Data", None))
        self.welcomeSaveImageButton.setText(QCoreApplication.translate("WelcomePanelWidget", u"Save Image", None))
        self.welcomeSaveSceneButton.setText(QCoreApplication.translate("WelcomePanelWidget", u"Save Scene", None))
        self.welcomeLoadSceneButton.setText(QCoreApplication.translate("WelcomePanelWidget", u"Load Scene", None))
        self.welcomeSaveOverlayButton.setText(QCoreApplication.translate("WelcomePanelWidget", u"Save Overlay", None))
        self.welcomeSaveVTKModelsButton.setText(QCoreApplication.translate("WelcomePanelWidget", u"Save VTK Models", None))
    # retranslateUi

