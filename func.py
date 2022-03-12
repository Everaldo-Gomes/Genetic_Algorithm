import random


# ================================================================================
#                                 Population
# ================================================================================

def info_from_file (FILE):

    # getting all the information in the file
    
    list = []

    with open (FILE) as file:
        for line in file:
            list.append(line.split(" "))

    return list


def init_population (machine_qnt, job_qnt):
    
    # create a list of people that has num_genes
    # where the genes is initiating randomly
 
    population_list = [[random.randint (1,job_qnt) for j in range (job_qnt)]
                      for i in range (machine_qnt)]

    return population_list;



# ================================================================================
#                                 Fitness
# ================================================================================



# ================================================================================
#                                Selection
# ================================================================================



# ================================================================================
#                                Crossover 
# ================================================================================



# ================================================================================
#                                Mutation
# ================================================================================


# list = []

    # with open (FILE) as file:
    #     for line in file:
    #         list.append(line.split(" "))
    #         #[0][0] é o numero de jobs
    #         #[0][1] é o numero de maquinas
    #         #[0][3] é tempo maximo do maluko la
    #         #[0][4] é o tempo minimo do maluko la
    #     print(list[0][0])
    #         # for x in range(1, int(lista[0][1]), 1):
    #         #     for y in range(int(lista[0][0])):
    #         #         print(lista[y][x])
    # return list
