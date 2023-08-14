from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QWidget, QPushButton, QStyle, QVBoxLayout, QHBoxLayout, QSlider)
 
class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
 
        self.__mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
 
        self.__playButton = QPushButton()
        self.__playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.__playButton.clicked.connect(self.__play)

        self.__positionSlider = QSlider(Qt.Horizontal)
        self.__positionSlider.setRange(0, 0)
        self.__positionSlider.sliderMoved.connect(self.__setPosition)

        hLayout = QHBoxLayout()
        hLayout.addWidget(self.__playButton, stretch=1)
        hLayout.addWidget(self.__positionSlider, stretch=14)
        control = QWidget()
        control.setLayout(hLayout)
  
        vLayout = QVBoxLayout()
        vLayout.addWidget(videoWidget, stretch=9)
        vLayout.addWidget(control, stretch=1)
 
        self.setLayout(vLayout)

        self.__mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(None)))
        self.__mediaPlayer.setVideoOutput(videoWidget)
        self.__mediaPlayer.positionChanged.connect(self.__positionChanged)
        self.__mediaPlayer.durationChanged.connect(self.__durationChanged)
        
    
 
    def __play(self):
        if self.__mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.__mediaPlayer.pause()
            self.__playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.__mediaPlayer.play()
            self.__playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def __setPosition(self, position):
        self.__mediaPlayer.setPosition(position)

    def __positionChanged(self, position):
        self.__positionSlider.setValue(position)

    def __durationChanged(self, duration):
        self.__positionSlider.setRange(0, duration)

    def __free_media(self):
        self.__mediaPlayer.setMedia(QMediaContent())  

    def updateMedia(self, path):
        self.__free_media()
        self.__mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
        self.__mediaPlayer.play()
