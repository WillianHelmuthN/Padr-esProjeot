import tkinter as tk
from gerador import QuizManager, UIController

def start_quiz():
    quiz_manager = QuizManager.get_instance()
    quiz_manager.load_questions_from_json("questions.json")
    print(f"Total de perguntas carregadas: {len(quiz_manager.questions)}")

    # Inicia a interface gráfica
    app = UIController(quiz_manager.questions)
    app.start()

if __name__ == "__main__":
    start_quiz()