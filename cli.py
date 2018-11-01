import random
import time

import click


questions = [
    {
        'question': 'What is the capital of the UK',
        'answers': ['London', 'Manchester', 'Birmingham']
    }
]

def cli(questions):
    for question in questions:
        answers = question['answers']
        correct_answer = answers[0]
        random.shuffle(answers)

        choices = range(1, len(answers) + 1)
        while True:
            click.echo()
            click.echo(f"{question['question']}?")
            for i, a in enumerate(answers, start=1):
                click.echo(f'{i}. {a}')

            response = click.prompt('Please enter a choice', type=int)

            if response not in choices:
                click.echo(
                    f"Invalid value, please enter a value in {list(choices)}"
                )
                continue

            chosen = answers[response - 1]
            if chosen == correct_answer:
                click.echo('CORRECT!')
                break
            else:
                click.echo('WRONG!')

            time.sleep(1)
