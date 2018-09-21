#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pandas as pd
from numpy import *
import sys
from file_process import *

#设置默认的编码方式
reload(sys) 
sys.setdefaultencoding( "utf-8" )

def kmeans(path,clusters,word_list):
	'''
	d = ","
	print "hello"
	matrix = file2matrix(path1,d)
	'''
	#data读入与预处理,要不要加个标准化呢？
	df = pd.read_csv(path,header=0)
	df = df.ix[:,1:] #去掉第一列

	'''
	##降维 !可选可不选
	dimension = 15
	df = pca(df,dimension) 
	'''

	print("start kmeans")
	#MiniBatchKMeans速度于快KMeans，但结果的质量会降低,If n_jobs=-1 all CPUs are used. 
	kmeans = KMeans(n_clusters=clusters,random_state=10,n_jobs=-1).fit(df)
	#kmeans = MiniBatchKMeans(n_clusters=clusters,random_state=10).fit(df)
	print("kmeans over")

	df['label'] = kmeans.labels_
	#统计各个类别的数目
	df_count_type=df.groupby('label').size()

	#定义聚类结果文档
	#result_path = "/home/zzm/prepare/file/glove50_result_del"+str(clusters)+".txt"
	result_path = "./file/glove50_result_del"+str(clusters)+".txt"
	result_f = open(result_path,"a") #a表示用于追加
	##输出各个类别的数目和聚类中心
	print >>result_f,df_count_type
	#print >>result_f,kmeans.cluster_centers_
	#用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
	print >>result_f,"the kmeans.inertia_ is:  "
	print >>result_f,kmeans.inertia_


	#根据label列进行判断，将所有相同label列的序号都取出来
	for i in range(0,clusters): #range包括start，不包括stop
		print >>result_f,"label "+str(i)+"is:\n"
		count = 0
		mini_list = []
		for x in range(0,df.shape[0]):	
			if df['label'][x]==i:
				print >>result_f,word_list[x]
		print >>result_f,"\n\n"
	result_f.close()
'''
	group = list(df.groupby('label'))
	#将每个类别写入不同的文件中
	for i in range(1,clusters+1):
		type_path = "D:/csv/type/"+str(i)+".txt" 
		type_f=open(type_path,"w") 
		print >>type_f,group[i-1][1]
	type_f.close()
	'''
	
'''
	#自动化评估
	for i in range(1,10,1):
		kmeans = KMeans(n_clusters=i,random_state=10).fit(df)
		df['label'] = kmeans.labels_
		#统计各个类别的数目
		df_count_type=df.groupby('label').size()

		##输出各个类别的数目和聚类中心
		print df_count_type
		print kmeans.cluster_centers_
		#用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
		print kmeans.inertia_
'''


'''
	new_df=df[:]
	new_df
	new_df.to_csv('d:/csv/new_df.csv')
'''

#用于降维
def pca(matrix,dimension):
	print("enter pca")
	pca = PCA(n_components=dimension)
	new_matrix = pd.DataFrame(pca.fit_transform(matrix))
	#print new_matrix
	return new_matrix

if __name__ == '__main__':
	main()