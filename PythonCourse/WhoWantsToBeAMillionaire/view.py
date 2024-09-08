class GameView:
    def display_welcome_message(self):
        print("Welcome to 'Who Wants to Be a Millionaire? - Python Edition'!")
        print("Answer Python-related questions to win up to 1,000,000 rubles!")

    def display_question(self, question):
        print(f"Question for {question.prize} rubles:")
        print(question.question_text)
        for i, option in enumerate(question.options, 1):
            print(f"{i}. {option}")

    def get_user_input(self):
        return input("Please select an option (1-4): ")

    def display_correct_answer(self):
        print("Correct! Moving on to the next question.\n")

    def display_incorrect_answer(self):
        print("Incorrect! Game over.\n")

    def display_total_prize(self, prize):
        print(f"Congratulations! You've won {prize} rubles!\n")

    def display_game_over(self, total_prize):
        print(f"Game over. You've won a total of {total_prize} rubles.")
