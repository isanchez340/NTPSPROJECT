class hookList(object):

    def __init__(self):
        self.HookList = list()

    def addHook(self, Hook):
        self.HookList.append(Hook)

    def removeHook(self, Hook):
        self.HookList.remove(Hook)

    def searchHook(self, searchName):
        for Hook in self.HookList:
            if(Hook.HookName is searchName):
                print(Hook.HookName) #<- va como se conecta al GUI para hacer display

    def printL(self):
        for Hook in self.HookList:
            print(Hook.HookName)

    def sortList(self, order):
        if(order is "ascending"):
            self.HookList.sort(key=lambda x: x.HookName)
        if(order is "descending"):
            self.HookList.sort(key=lambda x: x.HookName, reverse=True)
