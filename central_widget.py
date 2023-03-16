from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFileSystemModel
from PyQt5.QtCore import QModelIndex
from media_player import VideoPlayer
from tree_view import TreeView
from list_view import ListView

class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.__videoplayer = VideoPlayer()
        tree_view = TreeView()
        tree_view.clicked.connect(self.__tree_viewClicked)
        self.__list_view = ListView("./mock_data.xlsx")
        self.__list_view.doubleClicked.connect(self.__list_viewClicked)
        vbox = QVBoxLayout()
        vbox.addWidget(self.__list_view, stretch=1)
        vbox.addWidget(self.__videoplayer, stretch=2)
        widget = QWidget()
        widget.setLayout(vbox)
        hbox = QHBoxLayout()
        hbox.addWidget(tree_view, stretch=1)
        hbox.addWidget(widget, stretch=3)
        self.setLayout(hbox)

    def __tree_viewClicked(self, index: QModelIndex):
        if(QFileSystemModel().isDir(index)):
             self.__list_view.updateRootIndex(QFileSystemModel().filePath(index))

    def __list_viewClicked(self, index: QModelIndex):
        self.__videoplayer.updateMedia(QFileSystemModel().filePath(index))
             
