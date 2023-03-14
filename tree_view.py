from PyQt5.QtWidgets import QTreeView, QFileSystemModel
from PyQt5.QtCore import QDir

class TreeView(QTreeView):
    def __init__(self):
        super().__init__()

        model = QFileSystemModel()
        model.setRootPath('')
        model.setFilter(QDir.Dirs | QDir.NoDotAndDotDot)
        self.setModel(model)
        self.setColumnHidden(1,True)
        self.setColumnHidden(2,True)
        self.setColumnHidden(3,True)
    
