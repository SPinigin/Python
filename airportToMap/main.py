import sys
from PyQt6.QtWidgets import QApplication
from AirportModel import AirportModel
from AirportView import AirportView
from AirportController import AirportController


def main():
    app = QApplication(sys.argv)

    model = AirportModel()
    view = AirportView()
    controller = AirportController(model, view)

    view.controller = controller
    model.load_airports("airports.json")

    view.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
