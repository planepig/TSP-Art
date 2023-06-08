import tsplib95 as tsp
import numpy as np
from nearest_neighbor import*
from farthest_insertion import*
from nearest_insertion import*
from two_opt import*
from LKH import*
from christofides import*
from plot import *
from metric import *
import elkai
tspfilename = 'planepig'
# 加载tsp文件
# img_name_table = {"flaglogo","logo","mascot","scenery1","scenery2","scenery3","scenery4","scenery5","scenery6","scenery7","scenery8"}
img_name_table = {"yanshou"}
test_table = {"att48","a280"}
for item in img_name_table :
    tspfilename = item
    filename = '../dataset/' + tspfilename + '.tsp'
    tsp_data = tsp.load(filename)
        # 获取节点坐标,序号 : {x,y}
    node_coords_dict = tsp_data.node_coords
        # 将节点坐标转换为numpy数组
    node_coords = np.array(list(node_coords_dict.values()))


    LKH_path, LKH_best_distance = LKH(node_coords_dict, 1)
    plot_path(LKH_path, 'LKH Algorithm', LKH_best_distance,tspfilename, len(node_coords_dict))

    # two_opt_path, two_opt_best_distance = two_opt(node_coords_dict)
    # plot_path(two_opt_path, '2-opt Algorithm', two_opt_best_distance,tspfilename, len(node_coords_dict))


    # christofides_path, christofides_best_distance = christofides(node_coords_dict)
    # plot_path(christofides_path, 'Christofides Algorithm', christofides_best_distance,tspfilename,len(node_coords_dict))

    # nearest_neighbor_path, nearest_neighbor_best_distance = nearest_neighbor(node_coords_dict)
    # plot_path(nearest_neighbor_path, 'Nearest Neighbor Algorithm', nearest_neighbor_best_distance,tspfilename, len(node_coords_dict))

    # farthest_insertion_path, farthest_insertion_best_distance = farthest_insertion(node_coords_dict)
    # plot_path(farthest_insertion_path, 'Farthest Insertion Algorithm', farthest_insertion_best_distance,tspfilename,len(node_coords_dict))

    # nearest_insertion_path, nearest_insertion_best_distance = nearest_insertion(node_coords_dict)
    # plot_path(nearest_insertion_path, 'Nearest Insertion Algorithm', nearest_insertion_best_distance,tspfilename, len(node_coords_dict))


























# def generate_loop(node_coords_dict):
#     LKH_path, LKH_best_distance = LKH(node_coords_dict, 1)
#     plot_path(LKH_path, 'LKH Algorithm', LKH_best_distance,tspfilename,GAP(LKH_best_distance,LKH_best_distance),len(node_coords_dict))
#     # plot_path(LKH_path, 'LKH Algorithm', LKH_best_distance,tspfilename)
#
#     nearest_neighbor_path, nearest_neighbor_best_distance = nearest_neighbor(node_coords_dict)
#     # plot_path(nearest_neighbor_path, 'Nearest Neighbor Algorithm', nearest_neighbor_best_distance,tspfilename, GAP(LKH_best_distance,nearest_neighbor_best_distance))
#     plot_path(nearest_neighbor_path, 'Nearest Neighbor Algorithm', nearest_neighbor_best_distance,tspfilename, GAP(LKH_best_distance,nearest_neighbor_best_distance),len(node_coords_dict))
#
#     # christofides_path, christofides_best_distance = christofides(node_coords_dict)
#     # plot_path(christofides_path, 'Christofides Algorithm', christofides_best_distance,tspfilename,GAP(LKH_best_distance,christofides_best_distance),len(node_coords_dict))
#
#
#
#     two_opt_path, two_opt_best_distance = two_opt(node_coords_dict)
#     plot_path(two_opt_path, '2-opt Algorithm', two_opt_best_distance,tspfilename, GAP(LKH_best_distance,two_opt_best_distance),len(node_coords_dict))
#
#
#
#     farthest_insertion_path, farthest_insertion_best_distance = farthest_insertion(node_coords_dict)
#     plot_path(farthest_insertion_path, 'Farthest Insertion Algorithm', farthest_insertion_best_distance,tspfilename,GAP(LKH_best_distance,farthest_insertion_best_distance),len(node_coords_dict))
#
#
#     nearest_insertion_path, nearest_insertion_best_distance = nearest_insertion(node_coords_dict)
#     plot_path(nearest_insertion_path, 'Nearest Insertion Algorithm', nearest_insertion_best_distance,tspfilename, GAP(LKH_best_distance,nearest_insertion_best_distance),len(node_coords_dict))
#
#
# for item in img_name_table:
#     tspfilename = item
#     filename = 'dataset/task_dataset/'+tspfilename+'.tsp'
#     # filename = 'dataset/' + tspfilename + '.tsp'
#     tsp_data = tsp.load(filename)
#     # 获取节点坐标,序号 : {x,y}
#     node_coords_dict = tsp_data.node_coords
#     # 将节点坐标转换为numpy数组
#     node_coords = np.array(list(node_coords_dict.values()))
#     generate_loop(node_coords_dict)
