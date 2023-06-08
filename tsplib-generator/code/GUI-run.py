#! /usr/bin/env python3
import os
import sys
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import numpy as np

# GUI
root = Tk()
root.title("TSPLIB-Generator")

threshold_value = IntVar(value=128)

img_original = None
img_processed = None
img_out = None
img_label = None

export_flag = False


# 图片读取
def load_image():
    global img_original, img_processed, img_label, img_out
    img_path = filedialog.askopenfilename()

    img_original = Image.open(img_path)
    img_processed = img_original.convert('L')
    width, height = img_processed.size

    img_processed = img_processed.point(lambda p: 255 if p > threshold_value.get() else 0)
    img_out = img_processed

    # 图片转为Numpy数组，黑色像素坐标存入列表
    np_img = np.array(img_processed)
    point_list = []
    for i in range(0, width):
        for j in range(0, height):
            if np_img[j][i] == 0:
                point_list.append((i, j))

    # 标出黑色像素点
    for p in point_list:
        img_original.putpixel(p, (255, 0, 0))

    # 更新Label
    img_processed = ImageTk.PhotoImage(img_original)
    img_label.configure(image=img_processed)
    img_label.image = img_processed

    # 更新黑色像素点数量的 Label
    # point_num_label.configure(text=f"黑色像素点数量：{len(point_list)}")


# 二值化阈值
def threshold_adjust(val):
    global img_original, img_processed, img_label, img_out
    threshold_value.set(int(val))

    img_processed = img_original.convert('L')
    img_processed = img_processed.point(lambda p: 255 if p > threshold_value.get() else 0)
    img_out = img_processed
    img_processed = ImageTk.PhotoImage(img_processed)
    img_label.configure(image=img_processed)
    img_label.image = img_processed


# 导出图片
def export_png():
    global img_out
    global img_processed
    global export_flag
    if not img_processed:
        messagebox.showwarning("提示", "请先打开一张图片！") #中文提示
        return
    img_path = filedialog.asksaveasfilename(defaultextension=".png")
    if not img_path:
        return

    img_out.save(img_path)
    export_flag = True
    messagebox.showinfo("提示", "图片导出成功！")


# 取点数量
def point_number_adjust(val):
    global Point_number
    Point_number = int(val)


def tsp_create():
    global Point_number
    img_path = filedialog.askopenfilename()
    # point_num = int(Point_number.get())
    cmd = sys.executable
    os.system(cmd + " " + f"./stippler.py {img_path} --save \
               --n_point {Point_number} --n_iter 50 --pointsize 1.5 1.5 --figsize 6 \
               --threshold 255 --force --interactive")


# 打开图片
Button(root, text="LOAD", command=load_image).grid(row=0, column=0, padx=5, pady=5)

# 二值化阈值控制条
Scale(root, from_=0, to=255, orient=HORIZONTAL, label="BLK&WHT", variable=threshold_value,
      command=threshold_adjust).grid(row=0,
                                     column=1,
                                     padx=5, pady=5)

# Point_number控制条
Scale(root, from_=1000, to=30500, orient=HORIZONTAL, label="POINTS", command=point_number_adjust).grid(row=0, column=2,
                                                                                                       padx=5, pady=5)

# 导出按钮
Button(root, text="EXPORT", command=export_png).grid(row=1, column=0, padx=5, pady=5)

# tsp按钮
Button(root, text="TSP-CREATE", command=tsp_create).grid(row=0, column=3, padx=5, pady=5)

# # 创建黑色像素点数量的 Label
# point_num_label = Label(root, text="黑色像素点数量：0")
# point_num_label.grid(row=0, column=4, padx=5, pady=5)

# 创建图片展示的 Label
img_label = Label(root)
img_label.grid(row=3, column=0, columnspan=5)

root.mainloop()
