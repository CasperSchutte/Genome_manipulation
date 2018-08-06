from class_Genome_Manipulation_CS import GenomeMutation
from class_Genome_Manipulation_CS import WriteOutputFile
from class_FastA import FastA

if __name__ == "__main__":
    input_filename = 'demo_fasta_file.fasta'
    input_file = FastA()
    number_of_sequences = input_file.ReadFastA(input_filename)
    print("sequences = ", number_of_sequences)
    mutate_genome = GenomeMutation()
    path = '/home/19477619/Casper/Python/Project/Genome_manipulation-CHANGED/'
    for index, sequence in enumerate(input_file):
        mutated_sequence = mutate_genome.Inversion(sequence, 10, 15)
        out_file = input_file.GetContigName(index)
        sequence_name = out_file + '_INVERSION'
        out_file = path + '/' + out_file + '_INVERSION' + '.fasta'
        output_file = WriteOutputFile()
        output_file.WriteOutputFastA(out_file, sequence_name, mutated_sequence)
