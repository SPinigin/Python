from PyQt6.QtWidgets import QWidget, QVBoxLayout, QComboBox, QPushButton


class AirportView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Airport To Map")
        self.layout = QVBoxLayout()

        self.country_combo = QComboBox()
        self.layout.addWidget(self.country_combo)

        self.city_combo = QComboBox()
        self.layout.addWidget(self.city_combo)

        self.airport_combo = QComboBox()
        self.layout.addWidget(self.airport_combo)

        self.show_button = QPushButton("Show Airport on Map")
        self.layout.addWidget(self.show_button)

        self.setLayout(self.layout)

    def populate_countries(self, countries):
        self.country_combo.clear()
        self.country_combo.addItems(countries)

    def populate_cities(self, cities):
        self.city_combo.clear()
        self.city_combo.addItems(cities)

    def populate_airports(self, airports):
        self.airport_combo.clear()
        self.airport_combo.addItems(airports)
