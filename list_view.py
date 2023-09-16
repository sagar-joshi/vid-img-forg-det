from PyQt5.QtWidgets import QTreeView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtCore import Qt
import pandas as pd


class ListView(QTreeView):
    def __init__(self, path):
        super().__init__()

        self.__path = path
        self.__model = QStandardItemModel()
        
        
        self.updateModel('')

        self.setModel(self.__model)

    def getModel(self):
        return self.__model

    def updateModel(self, itemsToShow):
        df = pd.read_excel(self.__path)
        items = []
        
        for index,row in df.iterrows():
            if(itemsToShow in df.columns and row[itemsToShow]==1):
                pathText = row['Path']
                forgTypeText = 'Insertion' if row['Insertion Forgery']==1 else 'Deletion'
                forgType = QStandardItem(forgTypeText)
                forgType.setFlags(forgType.flags() & ~Qt.ItemIsEditable)
                forgType.setData(forgTypeText)
                # ext = QStandardItem(row['Extension'])
                # ext.setFlags(ext.flags() & ~Qt.ItemIsEditable)
                # ext.setData(pathText)
                path = QStandardItem(pathText)
                path.setFlags(path.flags() & ~Qt.ItemIsEditable)
                path.setData(pathText)
                items.append([path, forgType])

        self.__model.clear()
        self.__model.setColumnCount(2)
        self.__model.setHorizontalHeaderLabels(["Path", "Forgery Type"])

        for item in items:
            self.__model.appendRow(item)
