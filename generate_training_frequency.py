import os
import random
import csv

sym = "-ABCDEFGHIKLMNPQRSTUVWXYZ"
amino = {}
counter = 0
for i in range(len(sym)):
	amino[sym[i]] = counter
	counter+=1

'''
Create a training set for protein secondary structures. 
dir: the directory containing the secondary structure files
ntrain: number of ss files to take training data from
ntess: number of ss files to take testing data from
pftr: number of data points to take per training file (lower numbers avoid data and training set correlations
pfte: number of data points to take per testing file (lower numbers avoid data and training set correlations
width: number of amino acid sequence neighbors on the right and left side of the data point to take as input dimension (2*width+1 dimensions in total)
t: label type. t==0: potentially 8 different labels, t!=0: 3 different labels. 
'''
def create_trainingset(dir,ntrain,ntest,pftr,pfte,width,t=0):
	# get all file names in a list
	names = os.listdir(dir)
	# shuffle the names to get a random subset
	random.shuffle(names)
	# check if there are enough files for the training and test set
	try:
		trnames = names[:ntrain]
		tenames = names[ntrain:ntrain+ntest]
	except:
		print("Not enough files for training and test set")
		return
	# prepare a file with the training data, and another file with the origin of each data point
	f = open("training.csv","w")
	f2 = open("trainingnames.csv","w")
	# go through all selected training files
	for i in trnames:
		f2.write(i+"\n")
		# get a list of training points from the current file
		p = training_points(dir,i,pftr,width,t)
		# comma separate all dimensions and labels and put them on single lines
		for j in p:
			f.write(','.join(j)+"\n")
	f2.close()
	f.close()
	# similar to the file for training data, just for test data
	f = open("testing.csv","w")
	f2 = open("testingnames.csv","w")
	for i in tenames:
		f2.write(i+"\n")
		p = training_points(dir,i,pfte,width,t)
		for j in p:
			f.write(','.join(j)+"\n")
	f2.close()
	f.close()
	
		
def training_points(dir,filename,num,width,t):
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
		loc = random.randrange(len(seq))
		p = [0]*(2*width+2)*len(amino)
		al = [0]*len(amino)
		ar = [0]*len(amino)
		for j  in range(width+1):
			if(loc-j>=0):
				al[amino[seq[loc-j]]]+=1
				p[(width-j)*len(amino)+amino[seq[loc-j]]]=al[amino[seq[loc-j]]]
			if(loc+j<len(seq)):
				ar[amino[seq[loc+j]]]+=1
				p[(width+j)*len(amino)+amino[seq[loc+j]]]=ar[amino[seq[loc+j]]]
		if(t==0):
			p[-1] = ss[loc]
		else:
			if(ss[loc]=="-" or ss[loc]=="S" or ss[loc]=="T"):
				p[-1] = "-"
			elif(ss[loc]=="H" or ss[loc]=="G" or ss[loc]=="I"):
				p[-1] = "H"
			else:
				p[-1] = "E"
		for j in range(len(p)-1):
			p[j] = str(p[j])
		points.append(p)
	return points

