from pytube import YouTube
import csv
import sys
import traceback
from datetime import datetime

cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m'
}

line_count = 0
inicio = datetime.now()

with open('musicas.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        try:
            # print(f'Tentando baixar: {row[0]} --> {row[1]}')
            yt = YouTube(row[2])
            # print(f'Baixando: {yt.title}')
            
            yt.streams.get_highest_resolution().download('/home/victor/Área de Trabalho/testevideos/musicas_mp4/')

            print('Linha: {} --> {}OK{}'.format(line_count, cores['verde'], cores['limpa']))
        
        except:
            print('Linha: {} --> {}ERRO!{}. url: {}'.format(line_count, cores['vermelho'], cores['limpa'], row[2]))
            # print(sys.exc_info()[0])
            # print(traceback.print_exc())

        finally:
            line_count += 1
print(f'Finalizado, Tempo: {datetime.now() - inicio}')