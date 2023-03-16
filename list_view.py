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
            if(itemsToShow in df.columns and row[itemsToShow]=='y'):
                path = row['Path']
                name = QStandardItem(row['Name'])
                name.setFlags(name.flags() & ~Qt.ItemIsEditable)
                name.setData(path)
                ext = QStandardItem(row['Extension'])
                ext.setFlags(ext.flags() & ~Qt.ItemIsEditable)
                ext.setData(path)
                path = QStandardItem(path)
                path.setFlags(path.flags() & ~Qt.ItemIsEditable)
                path.setData = path
                items.append([name, ext, path])

        self.__model.clear()
        self.__model.setColumnCount(3)
        self.__model.setHorizontalHeaderLabels(["Name", "Type", "Path"])

        for item in items:
            self.__model.appendRow(item)
