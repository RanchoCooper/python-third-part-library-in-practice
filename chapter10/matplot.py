#!/usr/bin/env python
# encoding: utf-8
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 绘制点
    x = [1, 2]
    y = [2, 4]
    plt.axis([0, 10, 0, 10])    # 定义坐标轴范围
    plt.scatter(x, y)
    plt.show()

    # 绘制折线
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    plt.plot(input_values, squares, linewidth=5)    # linewidth设置线条粗细
    plt.title("Numbers", fontsize=24)               # 设置标题和字体大小
    plt.xlabel("Value", fontsize=14)                # 添加标签
    plt.ylabel("ARG Value", fontsize=14)
    plt.tick_params(axis='both', labelsize=10)      # 设置单位刻度的大小
    plt.show()
