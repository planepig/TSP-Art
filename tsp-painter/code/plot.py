import matplotlib.pyplot as plt
import numpy as np
# visulize the best_path
save_directory = '../output_figure/'
def plot_path(node, name, best_distance, tspfilename, point_amt):
    plt.figure(figsize=(15, 12))
    # 纵坐标取反
    plt.plot(node[:,0], node[:,1], 'o-', markersize=0, linewidth=2, color='k')
    # # 首尾相连
    # plt.plot([node[0][0], node[-1][0]], [node[0][1], node[-1][1]], 'o-', markersize=0, linewidth=0.6,color='k')
    plt.axis('off')  # 隐藏坐标轴
    # 显示标题
    #plt.title(name + ' Distance: ' + str(best_distance) + '\n' + str(error), fontsize=30,fontname="Times New Roman",color="red")

    plt.title(name + ' Distance: ' + str(best_distance) + '\n '  + '  point:' + str(point_amt), fontsize=35,fontname="Times New Roman", color="black")


    name = tspfilename + "__" + str(point_amt) + "point" + ' using ' + name
    plt.savefig(save_directory + name + '.png', dpi=300, bbox_inches='tight')
    # plt.show()
    # plt.close()
    np.save(f"../output_npy/{name}.npy", np.array(node))