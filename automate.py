from eightpuzzle import *
from csv_utils import *



def one_iteration(state, index=0):

    puzzle = EightPuzzleState(state)

    results = {}
    results['puzzle'] = state

    #puzzle = createRandomEightPuzzle(moves = 100)
    print(f'Puzzle {index}:')
    print(puzzle)
    print("solving...")

    problem = EightPuzzleSearchProblem(puzzle)

    path, results_data= search.aStarSearch(problem, heuristic=puzzle.h1)
    depth, explored, fringe = results_data
    print('A* with heuristic 1 found a path of %d moves: %s' % (len(path), str(path)))
    print("-----")
    results["h1-tree_depth"] = depth
    results["h1-explored_nodes"] = explored
    results["h1-fringe_max"] = fringe

    path, results_data= search.aStarSearch(problem, heuristic=puzzle.h2)
    depth, explored, fringe = results_data
    print('A* with heuristic 2 found a path of %d moves: %s' % (len(path), str(path)))
    print("-----")
    results["h2-tree_depth"] = depth
    results["h2-explored_nodes"] = explored
    results["h2-fringe_max"] = fringe

    path, results_data= search.aStarSearch(problem, heuristic=puzzle.h3)
    depth, explored, fringe = results_data
    print('A* with heuristic 3 found a path of %d moves: %s' % (len(path), str(path)))
    print("-----")
    results["h3-tree_depth"] = depth
    results["h3-explored_nodes"] = explored
    results["h3-fringe_max"] = fringe

    path, results_data= search.aStarSearch(problem, heuristic=puzzle.h4)
    depth, explored, fringe = results_data
    print('A* with heuristic 4 found a path of %d moves: %s' % (len(path), str(path)))
    print("-----")
    results["h4-tree_depth"] = depth
    results["h4-explored_nodes"] = explored
    results["h4-fringe_max"] = fringe

    return results
 


if __name__ == '__main__':
    field_names = ['puzzle', 'h1-tree_depth', 'h1-explored_nodes', 'h1-fringe_max','h2-tree_depth', 'h2-explored_nodes', 'h2-fringe_max',
                    'h3-tree_depth', 'h3-explored_nodes', 'h3-fringe_max', 'h4-tree_depth', 'h4-explored_nodes', 'h4-fringe_max']
    results = []
    states = read_from_csv()
    for i, state in enumerate(states):
        result = one_iteration(state, index=i)
        results.append(result)
    write_results(field_names, results)
    



