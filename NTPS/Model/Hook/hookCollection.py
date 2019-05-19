from Model.Hook import hook
from Model.Hook.hookList import hookList

class hookCollection(object):
    HookCollectionName = ""
    HookCollectionDescription = ""
    HookCollectionStatus = ""
    HookCollectionSequenceNumber = 0
    list = hookList()

    def __init__(self, HookCollectionName, HookCollectionDescription, HookCollectionStatus, HookCollectionSequenceNumber):
        print("created")
        self.HookCollectionName = HookCollectionName
        self.HookCollectionDescription = HookCollectionDescription
        self.HookCollectionStatus = HookCollectionStatus
        self.HookCollectionSequenceNumber = HookCollectionSequenceNumber

    def changeCollectionStatus(self, collectionStatus):
        self.HookCollectionStatus = collectionStatus

    def editCollectionHook(self, collectionName, collectionDescription, collectionExecutionSequence):
        if(self.HookCollectionName is not collectionName):
            self.HookName = collectionName
        if(self.HookCollectionDescription is not collectionDescription):
            self.HookCollectionDescription = collectionDescription
        if(self.HookCollectionSequenceNumber  is not collectionExecutionSequence):#y si ya esta ocupado?
            self.HookCollectionSequenceNumber = collectionExecutionSequence

    def addHookToCollection(self, hook):
        
        self.list.addHook(hook)
        hook.editHookAssociation("add")

    def removeHookToCollection(self, hook):
        self.list.removeHook(hook)
        hook.editHookAssociation("remove")
