import os
import random
import csv

def create_trainingset(dir,ntrain,ntest,pftr,pfte,width):
	# get all file names in a list
	names = os.listdir(dir)
	# shuffle the names to get a random subset
	random.shuffle(names)
	try:
		trnames = names[:ntrain]
		tenames = names[ntrain:ntrain+ntest]
	except:
		print("Not enough files for training and test set")
	f = open("training.csv","w")
	f2 = open("trainingnames.csv","w")
	for i in trnames:
		try:
			p,loc = training_points(dir,i,pftr,width)
			f2.write(i[:-3]+"\n")
			f2.write(','.join(map(str,loc))+"\n")
			for j in p:
				f.write(','.join(j)+"\n")
		except:
			print("Check "+i+" for errors")
	f2.close()
	f.close()
	f = open("testing.csv","w")
	f2 = open("testingnames.csv","w")
	for i in tenames:
		try:
			p,loc = training_points(dir,i,pfte,width)
			f2.write(i[:-3]+"\n")
			f2.write(','.join(map(str,loc))+"\n")
			for j in p:
				f.write(','.join(j)+"\n")
		except:
			print("Check "+i+" for errors")
	f2.close()
	f.close()
	
		
def training_points(dir,filename,num,width):
	with open(dir+os.sep+filename, newline='') as csvfile:
		try:
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
		except:
			print("Not a proper csv file for this application")
	points = []
	loc = []
	for i in range(num):
		loc.append(random.randrange(len(seq)))
		p = ['-']*(2*width+2)
		for j  in range(width+1):
			if(loc[i]-j>=0):
				p[width-j] = seq[loc[i]-j]
			if(loc[i]+j<len(seq)):
				p[width+j] = seq[loc[i]+j]
		p[-1] = ss[loc[i]]
		points.append(p)
	return points,loc

