# Importacoes
import time
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random
from algoritmos import insertionSort, selectionSort, mergeSort, heapSort
from utils import printList

instancias = [2000000, 1000000, 500000, 250000, 125000]
algoritmos = [insertionSort, selectionSort, mergeSort, heapSort]
distribuicoes = ['C', 'D', 'A', 'M'] # Crescente, Decrescente, Aleatório, 50% ordenado (respectivamente)

# Inicializa o array de dados
dados = {'algoritmo': [], 'instancia': [], 'distribuicao': [], 'tempo_execucao_s': [], 'tempo_execucao_ms': []}

# Percorre a lista de algoritmos
for algo in algoritmos:
    # Percorre a lista de instancias
    for inst in instancias:
        # Percorre a lista de distribuições
        for distrib in distribuicoes:
            if distrib == 'C': # Crescente
                dist = np.arange(inst)
            if distrib == 'D': # Decrescente
                dist = np.arange(inst)[::-1]
            if distrib == 'A': # Aleatório
                dist = random.randint(inst, size=(inst))
            if distrib == 'M': # 50% Ordenado
                meioOrdenado = np.arange(inst)[:int(inst/2)]
                meioAleatorio = random.randint(int(inst/2), size=(int(inst/2)))
                dist = np.concatenate((meioOrdenado, meioAleatorio))
                
            print(algo.__name__, inst, distrib)
            dados['algoritmo'].append(algo.__name__) 
            dados['instancia'].append(inst)
            dados['distribuicao'].append(distrib)
        
            # Calcula e salva o tempo de execução
            start_time = time.time()
        
            # Roda o algoritmo
            algo(dist)
            print('finalizou')
        
            end_time = time.time()
            tempo_execucao = end_time - start_time
            dados['tempo_execucao_s'].append(round(tempo_execucao,2))
            dados['tempo_execucao_ms'].append(round(tempo_execucao*1000,2))
        
            df = pd.DataFrame(dados)
            df.head()

            df.to_csv('dados.csv')
            print('Dados Salvos!')