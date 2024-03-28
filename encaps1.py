class item:
    def __init__(self, name,price,quantity,promocode):
        self.name = name
        self.price = price
        self._quantity = quantity
        self.__promocode = promocode
        
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_quantity(self):
        return self._quantity
    def get_promocode(self):
        return self.__promocode
    
    def set_name(self,new_name):
        self.name = new_name
    def set_price(self,new_price):
        self.price = new_price
    def set_quantity(self,new_quantity):
        self._quantity = new_quantity
    def set_promo(self,new_promo):
        self.__promocode = new_promo

obj = item("bangles","450","2","archu50")
print("the Item name is  :",obj.get_name())
print("the item price is :",obj.get_price())
print("item quantity is :",obj.get_quantity())
print("promo available :" , obj.get_promocode())

obj.set_name("manoj")
print("updated name :",obj.get_name())
