from PyQt5.QtWidgets import QTreeView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class TreeView(QTreeView):
    def __init__(self):
        super().__init__()

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderItem(0, QStandardItem(""))

        imgForensics = QStandardItem("Image Forensics")
        imgForensics.setEditable(False)
        normal = QStandardItem("Normal")
        normal.setEditable(False)
        copyMove = QStandardItem("Copy Move")
        copyMove.setEditable(False)
        splicing = QStandardItem("Splicing")
        splicing.setEditable(False)
        deepFake = QStandardItem("Deep Fake")
        deepFake.setEditable(False)
        vidForensics = QStandardItem("Video Forensics")
        vidForensics.setEditable(False)
        insertion = QStandardItem("Insertion Forgery")
        insertion.setEditable(False)
        deletion = QStandardItem("Deletion Forgery")
        deletion.setEditable(False)
        
        self.model.appendRow(imgForensics)
        self.model.appendRow(vidForensics)

        imgForensics.appendRow(normal)
        imgForensics.appendRow(deepFake)
        vidForensics.appendRow(insertion)
        vidForensics.appendRow(deletion)

        normal.appendRow(copyMove)
        normal.appendRow(splicing)

        self.setModel(self.model)


    
