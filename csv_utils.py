import csv
from eightpuzzle import createRandomEightPuzzle


def write_to_csv( rows, filename='scenarios.csv'):    
    with open(filename, mode='w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)


def read_from_csv(filename='scenarios.csv'):
    states = []
    with open(filename, mode='r') as file:
        csvfile = csv.reader(file)

        for lines in csvfile:
            #print(lines)
            if len(lines) != 0:
                int_lines = [int(i) for i in lines]
                states.append(int_lines)

    return states 


def read_results_csv(filename='results.csv'):
    results = []
    with open(filename, mode='r') as file:
        csvfile = csv.DictReader(file)
        for line in csvfile:
            if len(line) != 0:
                #print(line)
                results.append(line)

    return results



def write_results(field_names, data, filename='results.csv'):
    with open(filename, mode='w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)


def generate_random_state(movenumber=100):
    puzzle = createRandomEightPuzzle(moves=movenumber)

    return puzzle


def generate_random_states(number_states=5, move_number=25, filename='scenarios.csv'):
    all_states = []

    for i in range(number_states):
        state = generate_random_state(movenumber=move_number)
        state_list =[]
        for i in range(3):
            for j in range(3):
                state_list.append(state.cells[i][j])
        print(state_list)
        all_states.append(state_list)

    write_to_csv(all_states, filename)

if __name__ == '__main__':
    generate_random_states(100, 30, 'scenarios3.csv')






