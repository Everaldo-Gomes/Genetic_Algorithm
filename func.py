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

    # retorna toda a população (solução) com os tempos
    
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

    # retorna os 50 melhores (50 escolha pessoal)
    return lista_para_selecao[:50]
    
    


# ================================================================================
#                                Crossover 
# ================================================================================

def melhores_50_elementos_sem_os_tempos (melhores_50_elementos):

    # retorna a lista dos 50 mehores mas SEM os tempos 
    
    lista = []

    for i in melhores_50_elementos:
        lista.append (i[1])
    
    return lista


def remove_duplicados (lista):

    tmp = lista 
    
    if len(lista) != len(set(tmp)):
        return lista

    tamanho = len (lista)
    numero_duplicado = 0
    numero_faltante = 0
    indice = 0

    for i in range (tamanho):

        # verifica se o número existe na lista
        if i + 1 not in lista:
            numero_faltante = i + 1
            #print (lista[k])
            # verifia se está duplicado e retona o indice
            for j in range (tamanho):
                for k in range (j, tamanho):
                    if lista[j] == lista[k]:
                        indice = j
            
            lista[indice] = numero_faltante

    return lista
            


def recombinacao (melhores_50_elementos):
    
    # faz uma recombinação com os 50 melhores elementos
    filho = []
    linha = 1
    
    pais = melhores_50_elementos_sem_os_tempos (melhores_50_elementos)
    tamanho = len(pais)
    
    for i in range (tamanho):

        tmp = pais[i][:10] + pais[linha][10:20]
        filho.append (remove_duplicados (tmp))
        filho.append (pais[i])

        if linha < tamanho - 1:
            linha = linha + 1
#    print (filho)
    return filho



#b= melhores_50_elementos[j][k+1]

  #      tmp = melhores_50_elementos[i]
   #     tmp 
        

        
        
    



# ================================================================================
#                                 Mutação
# ================================================================================
