#!/usr/bin/python
#coding:utf-8

import sys
import numpy as np
from numpy import *

#将数据文件读入并转换为矩阵，d为分隔符
def file2matrix(path,d):
	recordlist = []
	print "hello"
	fp = open(path,"rb")
	content = fp.read()
	fp.close()

	#按行转换为一维表
	rowlist = content.splitlines()

	#逐行遍历，结果按分割符分割为行向量
	#map(function,list) 对列表里的每一个元素都执行函数
	#strip删除开头或是结尾的字符
	recordlist = [map(eval,row.split(d)) for row in rowlist if row.strip()]
	return mat(recordlist)

#读取来自DBPedia的RDF数据集，格式上类似于XML文档
#max用来指定读取行数
def readfilelines(path,max=0):
	fp = open(path,"rb")
	ncount = 0 #已读取行
	while True:
		content = fp.readline()
		#判断到文件尾或者读完指定行数
		if content == "" or (ncount>=max and max!=0):
			break
		yield content #返回读取的行
		if max!=0: ncount+=1
	fp.close()


def main():
	path1 = "d:/csv/alarm.csv"
	d = ","
	print "hello"
	matrix = file2matrix(path1,d)
	print(shape(matrix))

	linelist = readfilelines(path1,max=10)
	for line in linelist:
		print line.strip()
		#将每行转换为矩阵
		row_matrix = mat(line.split(d))
		print row_matrix 
		print shape(row_matrix)


if __name__ == '__main__':
	main()