
class ShoppingList2():
    #  Initialize the 3 A user
    ids = [1, 2, 3]
    names = ['zhang 3', 'li 4', 'Wang Wu']
    icons = ['root', 'abc123', '123456']

    def __init__(self) -> None:
        print("Objeto creado")

    def addItem(self, _id:int, _name:str, _icon:str) -> None:
        self.ids.append(_id)
        self.names.append(_name)
        self.icons.append(_icon)
        print("Se adicionó al objeto")

    def getList(self):
        print("mostrando la lista actual:")
        return self.ids,self.names,self.icons

    def getItem(self,_id):
        if( _id in self.ids):
            print(f"mostrando item {_id}")
            return self.ids[_id],self.names[_id],self.icons[_id]
        else:
            print("no encontrado")
            return None,None,None;

    def deleteItem(self,_id):
        if (_id in self.ids):
            print(f"Eliminando item {_id}")
            # Gets the subscript value
            index = self.ids.index(_id)
            self.ids.pop(index)
            self.names.pop(index)
            self.icons.pop(index)
            print("Delete the success ")
        else:
            print("no encontrado")
    def deleteAllItems(self):
        self.ids=[];
        self.names=[];
        self.icons=[];

class ShoppingItem():
    def __init__(self,_id,_name,_icon):
        self.id=_id;
        self.name=_name;
        self.icon=_icon;

    def __str__(self):
        return 'object: %s, %s, %s' % (self.id, self.name, self.icon)


class ShoppingList():
    lista=[];
    def __int__(self):
        pass
    #def __init__(self, shoppingItem:ShoppingItem):
    #    self.lista.append(shoppingItem);

    def addItem(self, shoppingItem:ShoppingItem) -> None:
        self.lista.append(shoppingItem)
        print("Se adicionó al objeto")

    def getList(self):
        print("mostrando la lista actual:")
        return self.lista

    def findItem(self,_id):
        print(f"buscando item con id: {_id}")
        for shoppingItem in self.lista:
            if(shoppingItem.id==_id):
                print("Se ha encontrado")
                return shoppingItem;
        print(f"no se ha encontrado item con id {_id}")
        return None;

    def getItem(self, _id):
        shoppingItem=self.findItem(_id)
        if (shoppingItem):
            print(f"mostrando item {_id}",shoppingItem)
            return shoppingItem;
        else:
            print("no encontrado")
            return None;

    def deleteItem(self, _id):
        shoppingItem = self.findItem(_id)
        if (shoppingItem):
            print(f"Eliminando item {_id}")
            # Gets the subscript value
            self.lista.remove(shoppingItem)
            print("Delete the success ")
        else:
            print("no encontrado")

    def deleteAllItems(self):
        self.lista = [];

