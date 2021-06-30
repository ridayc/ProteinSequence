import os
import random
import csv
import jarray
from algolib.algorithms.randomforest import RandomForest
from algolib.algorithms.randomforest import ForestFunctions
from algolib.algorithms.randomforest import RFData
from algolib.algorithms.randomforest.splitsetup import ClassicSetup
from algolib.algorithms.randomforest.splitsetup import MultiSplit
from algolib.algorithms.randomforest.splitsetup import RandomSplitSetup
from algolib.algorithms.randomforest.splitsetup import CVRPSplitSetup
from algolib.algorithms.randomforest.splitmethod import Gini
from algolib.algorithms.randomforest.splitmethod import Entropy
from algolib.algorithms.randomforest.splitmethod import GiniFlip
from algolib.algorithms.randomforest.splitmethod import VarReduc
from algolib.algorithms.randomforest.splitmethod import VarFlip
from algolib.algorithms.randomforest.splitmethod import RankFlip
from algolib.algorithms.randomforest.splitmethod import GiniX
from algolib.algorithms.randomforest.splitmethod import EntropyX
from algolib.algorithms.randomforest.splitmethod import GiniFlipX
from algolib.algorithms.randomforest.splitmethod import VarReducX
from algolib.algorithms.randomforest.splitmethod import VarFlipX
from algolib.algorithms.randomforest.splitmethod import RankFlipX
from algolib.math import VectorFun
from algolib.io import CSVScanner
from java.lang import Class

sym = "-ABCDEFGHIKLMNPQRSTUVWXYZ"
Q8_ = "-CHEBGIPTS"
amino = {}
Q8 = {}
counter = 0
for i in range(len(sym)):
	amino[sym[i]] = counter
	counter+=1
counter = 0
for i in range(len(Q8_)):
	Q8[Q8_[i]] = counter
	counter+=1


def list2jarray2(arr):
	n = len(arr)
	dim = len(arr[0])
	x = jarray.zeros(n,Class.forName("[D"))
	for i in range(n):
		x[i] = jarray.array(arr[i],"d")
	return x

def training_files(dir,num_file):
	names = os.listdir(dir)
	random.shuffle(names)
	try:
		files = []
		current = 0
		for i in range(num_file):
			files.append(names[current:current+num_file[i]])
			current+=num_file[i]
	except:
		print("Not enough files for all training sets")
		return
	f = open("trainingnames.csv","w")
	for i in files:
		f.write("Phase "+str(i)+"\n\n")
		for j in files[i]:
			f.write(j+"\n")
	f.close()
	return files
	
	
def phase0(dir,files,num_points):
	


def neighbors(loc,arr,width,dicname):
	p = ['-']*(2*width+1)
	for i in range(width+1):
		if(loc-i>=0):
			p[width-i] = dicname[arr[loc-i]]
		if(loc+i<len(seq)):
			p[width+i] = dicname[arr[loc+i]]
	return p
	
def label(loc,arr,t):
	if(t==0):
		p = Q8[arr[loc]]
	else:
		if(arr[loc]=="C" or ss[arr]=="S" or ss[arr]=="T"):
			p = Q8["C"]
		elif(ss[arr]=="H" or ss[arr]=="G" or ss[arr]=="I"):
			p = Q8["H"]
		else:
			p = Q8["E"]
	
def single_file_phase0(dir,filename,num_points,width,t):
	with open(dir+os.sep+filename, newline='') as csvfile:
		reader = csv.reader(csvfile,delimiter=',')
		counter = 0
		for row in reader:
			if(counter==0):
				seq = row
			elif(counter==1):
				ss = row
			else:
				break
			counter+=1
	points = []
	for i in range(num):
		if(len(seq)>num):
			loc = random.randrange(len(seq))
		else:
			loc = i
			if(i>=len(seq)):
				break
		p = neighbors(loc,seq,width,amino)
		p.append(label(loc,ss,t))
		points.append(p)
	return points
	
def single_file_phase1(dir,filename,num_points,width,t):
	with open(dir+os.sep+filename, newline='') as csvfile:
		reader = csv.reader(csvfile,delimiter=',')
		counter = 0
		for row in reader:
			if(counter==0):
				seq = row
			elif(counter==1):
				pss = row
			elif(counter==2):
				ss = row
			else:
				break
			counter+=1
	points = []
	for i in range(num):
		if(len(seq)>num):
			loc = random.randrange(len(seq))
		else:
			loc = i
			if(i>=len(seq)):
				break
		p = neighbors(loc,seq,width,amino)
		p+=neighbors(loc,pss,width,Q8)
		p.append(label(loc,ss,t))
		points.append(p)
	return points

def create_trainingset(dir,phase,files,num_points,width,t):
	try:
		os.mkdir(dir+"_"+str(phase))
	except:
		print("Phase directory already exists")
	f.open(dir+"_"+str(phase)+os.sep+"training.csv","w")
	for i in files:
		if(phase==0):
			p = single_file_phase0(dir,i,num_points,width,t)
		else:
			p = single_file_phase1(dir,i,num_points,width,t)
		for j in p:
			f.write(','.join(j)+"\n")
	f.close()
	


def train_forest(dir,phase,rfparam):
	dataset = CSVScanner.data_set(dir+"_"+str(phase)+os.sep+"training.csv",",")
	dim = len(dataset[0])-1
	rfd = RFData(dataset,0,dim,True)
	trainingset = rfd.trainingset()
	traininglabels = rdf.traininglabels2()
	weights = VectorFun.add(jarray.zeros(len(trainingset),"d"),1)
	l = rfd.nclass()
	cl = MultiSplit(jarray.array([1,1,1000,l],'d'),g,len(trainingset[0]),rfparam[0])
	rf = RandomForest(trainingset,traininglabels,weights,categorical,cl,rfparam[1],rfparam[2])
	return rf
	
def 
	
	