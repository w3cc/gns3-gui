# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/noplay/code/gns3/gns3-gui/gns3/modules/dynamips/ui/ios_router_wizard.ui'
#
# Created: Thu Apr 30 11:30:20 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from gns3.qt import QtCore, QtGui, QtWidgets


class Ui_IOSRouterWizard(object):

    def setupUi(self, IOSRouterWizard):
        IOSRouterWizard.setObjectName("IOSRouterWizard")
        IOSRouterWizard.resize(585, 398)
        IOSRouterWizard.setModal(True)
        self.uiServerWizardPage = QtWidgets.QWizardPage()
        self.uiServerWizardPage.setObjectName("uiServerWizardPage")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uiServerWizardPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiServerTypeGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiServerTypeGroupBox.setObjectName("uiServerTypeGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.uiServerTypeGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiRemoteRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiRemoteRadioButton.setChecked(True)
        self.uiRemoteRadioButton.setObjectName("uiRemoteRadioButton")
        self.horizontalLayout.addWidget(self.uiRemoteRadioButton)
        self.uiCloudRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiCloudRadioButton.setObjectName("uiCloudRadioButton")
        self.horizontalLayout.addWidget(self.uiCloudRadioButton)
        self.uiLocalRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiLocalRadioButton.setObjectName("uiLocalRadioButton")
        self.horizontalLayout.addWidget(self.uiLocalRadioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.uiServerTypeGroupBox)
        self.uiRemoteServersGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiRemoteServersGroupBox.setObjectName("uiRemoteServersGroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.uiRemoteServersGroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.uiLoadBalanceCheckBox = QtWidgets.QCheckBox(self.uiRemoteServersGroupBox)
        self.uiLoadBalanceCheckBox.setChecked(True)
        self.uiLoadBalanceCheckBox.setObjectName("uiLoadBalanceCheckBox")
        self.gridLayout_7.addWidget(self.uiLoadBalanceCheckBox, 0, 0, 1, 2)
        self.uiRemoteServersLabel = QtWidgets.QLabel(self.uiRemoteServersGroupBox)
        self.uiRemoteServersLabel.setObjectName("uiRemoteServersLabel")
        self.gridLayout_7.addWidget(self.uiRemoteServersLabel, 1, 0, 1, 1)
        self.uiRemoteServersComboBox = QtWidgets.QComboBox(self.uiRemoteServersGroupBox)
        self.uiRemoteServersComboBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersComboBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersComboBox.setSizePolicy(sizePolicy)
        self.uiRemoteServersComboBox.setObjectName("uiRemoteServersComboBox")
        self.gridLayout_7.addWidget(self.uiRemoteServersComboBox, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.uiRemoteServersGroupBox)
        IOSRouterWizard.addPage(self.uiServerWizardPage)
        self.uiIOSImageWizardPage = QtWidgets.QWizardPage()
        self.uiIOSImageWizardPage.setObjectName("uiIOSImageWizardPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uiIOSImageWizardPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.uiIOSExistingImageRadioButton = QtWidgets.QRadioButton(self.uiIOSImageWizardPage)
        self.uiIOSExistingImageRadioButton.setChecked(True)
        self.uiIOSExistingImageRadioButton.setObjectName("uiIOSExistingImageRadioButton")
        self.horizontalLayout_4.addWidget(self.uiIOSExistingImageRadioButton)
        self.uiIOSNewImageRadioButton = QtWidgets.QRadioButton(self.uiIOSImageWizardPage)
        self.uiIOSNewImageRadioButton.setChecked(False)
        self.uiIOSNewImageRadioButton.setObjectName("uiIOSNewImageRadioButton")
        self.horizontalLayout_4.addWidget(self.uiIOSNewImageRadioButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.uiIOSImageLabel = QtWidgets.QLabel(self.uiIOSImageWizardPage)
        self.uiIOSImageLabel.setObjectName("uiIOSImageLabel")
        self.verticalLayout_2.addWidget(self.uiIOSImageLabel)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.uiIOSImageListComboBox = QtWidgets.QComboBox(self.uiIOSImageWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiIOSImageListComboBox.sizePolicy().hasHeightForWidth())
        self.uiIOSImageListComboBox.setSizePolicy(sizePolicy)
        self.uiIOSImageListComboBox.setObjectName("uiIOSImageListComboBox")
        self.horizontalLayout_5.addWidget(self.uiIOSImageListComboBox)
        self.uiIOSImageLineEdit = QtWidgets.QLineEdit(self.uiIOSImageWizardPage)
        self.uiIOSImageLineEdit.setObjectName("uiIOSImageLineEdit")
        self.horizontalLayout_5.addWidget(self.uiIOSImageLineEdit)
        self.uiIOSImageToolButton = QtWidgets.QToolButton(self.uiIOSImageWizardPage)
        self.uiIOSImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiIOSImageToolButton.setObjectName("uiIOSImageToolButton")
        self.horizontalLayout_5.addWidget(self.uiIOSImageToolButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        IOSRouterWizard.addPage(self.uiIOSImageWizardPage)
        self.uiNamePlatformWizardPage = QtWidgets.QWizardPage()
        self.uiNamePlatformWizardPage.setObjectName("uiNamePlatformWizardPage")
        self.gridLayout = QtWidgets.QGridLayout(self.uiNamePlatformWizardPage)
        self.gridLayout.setObjectName("gridLayout")
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.uiNamePlatformWizardPage)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout.addWidget(self.uiNameLineEdit, 0, 1, 1, 1)
        self.uiChassisComboBox = QtWidgets.QComboBox(self.uiNamePlatformWizardPage)
        self.uiChassisComboBox.setObjectName("uiChassisComboBox")
        self.gridLayout.addWidget(self.uiChassisComboBox, 2, 1, 1, 1)
        self.uiTypeLabel = QtWidgets.QLabel(self.uiNamePlatformWizardPage)
        self.uiTypeLabel.setObjectName("uiTypeLabel")
        self.gridLayout.addWidget(self.uiTypeLabel, 1, 0, 1, 1)
        self.uiNameLabel = QtWidgets.QLabel(self.uiNamePlatformWizardPage)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiPlatformComboBox = QtWidgets.QComboBox(self.uiNamePlatformWizardPage)
        self.uiPlatformComboBox.setObjectName("uiPlatformComboBox")
        self.gridLayout.addWidget(self.uiPlatformComboBox, 1, 1, 1, 1)
        self.uiChassisLabel = QtWidgets.QLabel(self.uiNamePlatformWizardPage)
        self.uiChassisLabel.setObjectName("uiChassisLabel")
        self.gridLayout.addWidget(self.uiChassisLabel, 2, 0, 1, 1)
        self.uiEtherSwitchCheckBox = QtWidgets.QCheckBox(self.uiNamePlatformWizardPage)
        self.uiEtherSwitchCheckBox.setObjectName("uiEtherSwitchCheckBox")
        self.gridLayout.addWidget(self.uiEtherSwitchCheckBox, 3, 0, 1, 2)
        IOSRouterWizard.addPage(self.uiNamePlatformWizardPage)
        self.uiMemoryWizardPage = QtWidgets.QWizardPage()
        self.uiMemoryWizardPage.setObjectName("uiMemoryWizardPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiMemoryWizardPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiRamLabel = QtWidgets.QLabel(self.uiMemoryWizardPage)
        self.uiRamLabel.setObjectName("uiRamLabel")
        self.gridLayout_2.addWidget(self.uiRamLabel, 0, 0, 1, 1)
        self.uiRamSpinBox = QtWidgets.QSpinBox(self.uiMemoryWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRamSpinBox.sizePolicy().hasHeightForWidth())
        self.uiRamSpinBox.setSizePolicy(sizePolicy)
        self.uiRamSpinBox.setMinimum(32)
        self.uiRamSpinBox.setMaximum(65535)
        self.uiRamSpinBox.setSingleStep(32)
        self.uiRamSpinBox.setProperty("value", 128)
        self.uiRamSpinBox.setObjectName("uiRamSpinBox")
        self.gridLayout_2.addWidget(self.uiRamSpinBox, 0, 1, 1, 1)
        self.uiTestIOSImagePushButton = QtWidgets.QPushButton(self.uiMemoryWizardPage)
        self.uiTestIOSImagePushButton.setObjectName("uiTestIOSImagePushButton")
        self.gridLayout_2.addWidget(self.uiTestIOSImagePushButton, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.uiMemoryWizardPage)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 3)
        IOSRouterWizard.addPage(self.uiMemoryWizardPage)
        self.uiNetworkAdaptersWizardPage = QtWidgets.QWizardPage()
        self.uiNetworkAdaptersWizardPage.setObjectName("uiNetworkAdaptersWizardPage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.uiNetworkAdaptersWizardPage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.uiSlot0Label = QtWidgets.QLabel(self.uiNetworkAdaptersWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSlot0Label.sizePolicy().hasHeightForWidth())
        self.uiSlot0Label.setSizePolicy(sizePolicy)
        self.uiSlot0Label.setObjectName("uiSlot0Label")
        self.gridLayout_4.addWidget(self.uiSlot0Label, 0, 0, 1, 1)
        self.uiSlot0comboBox = QtWidgets.QComboBox(self.uiNetworkAdaptersWizardPage)
        self.uiSlot0comboBox.setObjectName("uiSlot0comboBox")
        self.gridLayout_4.addWidget(self.uiSlot0comboBox, 0, 1, 1, 1)
        self.uiSlot1Label = QtWidgets.QLabel(self.uiNetworkAdaptersWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSlot1Label.sizePolicy().hasHeightForWidth())
        self.uiSlot1Label.setSizePolicy(sizePolicy)
        self.uiSlot1Label.setObjectName("uiSlot1Label")
        self.gridLayout_4.addWidget(self.uiSlot1Label, 1, 0, 1, 1)
        self.uiSlot1comboBox = QtWidgets.QComboBox(self.uiNetworkAdaptersWizardPage)
        self.uiSlot1comboBox.setObjectName("uiSlot1comboBox")
        self.gridLayout_4.addWidget(self.uiSlot1comboBox, 1, 1, 1, 1)
        self.uiSlot2Label = QtWidgets.QLabel(self.uiNetworkAdaptersWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSlot2Label.sizePolicy().hasHeightForWidth())
        self.uiSlot2Label.setSizePolicy(sizePolicy)
        self.uiSlot2Label.setObjectName("uiSlot2Label")
        self.gridLayout_4.addWidget(self.uiSlot2Label, 2, 0, 1, 1)
        self.uiSlot2comboBox = QtWidgets.QComboBox(self.uiNetworkAdaptersWizardPage)
        self.uiSlot2comboBox.setObjectName("uiSlot2comboBox")
        self.gridLayout_4.addWidget(self.uiSlot2comboBox, 2, 1, 1, 1)
        self.uiSlot3Label = QtWidgets.QLabel(self.uiNetworkAdaptersWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSlot3Label.sizePolicy().hasHeightForWidth())
        self.uiSlot3Label.setSizePolicy(sizePolicy)
        self.uiSlot3Label.setObjectName("uiSlot3Label")
        self.gridLayout_4.addWidget(self.uiSlot3Label, 3, 0, 1, 1)
        self.uiSlot3comboBox = QtWidgets.QComboBox(self.uiNetworkAdaptersWizardPage)
        self.uiSlot3comboBox.setObjectName("uiSlot3comboBox")
        self.gridLayout_4.addWidget(self.uiSlot3comboBox, 3, 1, 1, 1)
        self.uiSlot4Label = QtWidgets.QLabel(self.uiNetworkAdaptersWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSlot4Label.sizePolicy().hasHeightForWidth())
        self.uiSlot4Label.setSizePolicy(sizePolicy)
        self.uiSlot4Label.setObjectName("uiSlot4Label")
        self.gridLayout_4.addWidget(self.uiSlot4Label, 4, 0, 1, 1)
        self.uiSlot4comboBox = QtWidgets.QComboBox(self.uiNetworkAdaptersWizardPage)
        self.uiSlot4comboBox.setObjectName("uiSlot4comboBox")
        self.gridLayout_4.addWidget(self.uiSlot4comboBox, 4, 1, 1, 1)
        self.uiSlot5Label = QtWidgets.QLabel(self.uiNetworkAdaptersWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSlot5Label.sizePolicy().hasHeightForWidth())
        self.uiSlot5Label.setSizePolicy(sizePolicy)
        self.uiSlot5Label.setObjectName("uiSlot5Label")
        self.gridLayout_4.addWidget(self.uiSlot5Label, 5, 0, 1, 1)
        self.uiSlot5comboBox = QtWidgets.QComboBox(self.uiNetworkAdaptersWizardPage)
        self.uiSlot5comboBox.setObjectName("uiSlot5comboBox")
        self.gridLayout_4.addWidget(self.uiSlot5comboBox, 5, 1, 1, 1)
        self.uiSlot6Label = QtWidgets.QLabel(self.uiNetworkAdaptersWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSlot6Label.sizePolicy().hasHeightForWidth())
        self.uiSlot6Label.setSizePolicy(sizePolicy)
        self.uiSlot6Label.setObjectName("uiSlot6Label")
        self.gridLayout_4.addWidget(self.uiSlot6Label, 6, 0, 1, 1)
        self.uiSlot6comboBox = QtWidgets.QComboBox(self.uiNetworkAdaptersWizardPage)
        self.uiSlot6comboBox.setObjectName("uiSlot6comboBox")
        self.gridLayout_4.addWidget(self.uiSlot6comboBox, 6, 1, 1, 1)
        IOSRouterWizard.addPage(self.uiNetworkAdaptersWizardPage)
        self.uiWicWizardPage = QtWidgets.QWizardPage()
        self.uiWicWizardPage.setObjectName("uiWicWizardPage")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.uiWicWizardPage)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.uiWic0Label = QtWidgets.QLabel(self.uiWicWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiWic0Label.sizePolicy().hasHeightForWidth())
        self.uiWic0Label.setSizePolicy(sizePolicy)
        self.uiWic0Label.setObjectName("uiWic0Label")
        self.gridLayout_5.addWidget(self.uiWic0Label, 0, 0, 1, 1)
        self.uiWic0comboBox = QtWidgets.QComboBox(self.uiWicWizardPage)
        self.uiWic0comboBox.setObjectName("uiWic0comboBox")
        self.gridLayout_5.addWidget(self.uiWic0comboBox, 0, 1, 1, 1)
        self.uiWic1Label = QtWidgets.QLabel(self.uiWicWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiWic1Label.sizePolicy().hasHeightForWidth())
        self.uiWic1Label.setSizePolicy(sizePolicy)
        self.uiWic1Label.setObjectName("uiWic1Label")
        self.gridLayout_5.addWidget(self.uiWic1Label, 1, 0, 1, 1)
        self.uiWic1comboBox = QtWidgets.QComboBox(self.uiWicWizardPage)
        self.uiWic1comboBox.setObjectName("uiWic1comboBox")
        self.gridLayout_5.addWidget(self.uiWic1comboBox, 1, 1, 1, 1)
        self.uiWic2Label = QtWidgets.QLabel(self.uiWicWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiWic2Label.sizePolicy().hasHeightForWidth())
        self.uiWic2Label.setSizePolicy(sizePolicy)
        self.uiWic2Label.setObjectName("uiWic2Label")
        self.gridLayout_5.addWidget(self.uiWic2Label, 2, 0, 1, 1)
        self.uiWic2comboBox = QtWidgets.QComboBox(self.uiWicWizardPage)
        self.uiWic2comboBox.setObjectName("uiWic2comboBox")
        self.gridLayout_5.addWidget(self.uiWic2comboBox, 2, 1, 1, 1)
        IOSRouterWizard.addPage(self.uiWicWizardPage)
        self.uiIdlePCWizardPage = QtWidgets.QWizardPage()
        self.uiIdlePCWizardPage.setObjectName("uiIdlePCWizardPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.uiIdlePCWizardPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.uiIdlepcLabel = QtWidgets.QLabel(self.uiIdlePCWizardPage)
        self.uiIdlepcLabel.setObjectName("uiIdlepcLabel")
        self.gridLayout_3.addWidget(self.uiIdlepcLabel, 0, 0, 1, 1)
        self.uiIdlepcLineEdit = QtWidgets.QLineEdit(self.uiIdlePCWizardPage)
        self.uiIdlepcLineEdit.setObjectName("uiIdlepcLineEdit")
        self.gridLayout_3.addWidget(self.uiIdlepcLineEdit, 0, 1, 1, 1)
        self.uiIdlePCFinderPushButton = QtWidgets.QPushButton(self.uiIdlePCWizardPage)
        self.uiIdlePCFinderPushButton.setObjectName("uiIdlePCFinderPushButton")
        self.gridLayout_3.addWidget(self.uiIdlePCFinderPushButton, 0, 2, 1, 1)
        IOSRouterWizard.addPage(self.uiIdlePCWizardPage)

        self.retranslateUi(IOSRouterWizard)
        QtCore.QMetaObject.connectSlotsByName(IOSRouterWizard)
        IOSRouterWizard.setTabOrder(self.uiNameLineEdit, self.uiPlatformComboBox)

    def retranslateUi(self, IOSRouterWizard):
        _translate = QtCore.QCoreApplication.translate
        IOSRouterWizard.setWindowTitle(_translate("IOSRouterWizard", "New IOS router template"))
        self.uiServerWizardPage.setTitle(_translate("IOSRouterWizard", "Server"))
        self.uiServerWizardPage.setSubTitle(_translate("IOSRouterWizard", "Please choose a server type to run your new IOS router."))
        self.uiServerTypeGroupBox.setTitle(_translate("IOSRouterWizard", "Server type"))
        self.uiRemoteRadioButton.setText(_translate("IOSRouterWizard", "Remote"))
        self.uiCloudRadioButton.setText(_translate("IOSRouterWizard", "Cloud"))
        self.uiLocalRadioButton.setText(_translate("IOSRouterWizard", "Local"))
        self.uiRemoteServersGroupBox.setTitle(_translate("IOSRouterWizard", "Remote servers"))
        self.uiLoadBalanceCheckBox.setText(_translate("IOSRouterWizard", "Load balance across all available remote servers"))
        self.uiRemoteServersLabel.setText(_translate("IOSRouterWizard", "Run on server:"))
        self.uiIOSImageWizardPage.setTitle(_translate("IOSRouterWizard", "IOS image"))
        self.uiIOSImageWizardPage.setSubTitle(_translate("IOSRouterWizard", "Please choose an IOS image."))
        self.uiIOSExistingImageRadioButton.setText(_translate("IOSRouterWizard", "Existing image"))
        self.uiIOSNewImageRadioButton.setText(_translate("IOSRouterWizard", "New Image"))
        self.uiIOSImageLabel.setText(_translate("IOSRouterWizard", "IOS image:"))
        self.uiIOSImageToolButton.setText(_translate("IOSRouterWizard", "&Browse..."))
        self.uiNamePlatformWizardPage.setTitle(_translate("IOSRouterWizard", "Name and platform"))
        self.uiNamePlatformWizardPage.setSubTitle(_translate("IOSRouterWizard", "Please choose a descriptive name for this new IOS router and verify the platform and chassis."))
        self.uiTypeLabel.setText(_translate("IOSRouterWizard", "Platform:"))
        self.uiNameLabel.setText(_translate("IOSRouterWizard", "Name:"))
        self.uiChassisLabel.setText(_translate("IOSRouterWizard", "Chassis:"))
        self.uiEtherSwitchCheckBox.setText(_translate("IOSRouterWizard", "This is an EtherSwitch router"))
        self.uiMemoryWizardPage.setTitle(_translate("IOSRouterWizard", "Memory"))
        self.uiMemoryWizardPage.setSubTitle(_translate("IOSRouterWizard", "Please check the amount of memory (RAM) that you allocate to IOS. Too much or not enough RAM could prevent IOS to start."))
        self.uiRamLabel.setText(_translate("IOSRouterWizard", "Default RAM:"))
        self.uiRamSpinBox.setSuffix(_translate("IOSRouterWizard", " MiB"))
        self.uiTestIOSImagePushButton.setText(_translate("IOSRouterWizard", "&Test IOS image"))
        self.label.setText(_translate("IOSRouterWizard", "<html><head/><body><p><a href=\"http://tools.cisco.com/ITDIT/CFN/jsp/SearchBySoftware.jsp\"><span style=\" text-decoration: underline; color:#0000ff;\">Check for minimum and maximum RAM requirement</span></a></p></body></html>"))
        self.uiNetworkAdaptersWizardPage.setTitle(_translate("IOSRouterWizard", "Network adapters"))
        self.uiNetworkAdaptersWizardPage.setSubTitle(_translate("IOSRouterWizard", "Please choose the default network adapters that should be inserted into every new instance of this router."))
        self.uiSlot0Label.setText(_translate("IOSRouterWizard", "slot 0:"))
        self.uiSlot1Label.setText(_translate("IOSRouterWizard", "slot 1:"))
        self.uiSlot2Label.setText(_translate("IOSRouterWizard", "slot 2:"))
        self.uiSlot3Label.setText(_translate("IOSRouterWizard", "slot 3:"))
        self.uiSlot4Label.setText(_translate("IOSRouterWizard", "slot 4:"))
        self.uiSlot5Label.setText(_translate("IOSRouterWizard", "slot 5:"))
        self.uiSlot6Label.setText(_translate("IOSRouterWizard", "slot 6:"))
        self.uiWicWizardPage.setTitle(_translate("IOSRouterWizard", "WIC modules"))
        self.uiWicWizardPage.setSubTitle(_translate("IOSRouterWizard", "Please choose the default WIC modules that should be inserted into every new instance of this router."))
        self.uiWic0Label.setText(_translate("IOSRouterWizard", "wic 0:"))
        self.uiWic1Label.setText(_translate("IOSRouterWizard", "wic 1:"))
        self.uiWic2Label.setText(_translate("IOSRouterWizard", "wic 2:"))
        self.uiIdlePCWizardPage.setTitle(_translate("IOSRouterWizard", "Idle-PC"))
        self.uiIdlePCWizardPage.setSubTitle(_translate("IOSRouterWizard", "An idle-pc value is necessary to prevent IOS to use 100% of your processor or one of its core."))
        self.uiIdlepcLabel.setText(_translate("IOSRouterWizard", "Idle-PC:"))
        self.uiIdlePCFinderPushButton.setText(_translate("IOSRouterWizard", "Idle-PC finder"))
