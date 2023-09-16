from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFileSystemModel
from media_player import VideoPlayer
from tree_view import TreeView
from list_view import ListView
from vid_forg_localiz import get_localized_video

class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.__videoplayer = VideoPlayer()
        self.__videoplayer2 = VideoPlayer()
        self.__treeview = TreeView()
        self.__treeview.clicked.connect(self.__tree_viewClicked)
        self.__listview = ListView("./mock_data.xlsx")
        self.__listview.doubleClicked.connect(self.__listviewClicked)
        hbox = QHBoxLayout()
        hbox.addWidget(self.__treeview, stretch=1)
        hbox.addWidget(self.__listview, stretch=3)
        widget = QWidget()
        widget.setLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.__videoplayer, stretch=1)
        hbox.addWidget(self.__videoplayer2, stretch=1)
        widget2 = QWidget()
        widget2.setLayout(hbox)
        vbox = QVBoxLayout()
        vbox.addWidget(widget, stretch=2)
        vbox.addWidget(widget2, stretch=3)
        self.setLayout(vbox)

    def __tree_viewClicked(self, index):
        model = self.__treeview.getModel()
        item = model.itemFromIndex(index)
        itemText = item.text()
        self.__listview.updateModel(itemText)

    def __listviewClicked(self, index):
        model = self.__listview.getModel()
        row = index.row()
        rowItems=[]
        for col in range(model.columnCount()):
            rowItems.append(model.item(row, col))
        # item = model.itemFromIndex(index)
        # print(item.data())
        videoPath = rowItems[0].data()
        forgType = rowItems[1].data()
        localizedVideoPath = get_localized_video(videoPath, forgType)
        self.__videoplayer.updateMedia(videoPath)
        self.__videoplayer2.updateMedia(localizedVideoPath)
             
