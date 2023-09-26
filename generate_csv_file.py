from random_state import generate_unique_permutations
from csv_utils import *



def main():
    num_permutations = 9  # Change this to the number of unique permutations you want
    unique_permutations = generate_unique_permutations(num_permutations)
    print(unique_permutations)
    write_to_csv(unique_permutations)

    read_from_csv('scenarios.csv')


main()