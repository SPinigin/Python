from PyQt6.QtCore import QObject, QUrl
from PyQt6.QtGui import QDesktopServices


class AirportController(QObject):
    def __init__(self, model, view):
        super().__init__()
        self.model = model
        self.view = view
        self.model.countries_loaded.connect(self.view.populate_countries)
        self.view.country_combo.currentIndexChanged.connect(self.get_cities)
        self.view.city_combo.currentIndexChanged.connect(self.get_airports)
        self.view.show_button.clicked.connect(self.show_on_map)

    def load_airports(self, filename):
        self.model.load_airports(filename)

    def get_cities(self):
        country = self.view.country_combo.currentText()
        cities = self.model.get_cities(country)
        self.view.populate_cities(cities)

    def get_airports(self):
        country = self.view.country_combo.currentText()
        city = self.view.city_combo.currentText()
        airports = self.model.get_airport_names(country, city)
        self.view.populate_airports(airports)

    def get_airport_coordinates(self, airport_name):
        return self.model.get_airport_coordinates(airport_name)

    def show_on_map(self):
        airport_name = self.view.airport_combo.currentText()
        coordinates = self.model.get_airport_coordinates(airport_name)
        url = f"https://www.google.com/maps/search/?api=1&query={coordinates}"
        QDesktopServices.openUrl(QUrl(url))
