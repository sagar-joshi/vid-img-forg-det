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
        self.__listview = ListView("./mock_data.xlsx")
        self.__listview.doubleClicked.connect(self.__listviewClicked)
        hbox = QHBoxLayout()
        hbox.addWidget(self.__treeview, stretch=1)
        hbox.addWidget(self.__listview, stretch=3)
        widget = QWidget()
        widget.setLayout(hbox)
        vbox = QVBoxLayout()
        vbox.addWidget(widget, stretch=2)
        vbox.addWidget(self.__videoplayer, stretch=3)
        self.setLayout(vbox)

    def __tree_viewClicked(self, index):
        model = self.__treeview.getModel()
        item = model.itemFromIndex(index)
        itemText = item.text()
        self.__listview.updateModel(itemText)

    def __listviewClicked(self, index):
        model = self.__listview.getModel()
        item = model.itemFromIndex(index)
        self.__videoplayer.updateMedia(item.data())
             
