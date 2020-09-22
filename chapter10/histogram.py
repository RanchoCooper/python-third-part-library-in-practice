#!/usr/bin/env python
# encoding: utf-8
import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.title('sex bili', fontsize=24)
    plt.xlabel('sex')
    plt.ylabel('number')
    plt.xticks((1, 2, 3), ('male', 'female', 'unknown'))
    plt.bar(x=(1, 2, 3), height=(1, 2, 5), width=0.2, align='center')
    plt.show()
