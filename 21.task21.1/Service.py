class ActiviItem():

    def __init__(self, _id=None, _name=None, _icon=None, _date=None):
        self.id = _id;
        self.name = _name;
        self.icon = _icon;
        self.date = _date;

    def __str__(self):
        return 'object: %s, %s, %s' % (self.id, self.name, self.icon)


class ActiviService():
    lista = [];

    def __int__(self):
        pass

    def addItem(self, activiItem: ActiviItem) -> None:
        self.lista.append(activiItem)
        print("Se adicionó al objeto")

    def getList(self):
        print("mostrando la lista actual:")
        return self.lista

    def findItem(self, _id):
        print(f"buscando item con id: {_id}")
        for activiItem in self.lista:
            if (activiItem.id == _id):
                print("Se ha encontrado")
                return activiItem;
        print(f"no se ha encontrado item con id {_id}")
        return None;

    def getItem(self, _id):
        activiItem = self.findItem(_id)
        if (activiItem):
            print(f"mostrando item {_id}", activiItem)
            return activiItem;
        else:
            print("no encontrado")
            return None;

    def deleteItem(self, _id):
        activiItem = self.findItem(_id)
        if activiItem:
            print(f"Eliminando item {_id}")
            # Gets the subscript value
            self.lista.remove(activiItem)
            print("Delete the success ")
        else:
            print("no encontrado")

    def deleteAllItems(self):
        self.lista = [];

    def getSequence(self):
        return len(self.lista) + 1
