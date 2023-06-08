import numpy as np
from calculate_distance import calculate_distance
from tqdm import tqdm

def two_opt(node_coords_dict):
    # 生成一个数组,用于记录节点是否被访问过
    visited = np.zeros(len(node_coords_dict) + 1, dtype=int)

    # 1-n中随机选取一个点作为起点
    start_index = np.random.randint(1, len(node_coords_dict) + 1)
    visited[start_index] = 1
    now_node = start_index
    path = []

    path.append(node_coords_dict[now_node])
    while (visited.sum() < len(node_coords_dict)):
        min_distance = np.inf
        nearest_node = -1
        for i in range(1, len(node_coords_dict) + 1):
            if (visited[i] == 0 and i != now_node):
                temp_distance = np.linalg.norm(np.array(node_coords_dict[now_node]) - np.array(node_coords_dict[i]))
                if (temp_distance < min_distance):
                    min_distance = temp_distance
                    nearest_node = i
        path.append(node_coords_dict[nearest_node])
        visited[nearest_node] = 1
        now_node = nearest_node
    path.append(node_coords_dict[start_index])

    min_distance = calculate_distance(np.array(path))
    path = np.array(path)
    # 2-opt算法优化
    cnt = 0
    while cnt < 2:
        cnt = cnt + 1
        for i in range(1, len(path) - 2):
            for j in range(i + 2, len(path) - 1):
                new_distance = (
                        calculate_distance(np.array([path[i - 1], path[i]])) +
                        calculate_distance(np.array([path[j], path[j + 1]])) +
                        calculate_distance(np.array([path[i], path[j + 1]])) +
                        calculate_distance(np.array([path[i - 1], path[j]]))
                )
                if new_distance < min_distance:
                    path[i:j + 1] = path[i:j + 1][::-1]  # 反转路径
                    min_distance = new_distance
                    improvement = True
    # np.save("./output_npy/two_opt.npy", np.array(path))
    return np.array(path), calculate_distance(np.array(path))