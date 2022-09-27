from Service import ShoppingList, ShoppingItem

def test1():
    item: ShoppingItem = None;
    shopLst = ShoppingList();
    shopLst.addItem(ShoppingItem(11, "nombre 11", "android"))
    shopLst.addItem(ShoppingItem(12, "nombre 12", "android"))
    shopLst.addItem(ShoppingItem(13, "nombre 13", "android"))
    shopLst.addItem(ShoppingItem(14, "nombre 14", "android"))
    shopLst.addItem(ShoppingItem(15, "nombre 15", "android"))
    print("-----")
    print(shopLst.getList())
    print("-----")
    item = shopLst.getItem(12)
    print("-----")
    shopLst.deleteItem(12)
    print("-----")
    print(shopLst.getList())
    print("-----")

def test2():
    shopLst = ShoppingList();
    for i in range(30):
        shopLst.addItem(ShoppingItem(i + 1, f"itemcito {i}", f"icon {i}"))
    #print(shopLst)
    print(shopLst.getItem(1))
test2();