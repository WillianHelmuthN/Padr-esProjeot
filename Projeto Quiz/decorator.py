import json

class Decorator:
    def __init__(self, text, options, correct_answer, difficulty):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
        self.difficulty = difficulty
    
    @staticmethod
    def from_dict(data):
        return Question(data['question'], data['options'], data['correctAnswer'], data['difficulty'])
    
class QuestionParser:   
    @staticmethod
    def load_questions_from_json(path):
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return [Decorator.from_dict(q) for q in data['questions']]
    
class QuizManager:
    """Classe para gerenciar perguntas do quiz."""
    _instance = None

    def __init__(self):
        if QuizManager._instance is not None:
            raise Exception("Use get_instance() para acessar o QuizManager.")
        self.questions = []
        QuizManager._instance = self

    @staticmethod
    def get_instance():
        if QuizManager._instance is None:
            QuizManager()
        return QuizManager._instance

    def load_questions_from_json(self, json_file):
        self.questions = QuestionParser.load_questions_from_json(json_file)

    def add_question(self, question):
        if isinstance(question, Question):
            self.questions.append(question)
        else:
            raise TypeError("A pergunta deve ser uma instância da classe Question.")

    def get_question(self, index):
        if 0 <= index < len(self.questions):
            return self.questions[index]
        else:
            raise IndexError("Índice de pergunta fora do intervalo.")
    
def start_quiz():
    quiz_manager = QuizManager.get_instance()
    quiz_manager.load_questions_from_json("questions.json")
    print(f"Total de perguntas carregadas: {len(quiz_manager.questions)}")

if __name__ == "__main__":
    start_quiz()