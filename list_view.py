from PyQt5.QtWidgets import QTreeView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import pandas as pd


class ListView(QTreeView):
    def __init__(self, path):
        super().__init__()

        df = pd.read_excel(path)
        items = []

        self.__itemsToShow = ''
        
        for index,row in df.iterrows():
            if(self.__itemsToShow in df.columns and row[self.__itemsToShow]=='y'):
                items.append([QStandardItem(row['Name']), QStandardItem(row['Extension'])])

        model = QStandardItemModel()
        model.setColumnCount(2)
        model.setHorizontalHeaderLabels(["Name", "Type"])
        
        for item in items:
            model.appendRow(item)

        self.setModel(model)

    def setItemsToShow(self, name):
        self.__itemsToShow = name