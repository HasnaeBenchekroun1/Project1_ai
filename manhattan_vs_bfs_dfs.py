from csv_utils import *
from eightpuzzle import *
import search
import time




def one_iteration(state, index=0):

    puzzle = EightPuzzleState(state)

    results = {}
    results['puzzle'] = state

    print(f'Puzzle {index}:')
    print(puzzle)
    print("solving...")

    problem = EightPuzzleSearchProblem(puzzle)

    path, results_data= search.aStarSearch(problem, heuristic=puzzle.h3)
    depth, explored, fringe = results_data
    print('A* with Manhattan Heuristic found a path of %d moves: %s' % (len(path), str(path)))
    print("-----")
    results["h3-tree_depth"] = depth
    results["h3-explored_nodes"] = explored
    results["h3-fringe_max"] = fringe

    path, results_data = search.bfs(problem)
    depth, explored, fringe = results_data
    print('BFS found a path of %d moves: %s' % (len(path), str(path)))
    print("-----")
    results["bfs-tree_depth"] = depth
    results["bfs-explored_nodes"] = explored
    results["bfs-fringe_max"] = fringe

    """"
    path, results_data = search.dfs(problem)
    depth, explored, fringe = results_data
    print('DFS found a path of %d moves: %s' % (len(path), str(path)))
    print("-----")
    results["dfs-tree_depth"] = depth
    results["dfs-explored_nodes"] = explored
    results["dfs-fringe_max"] = fringe
    

    path, results_data = search.ucs(problem)
    depth, explored, fringe = results_data
    print('UCS found a path of %d moves: %s' % (len(path), str(path)))
    print("-----")
    results["ucs-tree_depth"] = depth
    results["ucs-explored_nodes"] = explored
    results["ucs-fringe_max"] = fringe
    """

    return results


if __name__ == '__main__':
    field_names = ['puzzle', 'h3-tree_depth', 'h3-explored_nodes', 'h3-fringe_max','bfs-tree_depth', 'bfs-explored_nodes', 'bfs-fringe_max']
    results = []
    states = read_from_csv('scenarios3.csv')
    for i, state in enumerate(states):

        result = one_iteration(state, index=i)
        results.append(result)
    write_results(field_names, results, 'results3.csv')




