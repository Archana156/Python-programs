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
    def __init__(self, date_SK, place, food, weather, date_R, hotel, visit_place, climate):
        super().__init__(place, food, weather, hotel, visit_place, climate)
        self.date_SK = date_SK
        self.date_R = date_R

    def display_details(self):
        print("South Korea travel date is:", self.date_SK)
        print("Planning to visit the place is:", self.place)    
        print("Planning to eat food is:", self.food)
        print("Weather is:", self.weather)
        print("Russia travel date is:", self.date_R)
        print("Planning to stay at:", self.hotel)
        print("Planning to visit the place is:", self.visit_place)
        print("Climate is:", self.climate)

ob = VisitDate("29th Feb", "Seoul,city", "Kimchi", "Cold", "8th March", "Moscow", "Altay", "Winter")
ob.display_details()
