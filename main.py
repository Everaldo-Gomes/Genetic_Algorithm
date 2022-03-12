from func import *


# crossover
# mutacao
# gerar as médias
# pior casos
# definir OS critérios de parada


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


# inicializa e mostra população (soluções)

solucao = []
solucao = init_solution(100, qnt_tarefa)

#for i in range (0, 100):
#    print('%2s' % i, " -> ", solucao[i])

    
instancia = []
for i in range(1, qnt_maquina):
    if i > 0:
        instancia.append(lista[i])


i = 0
melhores_tempos = []
piores_tempos = []

while (i < 1):

    classificao = classifica (instancia, solucao)
    melhores_50_elementos = seleciona_melhores(classificao[0])
    melhor_tempo = melhores_50_elementos[0][0]  # só da ultima itenração
    pior_tempo = classificao[1] # só da ultima itenração

    # salvar os tempos para fazer a média
    melhores_tempos.append (melhor_tempo)
    piores_tempos.append (pior_tempo)

    
    i = i + 1
