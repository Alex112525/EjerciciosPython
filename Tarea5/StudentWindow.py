# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StudentWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(454, 422)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.Name = QLabel(self.centralwidget)
        self.Name.setObjectName(u"Name")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.Name)

        self.Name_edit = QLineEdit(self.centralwidget)
        self.Name_edit.setObjectName(u"Name_edit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.Name_edit)

        self.Email = QLabel(self.centralwidget)
        self.Email.setObjectName(u"Email")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.Email)

        self.Email_edit = QLineEdit(self.centralwidget)
        self.Email_edit.setObjectName(u"Email_edit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Email_edit)

        self.Password = QLabel(self.centralwidget)
        self.Password.setObjectName(u"Password")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.Password)

        self.Pass_edit = QLineEdit(self.centralwidget)
        self.Pass_edit.setObjectName(u"Pass_edit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.Pass_edit)

        self.Add_student = QPushButton(self.centralwidget)
        self.Add_student.setObjectName(u"Add_student")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.Add_student)

        self.Student_list = QComboBox(self.centralwidget)
        self.Student_list.setObjectName(u"Student_list")

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.Student_list)

        self.Del_student = QPushButton(self.centralwidget)
        self.Del_student.setObjectName(u"Del_student")

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.Del_student)

        self.Show_student = QPushButton(self.centralwidget)
        self.Show_student.setObjectName(u"Show_student")

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.Show_student)

        self.Up_student = QPushButton(self.centralwidget)
        self.Up_student.setObjectName(u"Up_student")

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.Up_student)

        self.Text = QTextEdit(self.centralwidget)
        self.Text.setObjectName(u"Text")

        self.formLayout.setWidget(8, QFormLayout.SpanningRole, self.Text)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 454, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Name.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.Email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.Password.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.Add_student.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.Del_student.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.Show_student.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.Up_student.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
    # retranslateUi

