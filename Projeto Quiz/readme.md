A estrutura mínima recomendável para om json é um arquivo json com um array de objetos, cada objeto representando uma pergunta. Cada pergunta deve ter um campo com a pergunta, um campo com as alternativas e um campo com a resposta correta, e a dificuldade da pergunta. Exemplo:
```json
[
    {
        "question": "Qual é a capital do Brasil?",
        "options": ["São Paulo", "Rio de Janeiro", "Brasília", "Belo Horizonte"],
        "correctAnswer": "Brasília",
        "dificulty": "easy"
    },
    {
        "question": "Qual é a capital do Japão?",
        "options": ["Tóquio", "Osaka", "Nagoya", "Yokohama"],
        "correctAnswer": "Tóquio"
        "dificulty": "medium"
    }
]
```