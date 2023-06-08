import numpy as np
from calculate_distance import calculate_distance
from tqdm import tqdm

def nearest_insertion(node_coords_dict):
    # 生成一个数组,用于记录节点是否被访问过
    visited = np.zeros(len(node_coords_dict) + 1, dtype=int)
    # 生成一个集合,用于记录未被访问过的节点
    unvisited = set(range(1, len(node_coords_dict) + 1))
    path = []
    # 1-n中随机选取一个点作为起点
    start_index = np.random.randint(1, len(node_coords_dict) + 1)
    visited[start_index] = 1
    now_node = start_index
    path.append(start_index)

    distances = np.zeros((len(node_coords_dict) + 1, len(node_coords_dict) + 1))

    # 计算并存储节点之间的距离
    for i in range(1, len(node_coords_dict) + 1):
        for j in range(1, len(node_coords_dict) + 1):
            distances[i][j] = np.linalg.norm(np.array(node_coords_dict[i]) - np.array(node_coords_dict[j]))
    pbar = tqdm(total=len(node_coords_dict))
    while (visited.sum() < len(node_coords_dict)):
        nearest_distance = np.inf
        nearest_node = -1
        for i in unvisited:
            for j in path:
                temp_distance = distances[i][j]
                if (temp_distance < nearest_distance):
                    nearest_distance = temp_distance
                    nearest_node = i
        now_node = nearest_node
        min_distance = np.inf
        insert_index = -1
        unvisited.remove(nearest_node)
        for i in range(0, len(path) - 1):
            if (distances[now_node][path[i]] + distances[now_node][path[i + 1]] < min_distance):
                min_distance = distances[now_node][path[i]] + distances[now_node][path[i + 1]]
                insert_index = i + 1

        visited[now_node] = 1
        path.insert(insert_index, now_node)
        pbar.update(1)
        pbar.set_postfix_str(f"Nearest Insertion Algorithm visited: {visited.sum()}")

    # pbar.update(1)
    pbar.set_postfix_str(f"Nearest Insertion Algorithm visited: {visited.sum()}")
    pbar.close()
    path.append(start_index)
    path = [node_coords_dict[i] for i in path]
    best_distance = calculate_distance(np.array(path))
    # np.save("./output_npy/nearest_insertion.npy", np.array(path))
    return np.array(path), best_distance


