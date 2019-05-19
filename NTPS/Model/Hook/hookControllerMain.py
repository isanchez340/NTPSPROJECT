from Model.Hook.hook import hook
from Model.Hook.hookList import hookList
from Model.Hook import hookCollection
from Model.Hook import hookCollectionList
#main tester
h1=hook("ahook1")
h2=hook("bhook2")
h3=hook("chook3")
h4=hook("dhook4")


lista=hookList()
lista.addHook(h1)
lista.addHook(h2)
lista.addHook(h3)
lista.addHook(h4)
lista.printL()

lista.sortList("descending")
lista.printL()


# hcl=hookCollection("collection1","test1", False, 1)
# hcl.addHookToCollection(h1)
# hcl.addHookToCollection(h2)
# hcl.removeHookToCollection(h2)
# hcl.list.printL()
#
# collectionList=hookCollectionList()
# collectionList.addCollection(hcl)
# print("colections:")
# collectionList.printL()
