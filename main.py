from func import *


# ================================================================================
#                                Constants
# ================================================================================

FILE = "TXTs/tai20_5.txt"



# ================================================================================
#                                   Main
# ================================================================================

# set the variable's values

list = []
list = info_from_file (FILE)

job_qnt     = int(list[0][0])
machine_qnt = int(list[0][1])
max_time    = int(list[0][3])
min_time    = int(list[0][4])


# initialize and show population

population = [[]]
population = init_population(machine_qnt, job_qnt)

print ("Population:   ", machine_qnt)
print ("Genes:        ", job_qnt, "\n")

for i in range (0, machine_qnt):
    print('%2s' % i, " -> ", population[i])
