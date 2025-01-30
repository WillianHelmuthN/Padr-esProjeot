"""
Este módulo contém classes e funções para gerenciar um quiz.
Inclui classes para representar perguntas, carregar perguntas de um arquivo JSON,
gerenciar a pontuação e controlar a interface gráfica do usuário.
"""

import json
from tkinter import Tk, Label, Button, Radiobutton, StringVar, Frame

#Factory Method
class Question:
    """Classe para representar uma pergunta."""
    def __init__(self, text, options, correct_answer, difficulty):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
        self.difficulty = difficulty
    
    @staticmethod
    def from_dict(data):
        return Question(data['question'], data['options'], data['correctAnswer'], data['difficulty'])

#Template Method
class QuestionParser:
    """Classe para carregar perguntas de um arquivo JSON."""
    @staticmethod
    def load_questions_from_json(path):
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return [Question.from_dict(q) for q in data['questions']]

#Singleton
class ScoreManager:
    """Classe que lida com o Score"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ScoreManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.score = 0
    
    def update_score(self, correct):
        if correct:
            self.score += 1

    def get_final_score(self):
        return self.score

#Singleton
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

#MVC
class UIController:
    """Classe para controlar a interface gráfica do usuário."""
    def __init__(self, questions):
        self.window = Tk()q
        self.window.geometry("800x260")
        self.questions = questions
        self.current_question_index = 0
        self.user_answer = StringVar(self.window)
        self.score_manager = ScoreManager()
        self.window.title("Quiz App")
        self.question_label = Label(self.window, text="")
        self.question_label.pack()
        self.options_buttons = []

        self.frame = Frame(self.window)
        self.frame.pack(expand=True)

        self.question_label = Label(self.frame, text="")
        self.question_label.pack(pady=20)
        for i in range(4):
            btn = Radiobutton(self.window, text="", variable=self.user_answer, value=str(i))
            btn.pack()
            self.options_buttons.append(btn)
        
        self.submit_button = Button(self.window, text="Responder", command=self.check_answer)
        self.submit_button.pack()

    def show_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.config(text=question.text)
            for i, option in enumerate(question.options):
                self.options_buttons[i].config(text=option, value=option)
        else:
            self.show_results()

    def check_answer(self):
        question = self.questions[self.current_question_index]
        correct = self.user_answer.get() == question.correct_answer
        self.score_manager.update_score(correct)
        self.current_question_index += 1
        self.show_question()

    def show_results(self):
        score = self.score_manager.get_final_score()
        self.question_label.config(text=f"Quiz finalizado! Pontuação: {score}")
        for btn in self.options_buttons:
            btn.pack_forget()
        self.submit_button.pack_forget()
    
    def start(self):
        self.show_question()
        self.window.mainloop()