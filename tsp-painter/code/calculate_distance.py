import numpy as np


def calculate_distance(node):
    distance = 0
    for i in range(len(node) - 1):
        distance += np.linalg.norm(node[i] - node[i + 1])
    # distance += np.linalg.norm(node[0] - node[-1])
    return distance
