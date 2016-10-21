from __future__ import division
import os
import re
import editdistance 



pathr =os.getcwd()+'/DataC/qs.txt'    
path_parsed =os.getcwd()+'/DataC/parses.txt'
path_selDep =os.getcwd()+'/DataC/selectedDep.txt'

count = 1


f= open(pathr,'r')
fPar= open(path_parsed, 'w')
fDep = open(path_selDep, 'w')

for x in f:
	if "Input" in x:
		linenum = fPar.write(str(count)+'\t'+x+'\n')
		count = count+1 			
	else:
		lineblank=fPar.write(x)
		count = count

f= open(pathr,'r')
k=0

for x in f:
	if re.search('ROOT',x):
		k=k+1
		word=fDep.write('\n'+str(k)+' '+x)

	elif re.search(r'\b' + "dep" + r'\b', x):	
		deps = x.strip().lstrip("| +--")
		dep =fDep.write(str(k)+' '+deps+'\n')

	elif re.search(r'\b' + "advcl" + r'\b', x):
		advs = x.strip().lstrip("| +--")
		adv =fDep.write(str(k)+' '+advs+'\n')

	elif re.search(r'\b' + "nsubj" + r'\b', x):
		subjs = x.strip().lstrip("| +--")
		subj =fDep.write(str(k)+' '+subjs+'\n')

	elif re.search(r'\b' + "nsubjpass" + r'\b', x):
		subjs = x.strip().lstrip("| +--")
		subj =fDep.write(str(k)+' '+subjs+'\n')

	elif re.search(r'\b' + "dobj" + r'\b', x):
		dobjs = x.strip().lstrip("| +--")
		dobj =fDep.write(str(k)+' '+dobjs+'\n')


	elif re.search(r'\b' + "iobj" + r'\b', x):	
		objs = x.strip().lstrip("| +--")
		obj =fDep.write(str(k)+' '+objs+'\n')
	
	elif re.search(r'\b' + "csubj" + r'\b', x):
		mods = x.strip().lstrip("| +--")
		mod =fDep.write(str(k)+' '+mods+'\n')
	
	elif re.search(r'\b' + "csubjpass" + r'\b', x):
		mods = x.strip().lstrip("| +--")
		mod =fDep.write(str(k)+' '+mods+'\n')

	elif re.search(r'\b' + "ccomp" + r'\b', x):
		mods = x.strip().lstrip("| +--")
		mod =fDep.write(str(k)+' '+mods+'\n')
	
	elif re.search(r'\b' + "xcomp" + r'\b', x):
		mods = x.strip().lstrip("| +--")
		mod =fDep.write(str(k)+' '+mods+'\n')

	elif re.search(r'\b' + "nmod" + r'\b', x):
		mods = x.strip().lstrip("| +--")
		mod =fDep.write(str(k)+' '+mods+'\n')

	elif re.search(r'\b' + "advmod" + r'\b', x):
		mods = x.strip().lstrip("| +--")
		mod =fDep.write(str(k)+' '+mods+'\n')
	elif re.search(r'\b' + "neg" + r'\b', x):
		mods = x.strip().lstrip("| +--")
		mod =fDep.write(str(k)+' '+mods+'\n')


fPar.close()
fDep.close()

