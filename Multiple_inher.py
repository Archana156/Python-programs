class visa():
    def south_korea(self,place,food,weather):
        self.place = place
        self.food = food
        self.weather = weather

class visa1():
    def Russia(self,hotel,visit_place,climate):
        self.hotel = hotel
        self.visit_place = visit_place
        self.climate = climate
        
class visit_date(visa,visa1):
    def __init__(self,date) -> None:
        super().__init__()

        

