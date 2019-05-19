
from Model.Hook import hookCollection


class hookCollectionList(object):

    def __init__(self):
        self.hookCollectionList = list()

    def addCollection(self, HookCollection):
        self.hookCollectionList.append(HookCollection)

    def removeCollection(self, HookCollection):
        self.hookCollectionList.remove(HookCollection)

    def searchCollection(self, searchName):
        for HookCollection in self.hookCollectionList:
            if(HookCollection.HookCollectionName is searchName):
                print(HookCollection.HookCollectionName) #va como se conecta al GUI para hacer display

    def printL(self):
        for HookCollection in self.hookCollectionList:
            print(HookCollection.HookCollectionName)

    def sortList(self, order):
        if(order is "ascending"):
            self.hookCollectionList.sort(key=lambda x: x.HookCollectionName)
        if(order is "descending"):
            self.hookCollectionList.sort(key=lambda x: x.HookCollectionName, reverse=True)
