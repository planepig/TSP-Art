import numpy as np
from calculate_distance import calculate_distance
from tqdm import tqdm
# node为nump类型,计算相邻两个点的距离


# Nearest Neighbor Algorithm (NN)
def nearest_neighbor(node_coords_dict):
    # 生成一个数组,用于记录节点是否被访问过
    visited = np.zeros(len(node_coords_dict) + 1, dtype=int)

    # 1-n中随机选取一个点作为起点
    start_index = np.random.randint(1, len(node_coords_dict) + 1)
    visited[start_index] = 1
    now_node = start_index
    path = []
    pbar = tqdm(total=len(node_coords_dict))
    path.append(node_coords_dict[now_node])
    while(visited.sum() < len(node_coords_dict)):
        min_distance = np.inf
        nearest_node = -1
        # if(visited.sum() == 1):
            # now_node = start_index
            # path.append(node_coords_dict[now_node])
        for i in range(1, len(node_coords_dict) + 1):
            if(visited[i] == 0 and i != now_node):
                temp_distance = np.linalg.norm(np.array(node_coords_dict[now_node]) - np.array(node_coords_dict[i]))
                if(temp_distance < min_distance):
                    min_distance = temp_distance
                    nearest_node = i
        path.append(node_coords_dict[nearest_node])
        visited[nearest_node] = 1
        now_node = nearest_node

        pbar.update(1)
        pbar.set_postfix_str(f"Nearest Neighbor Algorithm visited: {visited.sum()}")
    pbar.update(1)
    pbar.set_postfix_str(f"Nearest Neighbor Algorithm visited: {visited.sum()}")
    pbar.close()

    path.append(node_coords_dict[start_index])
    best_distance = calculate_distance(np.array(path))
    # print(path, best_distance)
    # np.save("./output_npy/nearest_neighbor.npy", np.array(path))
    return np.array(path), best_distance









