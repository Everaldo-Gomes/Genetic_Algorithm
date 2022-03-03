# ------------------------------+
# Author: Everaldo P. Gomes     +
# Email:  everaldo332@gmail.com +
# ------------------------------+

from func import *


# ================================================================================
#                                Constants
# ================================================================================
PEOPLE_QNT = 20
NUM_GENES = 5



# ================================================================================
#                                   Main
# ================================================================================


# initialize and show population

population = [[]]
population = init_population(PEOPLE_QNT, NUM_GENES)

print ("Population:   ", PEOPLE_QNT)
print ("Genes:        ", NUM_GENES, "\n")

for i in range (0, PEOPLE_QNT):
    print('%2s' % i, " -> ", population[i])
