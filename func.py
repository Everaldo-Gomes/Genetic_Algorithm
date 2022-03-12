import random
from random import sample


# ================================================================================
#                                 Solução
# ================================================================================

def info_from_file (FILE):
    
    list = []

    with open (FILE) as file:
        for line in file:
            int_list = [int (i) for i in line.split(" ")]
            list.append(int_list)
            
    return list


def init_solution (qnt_maquina, qnt_tarefa):

    solution_list = [sample (range(1, qnt_tarefa + 1), qnt_tarefa)
                     for i in range (qnt_maquina)]

    return solution_list;



# ================================================================================
#                                Função objetivo
# ================================================================================

def makespan (instancia, solucao):
    
    nM = len(instancia)
    tempo = [0] * nM
    
    for t in solucao:
        for m in range (nM):
            if tempo[m] < tempo[m-1] and m != 0:
                tempo[m] = tempo[m-1] 
            tempo[m] += instancia[m][t-1]
            
    return tempo[nM-1]



# ================================================================================
#                                     Seleção
# ================================================================================

def classifica (instancia, solucao):
    
    pior_tempo = 0
    pior_solucao = []
    lista_selecao = []

    for i in solucao:
        
        t = makespan (instancia, i)

        lista_selecao.append ([t,i])

        if t > pior_tempo:
            pior_solucao = i
            pior_tempo = t
            
    return [lista_selecao, pior_tempo, pior_solucao]



def seleciona_melhores (lista_para_selecao):

    # ordena lista ordem crescente
    lista_para_selecao = sorted (lista_para_selecao, key=lambda item: item[0])

    return lista_para_selecao[:50]
    
    


# ================================================================================
#                                Crossover 
# ================================================================================



# ================================================================================
#                                 Mutação
# ================================================================================
