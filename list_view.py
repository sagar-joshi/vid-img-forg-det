from PyQt5.QtWidgets import QListView, QFileSystemModel
from PyQt5.QtCore import QSize

class ListView(QListView):
    def __init__(self):
        super().__init__()
        self.__model = QFileSystemModel()
        self.__model.setRootPath("")
        self.setModel(self.__model)
        self.setRootIndex(self.__model.index(""))
        self.setViewMode(QListView.IconMode)
        self.setIconSize(QSize(60, 60))
        self.setUniformItemSizes(True)
    
    def updateRootIndex(self, path):
        self.setRootIndex(self.__model.index(path))
        