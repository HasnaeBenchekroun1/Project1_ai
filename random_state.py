import random
import csv

def generate_random_permutation():
    numbers = list(range(9))
    random.shuffle(numbers)
    return numbers

#random_permutation = generate_random_permutation()
#print(random_permutation)


def generate_unique_permutations(num_permutations):
    unique_permutations = []

    while len(unique_permutations) < num_permutations:
        permutation = generate_random_permutation()
        if permutation not in unique_permutations:
            unique_permutations.append(permutation)

    return unique_permutations

def main():
    num_permutations = 9  # Change this to the number of unique permutations you want
    unique_permutations = generate_unique_permutations(num_permutations)

    # Print the unique permutations
    for i, permutation in enumerate(unique_permutations):
        print(f"Permutation {i+1}: {permutation}")

if __name__ == "__main__":
    main()
