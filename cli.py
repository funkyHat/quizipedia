import random

import click


questions = [
    {
        'question': 'What is the capital of the UK',
        'answers': ['London', 'Manchester', 'Birmingham']
    }
]

for question in questions:
    answers = question['answers']
    correct = answers[0]
    random.shuffle(answers)
    choices = range(1, len(answers) + 1)
    while True:
        click.echo(question['question'])
        for i, a in enumerate(answers, start=1):
            click.echo(f'{i}. {a}')

        value = click.prompt('Please enter a choice', type=int)

        if value not in choices:
            print("Invalid value, please enter a value in  {list(choices)}")