from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFileSystemModel
from media_player import VideoPlayer
from tree_view import TreeView
from list_view import ListView

class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.__videoplayer = VideoPlayer()
        self.__treeview = TreeView()
        self.__treeview.clicked.connect(self.__tree_viewClicked)
        self.__list_view = ListView()
        self.__list_view.doubleClicked.connect(self.__list_viewClicked)
        vbox = QVBoxLayout()
        vbox.addWidget(self.__list_view, stretch=1)
        vbox.addWidget(self.__videoplayer, stretch=2)
        widget = QWidget()
        widget.setLayout(vbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.__treeview, stretch=1)
        hbox.addWidget(widget, stretch=3)
        self.setLayout(hbox)

    def __tree_viewClicked(self, index):
        model = self.__treeview.getModel()
        item = model.itemFromIndex(index)
        itemText = item.text()
        self.__list_view.setItemsToShow(itemText)

    def __list_viewClicked(self, index):
        self.__videoplayer.updateMedia(QFileSystemModel().filePath(index))
             
