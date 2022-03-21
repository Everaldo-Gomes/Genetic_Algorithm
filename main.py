from func import *
import time
import numpy as np


tempo_inicial = time.time()


# ================================================================================
#                                Constantes
# ================================================================================

FILE = [
    "TXTs/tai20_5.txt",
    "TXTs/tai20_10.txt",
    "TXTs/tai20_20.txt",
    "TXTs/tai50_5.txt",
    "TXTs/tai50_10.txt",
    "TXTs/tai50_20.txt",
    "TXTs/tai100_5.txt",
    "TXTs/tai100_10.txt",
    "TXTs/tai100_20.txt",  
    "TXTs/tai200_10.txt"]

# ================================================================================
#                                   Main
# ================================================================================

for arquivo in FILE:

    # set the variable's values
    lista = []
    lista = info_from_file (arquivo)
    
    qnt_tarefa  = int(lista[0][0])
    qnt_maquina = int(lista[0][1])
    max_time    = int(lista[0][3])
    min_time    = int(lista[0][4])
    
        
    instancia = []
    for i in range(1, qnt_maquina):
        if i > 0:
            instancia.append(lista[i])

    
    i = 0
    melhor_tempo_execucao = []
    pior_tempo_execucao = []
    tempo_execucao = []
    melhores_tempos = []
    piores_tempos = []
    
    while (i < 10):
    
        # inicializa e mostra população (soluções)
    
        solucao = []
        solucao = init_solution(100, qnt_tarefa)
    
        tempo_estourado = False
        melhor_tempo = 99999999
        pior_tempo = 0
        
        tempo_loop_inicial = time.time()
        numero_execucao = 0
        
        while (not tempo_estourado): # Critério de parada 1.     numero_execucao < 300
        
            classificao = classifica (instancia, solucao)
            melhores_50_elementos = seleciona_melhores(classificao[0])
    
            if melhores_50_elementos[0][0] < melhor_tempo:
                melhor_tempo = melhores_50_elementos[0][0]  # só da ultima iteração
    
            if classificao[1] > pior_tempo:
                pior_tempo = classificao[1]                 # só da ultima iteração
    
            novas_solucoes = recombinacao (melhores_50_elementos)
            solucao = mutacao (novas_solucoes, melhores_50_elementos_sem_os_tempos (melhores_50_elementos), qnt_tarefa)
    
            tempo_estourado = (time.time() - tempo_loop_inicial) > 10.0
            numero_execucao += 1

            # Critério de parada 2. se o nosso resultado for menor que 10% do resultado do carinha.
            if melhor_tempo < (min_time * 0.9):
                break
            
        # salvar os tempos para fazer a média
        tempo_execucao.append (time.time() - tempo_loop_inicial)
        melhores_tempos.append (melhor_tempo)
        piores_tempos.append (pior_tempo)
    
        i = i + 1

    print ("---------------------------------------------------------------")   
    print ("Arquivo: ", arquivo.split("/")[1], "\t\t  Lower bound: ", min_time)
    print ("---------------------------------------------------------------")
    print ("Lower bound:                    ", min(melhores_tempos))
    print ("Upper bound:                    ", max(piores_tempos))
    print ("Média do lower bound:           ", round(sum(melhores_tempos) / len(melhores_tempos), 4))
    print ("Desvio Padrao do lower bound:   ", round(np.std(melhores_tempos), 4))
    print ("Media Tempo:                    ", round(sum(tempo_execucao) / len(tempo_execucao), 4))
    print ("Desvio Padrao Tempo exec:       ", round(np.std(tempo_execucao), 2))
    print ("Total Tempo:                    ", round(time.time() - tempo_inicial, 4))
    print ("---------------------------------------------------------------\n")   
