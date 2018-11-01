from fetch_data import fetch_data
from data_extractor import build_question
from cli import cli, fix_question


if __name__ == '__main__':

    data = list(fetch_data("List of Hi-NRG artists and songs"))
    questions = [build_question(data) for i in range(5)]
    # print('questions1', questions)
    questions = [fix_question(data) for data in questions]
    # print('questions2', questions)
    cli(questions)
