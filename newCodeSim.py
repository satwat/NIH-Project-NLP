from __future__ import division
import os
import re
import editdistance 


count =10

path_selDep =os.getcwd()+'/DataC/selectedDep.txt'

path_save = os.getcwd()+'/DataC/fScore.txt'

try:
	os.remove(path_save)
except OSError:
  	pass



def getPair(s1, s2, path):
	fb = open(path, 'r')

	w1=''
	w2=''
	rel1=''
	rel2=''
	dep1=''
	dep2=''

	s1word=[]
	s2word=[]
	s1rel=[]
	s2rel=[]
	s1dep=[]
	s2dep=[]
	for a in fb.readlines():
		st= a.split()
		if str(s1) in st:					
				try:
					w1= a.split()[1]
				except IndexError:
					w1= a.split()[0]
				try:
					rel1=a.split()[2]
				except IndexError:
					rel1=''
				try:
					dep1=a.split()[3]
				except IndexError:
					dep1=''

				s1word.append(w1)	
				s1rel.append(rel1)
				s1dep.append(dep1)

		if str(s2) in st:
				try:
					w2= a.split()[1]
				except IndexError:
					w2= a.split()[0]
				try:
					rel2=a.split()[2]
				except IndexError:
					rel2=''
				try:
					dep2=a.split()[3]
				except IndexError:
					dep2=''

				s2word.append(w2)
				s2rel.append(rel2)
				s2dep.append(dep2)

	return 	s1word,s2word,s1dep,s2dep,s1rel,s2rel

def getSimValue(arr1, arr2):
	simScore = 0
	for word1 in arr1:
		for word2 in arr2:
			if(word1 == word2):
				simScore +=1
				
				

def getOption1Score(word1,word2,dep1,dep2,rel1,rel2):
	simScore=0
	l1=0
	while(l1<len(word1)):
		l2=0
		while(l2<len(word2)):
			w1=word1[l1]
			w2=word2[l2]
			p1=rel1[l1]
			p2=rel2[l2]
			d1=dep1[l1]
			d2=dep2[l2]
			if (w1!='' and w2!='' and w1==w2):
				simScore+=1
				if(d1!='' and d2!='' and d1==d2):
					simScore+=1
				if(p1!='' and p2!='' and p1==p2):
					simScore+=1

	
			l2 +=1
		l1+=1
	totalLen = l1+l2
	print(l1,l2, simScore)
	calcuValue = round((simScore/totalLen),2)
	return calcuValue



fw= open(path_save, 'a')
fw.write("Question #" + "\t" + "Question #" +"\t"+ "Sim Score" +'\n')

outer=1
while(outer <count):
	inner =1
	while(inner<count):
		if(1<2):
			name= os.path.basename(path_selDep).split('.')[0]
		        word1,word2,dep1,dep2,rel1,rel2 = getPair(outer,inner,path_selDep)
			score= getOption1Score(word1,word2,dep1,dep2,rel1,rel2)	
			fw.write(str(outer)+'\t\t'+str(inner)+'\t\t'+str(score) +'\n')
			
		inner= inner+1
	outer=outer+1




