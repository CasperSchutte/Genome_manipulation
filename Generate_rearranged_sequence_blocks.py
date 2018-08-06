from class_Genome_Manipulation_CS import GenomeMutation

import random
import numpy as np


sequence_blocks = range(1,5001)

#introduc inversions
i = 0
while i < 200:
    inversion_size = random.randint(2,300)
    inversion_start_position = random.randint(1, (5000 - inversion_size))
    inversion_end_position = inversion_start_position + inversion_size
    
    introduce_inversion = GenomeMutation()
    inversion = introduce_inversion.Inversion(sequence_blocks, inversion_start_position, inversion_end_position)
    sequence_blocks = inversion

    i += 1

#introduce translocations


list_of_sequence_blocks = []
positions = []
for i in range(len(sequence_blocks)):
    x = int(sequence_blocks[i])
    list_of_sequence_blocks.append(x)
    positions.append((1,7))



np.savetxt('sequence_blocks.txt', np.c_[list_of_sequence_blocks, positions], fmt="%f")

# The total number of items seems to change every time the program to generate them
