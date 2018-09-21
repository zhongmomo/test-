#!/usr/bin/python
# -*- coding: UTF-8 -*-

import spacy
import numpy as np
#from numba import jit

#@autogit
def delete_words(word_list,matrix,path):
	nlp = spacy.load('en_core_web_sm')

	paragraph_list = []
	#total_cnt = 0
	total_cnt = -1
	del_cnt = 0

	#delwords_path = "/home/zzm/prepare/file/delete_words_list.csv"
	delwords_path = "./file/delete_words_list.csv"
	result_f = open(delwords_path,"a") 
	delwords_list = []

	for i in range(len(word_list)):
		paragraph = u""+word_list[i]
		paragraph_list.append(paragraph)

	#for k in range(8):
	for k in range(len(word_list)):
		paragraph = nlp(paragraph_list[k])
		total_cnt += 1
		token_cnt = 0

		flag = 0  
		for word in paragraph:
			#print word,word.pos_
			if (word.pos_=='NOUN' or word.pos_=='ADJ' or word.pos_=='ADV' or word.pos_ =='VERB'):
				flag = 1 #1为留
			token_cnt += 1

		#被分词为多个的，以及词性不符合要求的都要删除
		if token_cnt!=1 or flag==0:
			
			print>>result_f,str(k)+":"+word_list[total_cnt-del_cnt]
			delwords_list.append(k)
			
			matrix = np.delete(matrix,total_cnt-del_cnt,axis=0)
			del word_list[total_cnt-del_cnt]
			del_cnt += 1

	print "delete words: "+str(del_cnt)

	#写入csv文件
	np.savetxt(path,matrix,delimiter=",",fmt = '%f')
	print np.shape(matrix)

	return delwords_list