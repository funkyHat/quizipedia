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


def get_question(path):
    """
    {
        'song': '"Fly With the Wind"',
        'query': 'Year',
        'answers': [1978, 1979, 1982, 1709]
    }
    """
    with open(path) as f:
        data = eval(f.read())
        query = data.pop('query')
        answers = data.pop('answers')
        what, subject = list(data.items())[0]
        question = f"what {query} was the {what} {subject}?"
    return {
        "question": question,
        "answers": answers,
    }


if __name__ == '__main__':
    cli(questions)

    more_question = get_question('query_bundle.json')
    print(more_question)
    cli([more_question])
