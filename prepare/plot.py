#!/usr/bin/python
#coding:utf-8

import sys
import numpy as np
import matplotlib.pyplot as plt

#详情请看https://matplotlib.org/tutorials/index.html#introductory

plt.figure() #创建新图

x = np.linspace(1,2,20)
y1 = x
y2 = 2*x
y3 = 3*x
print y3

#plt.xticks(()) #去掉x轴刻度


#子图1
plt.subplot(3,1,1)

plt.ylim((0.5,2.5))
plt.xlabel(r'$height$') #让字体更好看,显示不出来不知道为啥
'''
#设置坐标轴位置
ax = plt.gca()
ax.xaixs.set_ticks_position('bottom') #'AxesSubplot' object has no attribute 'xaixs'，应该是子图中不让设置坐标轴位置
ax.spines['bottom'].set_position(('data',-1))
'''
T = np.arctan2(y1,x) #设置好看的颜色
plt.scatter(x,y1,c=T,alpha=0.5) 

#子图2
plt.subplot(3,1,2)
plt.ylim((1,5))
x_ticks = np.linspace(1,2,5)
plt.xticks(x_ticks) #设置刻度
l, = plt.plot(x,y2) #必须要加逗号
#设置legend
plt.legend(handles=[l,],labels=['line'],loc='best')

#子图3
plt.subplot(3,1,3)
plt.xlim((1,2))
plt.ylim((1,8))
plt.bar(x,y3,facecolor='blue',edgecolor='white') #这个bar显示的有点问题

plt.show() #最后show一下