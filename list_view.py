from PyQt5.QtWidgets import QTreeView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import pandas as pd


class ListView(QTreeView):
    def __init__(self, path):
        super().__init__()

        self.__path = path
        self.__model = QStandardItemModel()
        
        
        self.updateModel('')

        self.setModel(self.__model)

    def updateModel(self, itemsToShow):
        df = pd.read_excel(self.__path)
        items = []
        
        for index,row in df.iterrows():
            if(itemsToShow in df.columns and row[itemsToShow]=='y'):
                items.append([QStandardItem(row['Name']), QStandardItem(row['Extension'])])

        self.__model.clear()
        self.__model.setColumnCount(2)
        self.__model.setHorizontalHeaderLabels(["Name", "Type"])
        
        for item in items:
            self.__model.appendRow(item)
