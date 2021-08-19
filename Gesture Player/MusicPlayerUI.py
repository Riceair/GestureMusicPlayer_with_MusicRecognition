# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MusicPlayerUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PlayListGenerator import PlayListGenerator
from DataRecorder import DataRecorder
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from MusicControler import MusicControler
import mediapipe as mp
import numpy as np
import HandTrackingModule as htm
from GestureRecognizer import GestureRecognizer
import threading
import time
import sys
import os
import cv2


class Ui_GesturePlayer(object):
    def setupUi(self, GesturePlayer):
        GesturePlayer.setObjectName("GesturePlayer")
        GesturePlayer.resize(591, 332)
        self.centralwidget = QtWidgets.QWidget(GesturePlayer)
        self.centralwidget.setObjectName("centralwidget")
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setGeometry(QtCore.QRect(30, 230, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(36)
        self.prevButton.setFont(font)
        self.prevButton.setObjectName("prevButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(390, 230, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(36)
        self.nextButton.setFont(font)
        self.nextButton.setCheckable(False)
        self.nextButton.setObjectName("nextButton")
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(220, 270, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(18)
        self.pauseButton.setFont(font)
        self.pauseButton.setObjectName("pauseButton")
        self.songName = QtWidgets.QLabel(self.centralwidget)
        self.songName.setGeometry(QtCore.QRect(120, 150, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        self.songName.setFont(font)
        self.songName.setAlignment(QtCore.Qt.AlignCenter)
        self.songName.setObjectName("songName")
        self.className = QtWidgets.QLabel(self.centralwidget)
        self.className.setGeometry(QtCore.QRect(190, 70, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.className.setFont(font)
        self.className.setAlignment(QtCore.Qt.AlignCenter)
        self.className.setObjectName("className")
        self.styleButton = QtWidgets.QPushButton(self.centralwidget)
        self.styleButton.setGeometry(QtCore.QRect(220, 230, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(12)
        self.styleButton.setFont(font)
        self.styleButton.setObjectName("styleButton")
        self.gestureUse = QtWidgets.QCheckBox(self.centralwidget)
        self.gestureUse.setGeometry(QtCore.QRect(20, 60, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.gestureUse.setFont(font)
        self.gestureUse.setObjectName("gestureUse")
        self.cameraNum = QtWidgets.QLineEdit(self.centralwidget)
        self.cameraNum.setGeometry(QtCore.QRect(170, 30, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.cameraNum.setFont(font)
        self.cameraNum.setObjectName("cameraNum")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        GesturePlayer.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(GesturePlayer)
        self.statusbar.setObjectName("statusbar")
        GesturePlayer.setStatusBar(self.statusbar)
        ##各種GUI的設定
        self.retranslateUi(GesturePlayer)
        QtCore.QMetaObject.connectSlotsByName(GesturePlayer)

        #限制Camera Numer的輸入
        regex = QtCore.QRegExp("[0-9]")
        validator = QtGui.QRegExpValidator(regex,self.cameraNum)
        self.cameraNum.setValidator(validator)
        self.__setEventListener()

    def retranslateUi(self, GesturePlayer):
        ##GUI的設定
        self._translate = QtCore.QCoreApplication.translate
        GesturePlayer.setWindowTitle(self._translate("GesturePlayer", "MainWindow"))
        self.prevButton.setText(self._translate("GesturePlayer", "Prev"))
        self.nextButton.setText(self._translate("GesturePlayer", "Next"))
        self.pauseButton.setText(self._translate("GesturePlayer", "Play"))
        self.songName.setText(self._translate("GesturePlayer", "Press Play to start"))
        self.className.setText(self._translate("GesturePlayer", ""))
        self.styleButton.setText(self._translate("GesturePlayer", "Style Change"))
        self.gestureUse.setText(self._translate("GesturePlayer", "Gesture"))
        self.cameraNum.setText(self._translate("GesturePlayer", "0"))
        self.label.setText(self._translate("GesturePlayer", "Camera Number:"))

        self.isGesThreadRun=False #手勢辨識執行續的開關
        self.__PlayerSetting() #設置Music Player

    def __setEventListener(self): #設定按鈕的event listener
        self.nextButton.clicked.connect(self.__nextPress)
        self.prevButton.clicked.connect(self.__prevPress)
        self.pauseButton.clicked.connect(self.__pausePress)
        self.styleButton.clicked.connect(self.__stylePress)
        self.gestureUse.clicked.connect(self.__gesturePress)
        self.cameraNum.textChanged.connect(self.__camCheck)
    
    def __PlayerSetting(self): #設置Music Player
        data_init = DataRecorder() #初始化音樂設定 (分類清單建立)
        data_init.startRecord()
        self.__setButtonEnable(False)
        self.cameraNum.setEnabled(False)
        self.gestureUse.setEnabled(False)

        if len(os.listdir("music"))==0: #若沒有歌曲就顯示
            self.songName.setText(self._translate("GesturePlayer", "Please add music in music folder"))
            return
        self.playlist_generator = PlayListGenerator()
        self.music_controler = MusicControler()
        self.__stylePress()
        self.__pausePress()

        self.__setButtonEnable(True)
        self.cameraNum.setEnabled(True)
        self.gestureUse.setEnabled(True)

    def __camCheck(self):
        cam_num = self.cameraNum.text()
        if cam_num=="":
            self.gestureUse.setEnabled(False)
        else:
            self.gestureUse.setEnabled(True)

    def __gesturePress(self): #是否使用手勢操作
        if self.gestureUse.isChecked():
            self.cameraNum.setEnabled(False)
            self.__setButtonEnable(False)

            self.isGesThreadRun=True #開啟手勢辨識的執行續
            t = threading.Thread(target=self.__gestureThreadJob)
            t.start()
        elif not self.gestureUse.isChecked():
            self.cameraNum.setEnabled(True)
            self.__setButtonEnable(True)

            self.isGesThreadRun=False #關閉手勢辨識的執行續

    def __setButtonEnable(self,isEnable):
        self.nextButton.setEnabled(isEnable)
        self.prevButton.setEnabled(isEnable)
        self.pauseButton.setEnabled(isEnable)
        self.styleButton.setEnabled(isEnable)

    def __nextPress(self):
        self.music_controler.music_next()
        self.songName.setText(self._translate("GesturePlayer", self.music_controler.getCurrentName()[6:]))
        self.pauseButton.setText(self._translate("GesturePlayer", "Pause"))

    def __prevPress(self):
        self.music_controler.music_prev()
        self.songName.setText(self._translate("GesturePlayer", self.music_controler.getCurrentName()[6:]))
        self.pauseButton.setText(self._translate("GesturePlayer", "Pause"))
    
    def __pausePress(self):
        self.music_controler.music_pause()
        if self.music_controler.get_isPause():
            self.pauseButton.setText(self._translate("GesturePlayer", "Play"))
        else:
            self.pauseButton.setText(self._translate("GesturePlayer", "Pause"))
    
    def __stylePress(self):
        style, self.playlist = self.playlist_generator.getPlayList()
        self.music_controler.clear_music_list()
        self.music_controler.add_music_list(self.playlist)
        self.music_controler.music_play()

        self.className.setText(self._translate("GesturePlayer", style))
        self.songName.setText(self._translate("GesturePlayer", self.music_controler.getCurrentName()[6:]))


    def __gestureThreadJob(self):
        try:
            cam_num = int(self.cameraNum.text())
            cap = cv2.VideoCapture(cam_num)
            detector = htm.handDetector()
            gRecognizer = GestureRecognizer()
            PLAY_PAUSE = 0
            NEXT = 1
            PREV = 2
            STYLE_CHANGE = 3

            ###由於辨識會出現辨識錯誤的情形，因此需要連續出現一定的次數才判定為正確手勢
            current_gesture = 0 #紀錄當前的手勢
            gesture_appear_times = 0 #紀錄當前手勢出現的次數
            TRUE_APPEAR_TIMES = 50 #連續出現n個frame判為正確
            while self.isGesThreadRun:
                success, img = cap.read()
                img = detector.findHands(img, draw=True )
                lmList = detector.findPosition(img, draw=False)
                if len(lmList) != 0:
                    gesture = gRecognizer.getGestureType(lmList)
                    if gesture is not None:
                        if current_gesture != gesture: #若發現為不同手勢重新計次
                            current_gesture = gesture
                            gesture_appear_times = 1
                        elif current_gesture == gesture: #發現為相同手勢計次
                            gesture_appear_times += 1
                        
                        if gesture_appear_times==TRUE_APPEAR_TIMES: #到達累計次數
                            if current_gesture==PLAY_PAUSE:
                                self.__pausePress()
                            elif current_gesture==NEXT:
                                self.__nextPress()
                            elif current_gesture==PREV:
                                self.__prevPress()
                            elif current_gesture==STYLE_CHANGE:
                                self.__stylePress()
                            gesture_appear_times = 0
                            time.sleep(5)
            cap.release()
            cv2.destroyAllWindows()
            print("Thread End")
        except:
            cap.release()
            cv2.destroyAllWindows()
            self.gestureUse.setChecked(False)
            self.__gesturePress() #開啟失敗，關閉相機

if __name__ == '__main__':  
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_GesturePlayer()

    ui.setupUi(MainWindow) 
    MainWindow.show()
    sys.exit(app.exec_())