#!/usr/bin/env python
from instagram.crew import InstagramCrew
import datetime
import os

def create_report_directory():
    # Criar a pasta 'relatório' se ela não existir
    report_dir = 'relatórios'
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
        print(f"Pasta '{report_dir}' criada com sucesso.")

def run():
    # Crie o diretório de relatório antes de iniciar o processo
    create_report_directory()

    # Substitua com seus inputs, as informações de tarefas e agentes serão interpoladas automaticamente
    inputs = {
        'current_date': datetime.datetime.now().strftime("%Y-%m-%d"),
        'instagram_description': input('Escreva a descrição da página aqui: '),
        'topic_of_the_week': input('Escreva o tópico da semana aqui: '),
    }

    InstagramCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
