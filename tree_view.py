from PyQt5.QtWidgets import QTreeView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class TreeView(QTreeView):
    def __init__(self):
        super().__init__()

        self.__model = QStandardItemModel()
        self.__model.setHorizontalHeaderLabels(["Name"])

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
        
        self.__model.appendRow(imgForensics)
        self.__model.appendRow(vidForensics)

        imgForensics.appendRow(copyMove)
        imgForensics.appendRow(splicing)
        vidForensics.appendRow(insertion)
        vidForensics.appendRow(deletion)


        self.setModel(self.__model)

    def getModel(self):
        return self.__model


    
