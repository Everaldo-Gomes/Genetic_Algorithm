from func import *
import time

# crossover
# mutacao
# gerar as médias
# pior casos
# definir OS critérios de parada
# contagem do tempo de execução usando a função time()

tempo_inicial = time.time()


# ================================================================================
#                                Constantes
# ================================================================================

FILE = "TXTs/tai20_5.txt"

# ================================================================================
#                                   Main
# ================================================================================

# set the variable's values

lista = []
lista = info_from_file (FILE)

qnt_tarefa  = int(lista[0][0])
qnt_maquina = int(lista[0][1])
max_time    = int(lista[0][3])
min_time    = int(lista[0][4])

#for i in range (0, 100):
#    print('%2s' % i, " -> ", solucao[i])
    
instancia = []
for i in range(1, qnt_maquina):
    if i > 0:
        instancia.append(lista[i])


i = 0
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
    
    while (not tempo_estourado or numero_execucao < 100):

        classificao = classifica (instancia, solucao)
        melhores_50_elementos = seleciona_melhores(classificao[0])

        if melhores_50_elementos[0][0] < melhor_tempo:
            melhor_tempo = melhores_50_elementos[0][0]  # só da ultima iteração

        if classificao[1] > pior_tempo:
            pior_tempo = classificao[1]                 # só da ultima iteração

        novas_solucoes = recombinacao (melhores_50_elementos)
        solucao = mutacao (novas_solucoes, melhores_50_elementos_sem_os_tempos (melhores_50_elementos), qnt_tarefa)

        tempo_estourado = (time.time() - tempo_loop_inicial) > 2.0
        numero_execucao += 1
        
    # salvar os tempos para fazer a média
    melhores_tempos.append (melhor_tempo)
    piores_tempos.append (pior_tempo)

    i = i + 1

print ("Melhores tempos:")
print (melhores_tempos)

print ("Piores tempos:")
print (piores_tempos)

tempo_final = time.time()
print("Total Tempo gasto: ", tempo_final - tempo_inicial)
