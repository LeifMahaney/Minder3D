# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovView2DPanelWidgetyMBlFj.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QToolButton, QVBoxLayout,
    QWidget)

class Ui_View2DPanelWidget(object):
    def setupUi(self, View2DPanelWidget):
        if not View2DPanelWidget.objectName():
            View2DPanelWidget.setObjectName(u"View2DPanelWidget")
        View2DPanelWidget.resize(495, 491)
        self.gridLayout = QGridLayout(View2DPanelWidget)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.view2DPointerModeButton = QToolButton(View2DPanelWidget)
        self.view2DPointerModeButton.setObjectName(u"view2DPointerModeButton")
        font = QFont()
        font.setPointSize(7)
        self.view2DPointerModeButton.setFont(font)
        icon = QIcon()
        iconThemeName = u"contact-new"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.view2DPointerModeButton.setIcon(icon)
        self.view2DPointerModeButton.setCheckable(True)
        self.view2DPointerModeButton.setChecked(True)
        self.view2DPointerModeButton.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout_3.addWidget(self.view2DPointerModeButton)

        self.view3DWLModeButton = QToolButton(View2DPanelWidget)
        self.view3DWLModeButton.setObjectName(u"view3DWLModeButton")
        self.view3DWLModeButton.setFont(font)
        icon1 = QIcon()
        iconThemeName = u"camera-photo"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.view3DWLModeButton.setIcon(icon1)
        self.view3DWLModeButton.setCheckable(True)

        self.verticalLayout_3.addWidget(self.view3DWLModeButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.view2DLayout = QVBoxLayout()
        self.view2DLayout.setSpacing(3)
        self.view2DLayout.setObjectName(u"view2DLayout")
        self.view2DLayout.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.gridLayout_2.addLayout(self.view2DLayout, 0, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.view2DSliceSlider = QSlider(View2DPanelWidget)
        self.view2DSliceSlider.setObjectName(u"view2DSliceSlider")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view2DSliceSlider.sizePolicy().hasHeightForWidth())
        self.view2DSliceSlider.setSizePolicy(sizePolicy)
        self.view2DSliceSlider.setMinimumSize(QSize(10, 422))
        self.view2DSliceSlider.setOrientation(Qt.Vertical)

        self.verticalLayout.addWidget(self.view2DSliceSlider)

        self.view2DSliceText = QSpinBox(View2DPanelWidget)
        self.view2DSliceText.setObjectName(u"view2DSliceText")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.view2DSliceText.sizePolicy().hasHeightForWidth())
        self.view2DSliceText.setSizePolicy(sizePolicy1)
        self.view2DSliceText.setMinimumSize(QSize(39, 0))
        self.view2DSliceText.setMaximum(999)
        self.view2DSliceText.setDisplayIntegerBase(10)

        self.verticalLayout.addWidget(self.view2DSliceText)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.view2DXYButton = QPushButton(View2DPanelWidget)
        self.view2DXYButton.setObjectName(u"view2DXYButton")
        sizePolicy1.setHeightForWidth(self.view2DXYButton.sizePolicy().hasHeightForWidth())
        self.view2DXYButton.setSizePolicy(sizePolicy1)
        self.view2DXYButton.setMinimumSize(QSize(30, 0))
        self.view2DXYButton.setFont(font)

        self.horizontalLayout.addWidget(self.view2DXYButton)

        self.view2DXZButton = QPushButton(View2DPanelWidget)
        self.view2DXZButton.setObjectName(u"view2DXZButton")
        sizePolicy1.setHeightForWidth(self.view2DXZButton.sizePolicy().hasHeightForWidth())
        self.view2DXZButton.setSizePolicy(sizePolicy1)
        self.view2DXZButton.setMinimumSize(QSize(30, 0))
        self.view2DXZButton.setFont(font)

        self.horizontalLayout.addWidget(self.view2DXZButton)

        self.view2DYZButton = QPushButton(View2DPanelWidget)
        self.view2DYZButton.setObjectName(u"view2DYZButton")
        sizePolicy1.setHeightForWidth(self.view2DYZButton.sizePolicy().hasHeightForWidth())
        self.view2DYZButton.setSizePolicy(sizePolicy1)
        self.view2DYZButton.setMinimumSize(QSize(30, 0))
        self.view2DYZButton.setFont(font)

        self.horizontalLayout.addWidget(self.view2DYZButton)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.view2DOverlayOpacityLabel = QLabel(View2DPanelWidget)
        self.view2DOverlayOpacityLabel.setObjectName(u"view2DOverlayOpacityLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.view2DOverlayOpacityLabel.sizePolicy().hasHeightForWidth())
        self.view2DOverlayOpacityLabel.setSizePolicy(sizePolicy2)
        self.view2DOverlayOpacityLabel.setFont(font)

        self.horizontalLayout.addWidget(self.view2DOverlayOpacityLabel)

        self.view2DOverlayOpacitySlider = QSlider(View2DPanelWidget)
        self.view2DOverlayOpacitySlider.setObjectName(u"view2DOverlayOpacitySlider")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.view2DOverlayOpacitySlider.sizePolicy().hasHeightForWidth())
        self.view2DOverlayOpacitySlider.setSizePolicy(sizePolicy3)
        self.view2DOverlayOpacitySlider.setMinimumSize(QSize(75, 12))
        self.view2DOverlayOpacitySlider.setBaseSize(QSize(0, 0))
        self.view2DOverlayOpacitySlider.setFont(font)
        self.view2DOverlayOpacitySlider.setMaximum(100)
        self.view2DOverlayOpacitySlider.setValue(50)
        self.view2DOverlayOpacitySlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.view2DOverlayOpacitySlider)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.view2DResetButton = QPushButton(View2DPanelWidget)
        self.view2DResetButton.setObjectName(u"view2DResetButton")
        sizePolicy1.setHeightForWidth(self.view2DResetButton.sizePolicy().hasHeightForWidth())
        self.view2DResetButton.setSizePolicy(sizePolicy1)
        self.view2DResetButton.setMinimumSize(QSize(35, 0))
        self.view2DResetButton.setFont(font)

        self.horizontalLayout.addWidget(self.view2DResetButton)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 2)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)


        self.retranslateUi(View2DPanelWidget)

        QMetaObject.connectSlotsByName(View2DPanelWidget)
    # setupUi

    def retranslateUi(self, View2DPanelWidget):
        View2DPanelWidget.setWindowTitle(QCoreApplication.translate("View2DPanelWidget", u"Form", None))
        self.view2DXYButton.setText(QCoreApplication.translate("View2DPanelWidget", u"XY", None))
        self.view2DXZButton.setText(QCoreApplication.translate("View2DPanelWidget", u"XZ", None))
        self.view2DYZButton.setText(QCoreApplication.translate("View2DPanelWidget", u"YZ", None))
        self.view2DOverlayOpacityLabel.setText(QCoreApplication.translate("View2DPanelWidget", u"Overlay Opacity: ", None))
        self.view2DResetButton.setText(QCoreApplication.translate("View2DPanelWidget", u"Reset", None))
    # retranslateUi
