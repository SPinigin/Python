from model import GameModel
from view import GameView
from controller import GameController

if __name__ == "__main__":
    # Load questions from the JSON file
    json_file = 'questions.json'

    # Initialize the model, view, and controller
    model = GameModel(json_file)
    view = GameView()
    controller = GameController(model, view)

    # Start the game
    controller.start_game()
