#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import numpy as np
from numpy import *

#设置默认的编码方式
reload(sys) 
sys.setdefaultencoding( "utf-8" )

def readGlove(path1,column):
	fp = open(path1,"r")
	content = fp.read()
	fp.close()

	rowlist = content.splitlines()
	print len(rowlist)

	row_seq = 0
	word_list = []
	total_list = []
	d = " "
	for row in rowlist:
		row_list = row.split(d)
		word_list.append(row_list[0])
		#将单词名字更改为序号
		row_list[0] = row_seq
		for i in range(1,len(row_list)):
			row_list[i] = float(row_list[i])
		total_list.append(row_list)
		row_seq+=1

	matrix = np.array(total_list)
	print np.shape(matrix)
	#print type(matrix[0][0])
	#print type(matrix[0][1])

	return matrix,word_list
