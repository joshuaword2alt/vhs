# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.controlLayout = QtWidgets.QVBoxLayout()
        self.controlLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.controlLayout.setObjectName("controlLayout")
        self.checkboxesLayout = QtWidgets.QGridLayout()
        self.checkboxesLayout.setObjectName("checkboxesLayout")
        self.controlLayout.addLayout(self.checkboxesLayout)
        self.horizontalLayout_3.addLayout(self.controlLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.image_frame = QtWidgets.QLabel(self.centralwidget)
        self.image_frame.setMinimumSize(QtCore.QSize(854, 480))
        self.image_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.image_frame.setObjectName("image_frame")
        self.verticalLayout.addWidget(self.image_frame)
        self.positionControlLayout = QtWidgets.QHBoxLayout()
        self.positionControlLayout.setObjectName("positionControlLayout")
        self.videoTrackSlider = QtWidgets.QScrollBar(self.centralwidget)
        self.videoTrackSlider.setTabletTracking(False)
        self.videoTrackSlider.setAutoFillBackground(False)
        self.videoTrackSlider.setMinimum(1)
        self.videoTrackSlider.setMaximum(3000)
        self.videoTrackSlider.setTracking(True)
        self.videoTrackSlider.setOrientation(QtCore.Qt.Horizontal)
        self.videoTrackSlider.setInvertedControls(True)
        self.videoTrackSlider.setObjectName("videoTrackSlider")
        self.positionControlLayout.addWidget(self.videoTrackSlider)
        self.livePreviewCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.livePreviewCheckbox.setMaximumSize(QtCore.QSize(136, 16777215))
        self.livePreviewCheckbox.setObjectName("livePreviewCheckbox")
        self.positionControlLayout.addWidget(self.livePreviewCheckbox)
        self.verticalLayout.addLayout(self.positionControlLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.previewHeightBox = QtWidgets.QSpinBox(self.centralwidget)
        self.previewHeightBox.setMaximum(2288)
        self.previewHeightBox.setSingleStep(120)
        self.previewHeightBox.setProperty("value", 480)
        self.previewHeightBox.setObjectName("previewHeightBox")
        self.gridLayout_2.addWidget(self.previewHeightBox, 0, 1, 1, 1)
        self.seedSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.seedSpinBox.setObjectName("seedSpinBox")
        self.gridLayout_2.addWidget(self.seedSpinBox, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMidLineWidth(-3)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.seedLabel = QtWidgets.QLabel(self.centralwidget)
        self.seedLabel.setMaximumSize(QtCore.QSize(85, 16777215))
        self.seedLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.seedLabel.setObjectName("seedLabel")
        self.gridLayout_2.addWidget(self.seedLabel, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.renderHeightBox = QtWidgets.QSpinBox(self.centralwidget)
        self.renderHeightBox.setMaximum(3000)
        self.renderHeightBox.setSingleStep(120)
        self.renderHeightBox.setObjectName("renderHeightBox")
        self.gridLayout_2.addWidget(self.renderHeightBox, 1, 1, 1, 1)
        self.compareModeButton = QtWidgets.QCheckBox(self.centralwidget)
        self.compareModeButton.setObjectName("compareModeButton")
        self.gridLayout_2.addWidget(self.compareModeButton, 1, 3, 1, 1)
        self.toggleMainEffect = QtWidgets.QCheckBox(self.centralwidget)
        self.toggleMainEffect.setChecked(True)
        self.toggleMainEffect.setObjectName("toggleMainEffect")
        self.gridLayout_2.addWidget(self.toggleMainEffect, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setText("")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout.addWidget(self.statusLabel)
        self.openFile = QtWidgets.QPushButton(self.centralwidget)
        self.openFile.setObjectName("openFile")
        self.verticalLayout.addWidget(self.openFile)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.renderVideoButton = QtWidgets.QPushButton(self.centralwidget)
        self.renderVideoButton.setEnabled(True)
        self.renderVideoButton.setObjectName("renderVideoButton")
        self.horizontalLayout.addWidget(self.renderVideoButton)
        self.pauseRenderButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pauseRenderButton.sizePolicy().hasHeightForWidth())
        self.pauseRenderButton.setSizePolicy(sizePolicy)
        self.pauseRenderButton.setMaximumSize(QtCore.QSize(165, 16777215))
        self.pauseRenderButton.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.pauseRenderButton.setFont(font)
        self.pauseRenderButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pauseRenderButton.setIconSize(QtCore.QSize(16, 16))
        self.pauseRenderButton.setCheckable(True)
        self.pauseRenderButton.setObjectName("pauseRenderButton")
        self.horizontalLayout.addWidget(self.pauseRenderButton)
        self.stopRenderButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopRenderButton.setEnabled(False)
        self.stopRenderButton.setMaximumSize(QtCore.QSize(138, 16777215))
        self.stopRenderButton.setObjectName("stopRenderButton")
        self.horizontalLayout.addWidget(self.stopRenderButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Über NTSC — QT Edition 3000"))
        self.image_frame.setText(_translate("MainWindow", "ImageFrameTextLabel"))
        self.livePreviewCheckbox.setText(_translate("MainWindow", "LivePreview"))
        self.label.setText(_translate("MainWindow", "Preview height"))
        self.seedLabel.setText(_translate("MainWindow", "Seed"))
        self.label_2.setText(_translate("MainWindow", "Render height"))
        self.compareModeButton.setText(_translate("MainWindow", "Compare mode"))
        self.toggleMainEffect.setText(_translate("MainWindow", "ON/OFF"))
        self.openFile.setText(_translate("MainWindow", "Open Video"))
        self.renderVideoButton.setText(_translate("MainWindow", "Render As"))
        self.pauseRenderButton.setText(_translate("MainWindow", "⏸ Pause Render"))
        self.stopRenderButton.setText(_translate("MainWindow", "Stop Render"))
