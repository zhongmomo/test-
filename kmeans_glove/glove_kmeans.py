#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
from numpy import *
import sys
from readGlove import *
from k_means import *
from test.cosine import *
import spacy
from delete_words import *

#设置默认的编码方式
reload(sys) 
sys.setdefaultencoding( "utf-8" )

def main():
	
	#定义读取和写入的文件路径
	path1 = "./file/glove.6B.50d.txt"
	#path1 = "/home/zzm/prepare/file/glove.6B.50d.txt"
	path2 = "./file/glove50d_del3.csv"
	#path2 = "/home/zzm/prepare/file/glove50d_del2.csv"
	colnumn = 50 #词向量50维
	matrix,word_list = readGlove(path1,colnumn)
	print len(word_list)

	#进行删词处理
	delwords_list = delete_words(word_list,matrix,path2)

	#同样对100d 200d 300d进行删词处理

	#利用夹角余弦计算相似度
	#cosine(word_list)

	clusters = 200
	kmeans(path2,clusters,word_list)

if __name__ == '__main__':
	main()