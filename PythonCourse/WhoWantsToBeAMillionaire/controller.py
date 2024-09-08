class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start_game(self):
        self.view.display_welcome_message()

        while not self.model.is_game_over():
            question = self.model.get_current_question()
            if not question:
                break

            self.view.display_question(question)
            user_input = self.view.get_user_input()

            try:
                answer_index = int(user_input) - 1
                if 0 <= answer_index < len(question.options):
                    selected_answer = question.options[answer_index]
                    if self.model.check_answer(selected_answer):
                        self.view.display_correct_answer()
                    else:
                        self.view.display_incorrect_answer()
                        break
                else:
                    print("Некорректный выбор. Необзодимо ввести цифру от 1 до 4\n")
            except ValueError:
                print("Некорректный ввод. Попробуйте еще раз.\n")

        self.view.display_game_over(self.model.get_total_prize())
