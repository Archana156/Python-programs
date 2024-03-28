class products:
    def __init__(self,sarees,cosmetics,kitchenitems,kurtis,watches):
        self.sarees = sarees
        self.cosmetics = cosmetics
        self.kitchenitems= kitchenitems
        self.kurtis = kurtis
        self.watches = watches
        
class saree(products):
    def price(self,sarees):
        self.__price = self.sarees
    def types(self,cotton,silk):
        self.cotton = cotton
        self.silk = silk
    



        