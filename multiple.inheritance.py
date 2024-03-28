class TravelDetails:
    def __init__(self, place, food, weather, hotel, visit_place, climate):
        self.place = place
        self.food = food
        self.weather = weather
        self.hotel = hotel
        self.visit_place = visit_place
        self.climate = climate

class Visa(TravelDetails):
    def south_korea(self, place, food, weather):
        super().__init__(place, food, weather)

class Visa1(TravelDetails):
    def Russia(self, hotel, visit_place, climate):
        super().__init__(hotel, visit_place, climate)

class VisitDate(Visa, Visa1):
    def __init__(self, date_SK,place,food,weather,date_R,hotel,visit_place,climate,):
        super.__init__(date_SK, place, food, weather, date_R, hotel, visit_place, climate)
        self.date_SK = date_SK
        self.date_R = date_R

    def display_details(self):
        print("South korea travel date is:",self.date_SK)
        print("planing to visit the place is:",self.place)
        print("planing to eat a food is:", self.food)
        print("weather is:", self.weather)
        print("Russia travel date is:",self.date_R)
        print("planing to stay is:",self.hotel)
        print("planing to visit the place is:",self.visit_place)
        print("Climate is:", self.climate)
        
ob = VisitDate("29th feb","seaoul","kimchi","cold","8th march","moscow","altay","winter")
ob.display_details()
