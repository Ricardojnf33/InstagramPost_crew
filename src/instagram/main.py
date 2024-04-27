#!/usr/bin/env python
from instagram.crew import InstagramCrew
import datetime

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'current_date': datetime.datetime.now().strftime("%Y-%m-%d"),
        'instagram_description': input('Escreva a descrição da página aqui: '),
        'topic_of_the_week': input('Escreva o tópico da semana aqui: '),
    }
    InstagramCrew().crew().kickoff(inputs=inputs)