from csv_utils import read_results_csv
from matplotlib import pyplot as plt 
import numpy as np


    

if __name__ == '__main__':

    h1_tree_depth_average = 0
    h1_explored_nodes_average = 0
    h1_max_fringe_average = 0
    h2_tree_depth_average = 0
    h2_explored_nodes_average = 0
    h2_max_fringe_average = 0
    h3_tree_depth_average = 0
    h3_explored_nodes_average = 0
    h3_max_fringe_average = 0
    h4_tree_depth_average = 0
    h4_explored_nodes_average = 0
    h4_max_fringe_average = 0

    #loading data
    results = read_results_csv()

    #calculating averages:
    for i in range(100):
        h1_tree_depth_average += int(results[i]['h1-tree_depth'])
        h1_explored_nodes_average += int(results[i]['h1-explored_nodes'])
        h1_max_fringe_average += int(results[i]['h1-fringe_max'])

        h2_tree_depth_average += int(results[i]['h2-tree_depth'])
        h2_explored_nodes_average += int(results[i]['h2-explored_nodes'])
        h2_max_fringe_average += int(results[i]['h2-fringe_max'])

        h3_tree_depth_average += int(results[i]['h3-tree_depth'])
        h3_explored_nodes_average += int(results[i]['h3-explored_nodes'])
        h3_max_fringe_average += int(results[i]['h3-fringe_max'])

        h4_tree_depth_average += int(results[i]['h4-tree_depth'])
        h4_explored_nodes_average += int(results[i]['h4-explored_nodes'])
        h4_max_fringe_average += int(results[i]['h4-fringe_max'])

    h1_tree_depth_average = h1_tree_depth_average / 100
    h1_explored_nodes_average = h1_explored_nodes_average/100
    h1_max_fringe_average = h1_max_fringe_average/100

    h2_tree_depth_average = h2_tree_depth_average / 100
    h2_explored_nodes_average = h2_explored_nodes_average/100
    h2_max_fringe_average = h2_max_fringe_average/100

    h3_tree_depth_average = h3_tree_depth_average / 100
    h3_explored_nodes_average = h3_explored_nodes_average/100
    h3_max_fringe_average = h3_max_fringe_average/100

    h4_tree_depth_average = h4_tree_depth_average / 100
    h4_explored_nodes_average = h4_explored_nodes_average/100
    h4_max_fringe_average = h4_max_fringe_average/100

    print(f"Heuristic 1 Misplaced Tiles:\nTree depth = {h1_tree_depth_average}\nExplored nodes = {h1_explored_nodes_average}\nFringe max size = {h1_max_fringe_average}")
    print("------------------")
    print(f"Heuristic 2 Euclidean Distance:\nTree depth = {h2_tree_depth_average}\nExplored nodes = {h2_explored_nodes_average}\nFringe max size = {h2_max_fringe_average}")
    print("------------------")
    print(f"Heuristic 3 Manhattan Distance:\nTree depth = {h3_tree_depth_average}\nExplored nodes = {h3_explored_nodes_average}\nFringe max size = {h3_max_fringe_average}")
    print("------------------")
    print(f"Heuristic 4 Tiles out of rows + columns:\nTree depth = {h4_tree_depth_average}\nExplored nodes = {h4_explored_nodes_average}\nFringe max size = {h4_max_fringe_average}")
    print("------------------")

    heuristics = ["Misplaced Tiles", "Euclidean Distance", "Manhattan Distance", "Rows + Columns"]
    metrics = ["Max Tree-depth", "Number Explored Nodes", "Max Fringe-size"]
    data = [
        [h1_tree_depth_average, h1_explored_nodes_average, h1_max_fringe_average],
        [h2_tree_depth_average, h2_explored_nodes_average, h2_max_fringe_average],
        [h3_tree_depth_average, h3_explored_nodes_average, h3_max_fringe_average],
        [h4_tree_depth_average, h4_explored_nodes_average, h4_max_fringe_average]
    ]

    data = np.array(data)

    bar_width = 0.2
    index = np.arange(len(heuristics))

    # Create subplots for each metric
    plt.figure(figsize=(10, 6))  

    for i, metric in enumerate(metrics):
        plt.bar(index + i * bar_width, data[:, i], bar_width, label=metric)

    # Customize the plot
    plt.xlabel('Heuristics')
    plt.ylabel('Average Value')
    plt.title('Graphical comparaison of heuristics performance')
    plt.xticks(index + (bar_width * (len(metrics) / 2)), heuristics)
    plt.legend()

    # Show the plot
    plt.tight_layout() 
    plt.show()



