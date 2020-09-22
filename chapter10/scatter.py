#!/usr/bin/env python
# encoding: utf-8
import matplotlib.pyplot as plt
from pylab import *

if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False      # 解决保存图像时负号显示为方块的问题

    x_values = [x for x in range(1, 1001)]
    y_values = [x**2 for x in x_values]
    plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)   # 设置点的颜色、移除黑色轮廓、点大小
    plt.title("某地区销售统计表", fontsize=24)
    plt.xlabel("节点", fontsize=14)
    plt.ylabel("销售数据", fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.axis([0, 110, 0, 1100])                     # 设置坐标轴取值范围
    plt.show()
