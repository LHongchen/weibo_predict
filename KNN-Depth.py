#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 21:40
# @Author  : Moxiaofei
# @Site    : 
# @File    : KNN-Depth.py
# @Software: PyCharm
# 在微博转发深度下 KNN 预测50条数据误差 0.39011226930963766
import pandas as pd
import matplotlib.pyplot as plt
# 导入KNN模型
from sklearn.neighbors import KNeighborsClassifier

# 读取数据
source = pd.read_csv('depthlast.csv', sep=' ')
# 定义用于训练时的特征
x_col = ["emotional_level", "fans_num", "at_flag", "topic_flag", "url_flag", "content_length", "time_step", 'depth1',
         'depth2']
# 定义自变量和目标变量
x_train = source[x_col][:9737]
y_train = source['depth9'][:9737]
# 定义需要预测的自变量和目标变量
predict_value = source[x_col][9737:]
true_value = source['depth9'][9737:]
# 建立模型
model = KNeighborsClassifier()
# 训练模型
model.fit(x_train, y_train)
# 预测测试数据
pre_value = model.predict(predict_value)
# 计算平均绝对百分比误差
avg_error = ((abs(pre_value-true_value)/true_value).sum())/len(pre_value)
print(avg_error)
# 画图展示预测值与真实值之间的关系
plt.figure(figsize=(7, 5))
x1 = x2 = range(0, 50)
y1 = true_value
y2 = pre_value
plt.plot(x1, y1, 'r', label='true value', linewidth=1)
plt.plot(x2, y2, '--b', label='predict value', linewidth=1)
plt.xlabel('microblog number')
plt.ylabel('depth')
plt.legend()
plt.savefig('KNN-depth-50.png', dpi=400, bbox_inches='tight')
plt.show()
