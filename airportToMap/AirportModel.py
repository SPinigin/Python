import json
from PyQt6.QtCore import QObject, pyqtSignal


class AirportModel(QObject):
    countries_loaded = pyqtSignal(list)
    cities_loaded = pyqtSignal(list)
    airports_loaded = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.airports = []

    def load_airports(self, filename):
        with open(filename, 'r') as file:
            self.airports = json.load(file)
            countries = sorted(set(airport['country'] for airport in self.airports))
            self.countries_loaded.emit(countries)

    def get_cities(self, country):
        cities = sorted(set(airport['city'] for airport in self.airports if airport['country'] == country))
        self.cities_loaded.emit(cities)
        return cities

    def get_airport_names(self, country, city):
        airports = [airport['airport'] for airport in self.airports if airport['country'] == country and airport['city'] == city]
        self.airports_loaded.emit(airports)
        return airports

    def get_airport_coordinates(self, airport_name):
        for airport in self.airports:
            if airport['airport'] == airport_name:
                return f"{airport['latitude']},{airport['longitude']}"
            