import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data')
DEFAULT_JSON_FILE = 'perguntas.json'
NUM_QUESTIONS_PER_QUIZ = 10  # Quantas perguntas o quiz deve ter
