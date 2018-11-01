from fetch_data import fetch_data
from data_extractor import build_question
from cli import cli


data = fetch_data("List of Hi-NRG artists and songs")
questions = [build_question(data) for i in range(5)]
cli(questions)
