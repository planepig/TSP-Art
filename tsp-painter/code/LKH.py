import elkai
import numpy as np
from calculate_distance import calculate_distance
def LKH(node_coords_dict, cnt):
    path = elkai.Coordinates2D(node_coords_dict).solve_tsp(cnt)
    path = [node_coords_dict[i] for i in path]
    #将结果保存为numpy数组存储在文件中
    # np.save("./output_npy/LKH.npy", np.array(path))
    return np.array(path), calculate_distance(np.array(path))