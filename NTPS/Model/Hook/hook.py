import importlib
import importlib.util

class hook(object):
    HookName = ""
    HookSequenceNumber = ""
    HookStatus = ""
    HookDescription = ""
    HookPath = ""
    HookAssociation = 0
    path = ''


    def __init__(self, HookName, HookDescription="l", HookPath="l", HookSequenceNumber=0, HookStatus=False):
        self.HookName = HookName
        self.HookSequenceNumber = HookSequenceNumber
        self.HookDescription = HookDescription
        self.HookStatus = HookStatus
        self.HookPath = HookPath

    def changeStatus(self, status):
        self.HookStatus = status

    def editHook(self, name, description="l", path="k"):
        if(self.HookName is not name):
            self.HookName = name
        if(self.HookDescription is not description):
            self.HookDescription = description
        if(self.HookPath is not path):
            self.HookPath = path

    def editHookAssociation(self, association):
        if(association is "add"):
            self.HookAssociation += 1
        if(association is "remove"):
            self.HookAssociation -= 1

    def print(self):
        print(self.HookName)


    def run(pk):
        file = 'script.py'
        hookT = importlib.util.spec_from_file_location(file, '/root/PycharmProjects/NTPS/Model/Hook/script.py')
        hookS = importlib.util.module_from_spec(hookT)
        hookT.loader.exec_module(hookS)
        Rhook = hookS.run(pk)
        return Rhook

