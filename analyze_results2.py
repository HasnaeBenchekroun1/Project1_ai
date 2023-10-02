from csv_utils import read_results_csv
from matplotlib import pyplot as plt 
import numpy as np


    

if __name__ == '__main__':

    h3_tree_depth_average = 0
    h3_explored_nodes_average = 0
    h3_max_fringe_average = 0
    bfs_tree_depth_average = 0
    bfs_explored_nodes_average = 0
    bfs_max_fringe_average = 0

    """"
    dfs_tree_depth_average = 0
    dfs_explored_nodes_average = 0
    dfs_max_fringe_average = 0
    ucs_tree_depth_average = 0
    ucs_explored_nodes_average = 0
    ucs_max_fringe_average = 0
    """

    #loading data
    results = read_results_csv(filename='results3.csv')

    #calculating averages:
    for i in range(100):
        h3_tree_depth_average += int(results[i]['h3-tree_depth'])
        h3_explored_nodes_average += int(results[i]['h3-explored_nodes'])
        h3_max_fringe_average += int(results[i]['h3-fringe_max'])

        bfs_tree_depth_average += int(results[i]['bfs-tree_depth'])
        bfs_explored_nodes_average += int(results[i]['bfs-explored_nodes'])
        bfs_max_fringe_average += int(results[i]['bfs-fringe_max'])

        """"
        dfs_tree_depth_average += int(results[i]['dfs-tree_depth'])
        dfs_explored_nodes_average += int(results[i]['dfs-explored_nodes'])
        dfs_max_fringe_average += int(results[i]['dfs-fringe_max'])

        ucs_tree_depth_average += int(results[i]['ucs-tree_depth'])
        ucs_explored_nodes_average += int(results[i]['ucs-explored_nodes'])
        ucs_max_fringe_average += int(results[i]['ucs-fringe_max'])
        """

    h3_tree_depth_average = h3_tree_depth_average / 100
    h3_explored_nodes_average = h3_explored_nodes_average/100
    h3_max_fringe_average = h3_max_fringe_average/100

    bfs_tree_depth_average = bfs_tree_depth_average / 100
    bfs_explored_nodes_average = bfs_explored_nodes_average/100
    bfs_max_fringe_average = bfs_max_fringe_average/100

    """"
    dfs_tree_depth_average = dfs_tree_depth_average / 100
    dfs_explored_nodes_average = dfs_explored_nodes_average/100
    dfs_max_fringe_average = dfs_max_fringe_average/100

    ucs_tree_depth_average = ucs_tree_depth_average / 100
    ucs_explored_nodes_average = ucs_explored_nodes_average/100
    ucs_max_fringe_average = ucs_max_fringe_average/100
    """

    print(f"A* Manhattan distance:\nTree depth = {h3_tree_depth_average}\nExplored nodes = {h3_explored_nodes_average}\nFringe max size = {h3_max_fringe_average}")
    print("------------------")
    print(f"BFS:\nTree depth = {bfs_tree_depth_average}\nExplored nodes = {bfs_explored_nodes_average}\nFringe max size = {bfs_max_fringe_average}")
    print("------------------")
    """"
    print(f"DFS:\nTree depth = {dfs_tree_depth_average}\nExplored nodes = {dfs_explored_nodes_average}\nFringe max size = {dfs_max_fringe_average}")
    print("------------------")
    print(f"UCS:\nTree depth = {ucs_tree_depth_average}\nExplored nodes = {ucs_explored_nodes_average}\nFringe max size = {ucs_max_fringe_average}")
    print("------------------")
    """

    heuristics = ["A* Manhattan Distance", "BFS"]#, "DFS", "UCS"]
    metrics = ["Max Tree-depth", "Number Explored Nodes", "Max Fringe-size"]
    data = [
        [h3_tree_depth_average, h3_explored_nodes_average, h3_max_fringe_average],
        [bfs_tree_depth_average, bfs_explored_nodes_average, bfs_max_fringe_average]
            ]
    """"
        [dfs_tree_depth_average, dfs_explored_nodes_average, dfs_max_fringe_average],
        [ucs_tree_depth_average, ucs_explored_nodes_average, ucs_max_fringe_average]
    ]
    """

    data = np.array(data)

    bar_width = 0.2
    index = np.arange(len(heuristics))

    # Create subplots for each metric
    plt.figure(figsize=(10, 6))  

    for i, metric in enumerate(metrics):
        plt.bar(index + i * bar_width, data[:, i], bar_width, label=metric)

    # Customize the plot
    plt.xlabel('Search Strategy')
    plt.ylabel('Average Value')
    plt.title('Graphical comparaison of A*, BFS')
    plt.xticks(index + (bar_width * (len(metrics) / 2)), heuristics)
    plt.legend()

    # Show the plot
    plt.tight_layout() 
    plt.show()



