import re
import os

def generate_files(filename,dir):
	try:
		os.mkdir(dir)
	except:
		print("Directory already exists")
	f = open(filename,"r")
	seq = []
	sec = []
	ss = False
	name = ""
	chain = ""
	for line in f:
		label = re.findall(">.*:",line)
		if(label):
			if(re.findall("sequence",line)):
				if(seq):
					f2 = open(dir+os.sep+name+".ss","w")
					f2.write(','.join(seq)+"\n")
					f2.write(','.join(sec)+"\n")
					f2.close()
				ss = False
				name = re.findall(">.*?:",line)
				name = name[0][1:-1]
				chain = re.findall(":.*?:",line)
				name+="_"+chain[0][1:-1]
				if(len(seq)!=len(sec)):
					print("Lengths don't agree in "+name)
				seq = []
				sec = []
			else:
				ss = True
		else:
			if(not ss):
				seq+=list(re.sub("\s","-",line[0:-1]))
			else:
				sec+=list(re.sub("\s","-",line[0:-1]))
	if(seq):
		f2 = open(dir+os.sep+name+".ss","w")
		f2.write(','.join(seq)+"\n")
		f2.write(','.join(sec)+"\n")
		f2.close()