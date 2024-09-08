import json

class Question:
    def __init__(self, question_text, options, correct_answer, prize):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer
        self.prize = prize

class GameModel:
    def __init__(self, json_file):
        self.questions = self.load_questions_from_json(json_file)
        self.current_index = 0
        self.total_prize = 0

    def load_questions_from_json(self, json_file):
        questions = []
        with open(json_file, 'r') as file:
            data = json.load(file)
            for item in data:
                question = Question(
                    item['question_text'],
                    item['options'],
                    item['correct_answer'],
                    item['prize']
                )
                questions.append(question)
        return questions

    def get_current_question(self):
        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        return None

    def check_answer(self, answer):
        current_question = self.questions[self.current_index]
        if answer == current_question.correct_answer:
            self.total_prize += current_question.prize
            self.current_index += 1
            return True
        return False

    def get_total_prize(self):
        return self.total_prize

    def is_game_over(self):
        return self.current_index >= len(self.questions)
