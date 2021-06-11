""" this file contains functions for the extraction of protein amino acids sequence and secondary structures from pdb files 
 and prepared dssp files (see extract_dssp.sh script to achieve that)
 For some reason dssp extraction didn't work properly when called using the biopython module
"""

# the biopython module is the only dependency this file has
from Bio.PDB import PDBParser
from Bio.PDB.DSSP import DSSP
import os

# extract the amino acid sequence and secondary structure from a pdb and dssp file and store these in a two-line csv type file
# name is the protein name
# loc_pdb is the folder containing pdb files
# loc_dssp is the folder containing dssp files
# loc_ss is the folder for storing the created ss (secondary structure) file. It will be created if it doesn't exist.
def single_ss(name,loc_pdb,loc_dssp,loc_ss):
	# to avoid the program crashing when errors arise
	try:
		# read out the structure from the pdb and dssp files
		p = PDBParser()
		structure = p.get_structure(name,loc_pdb+os.sep+name+".pdb")
		model = structure[0]
		dssp = DSSP(model, loc_dssp+os.sep+name+".dssp")
		# prepare a 2D list to store the sequence and the secondary structures
		sec = [[],[]]
		# loop over all residuals (amino acid labels) and add the sequence letter of secondary structure
		for a in dssp.keys():
			sec[0].append(dssp[a][1])
			sec[1].append(dssp[a][2])
		# write the sequence and ss to a file
		f = open(loc_ss+os.sep+name+".ss","w")
		f.write(','.join(sec[0])+"\n")
		f.write(','.join(sec[1])+"\n")
		f.close()
	except:
		print("Something went wrong with "+name+".")

# create a file containing the sequence and secondary structure for each dssp file in a target directory
# see folder name definitions for single_ss. SS folder will be created if it doesn't already exist
def all_ss(loc_pdb,loc_dssp,loc_ss):
	# make a directory for the ss files if it doesn't exist
	try:
		os.mkdir(loc_ss)
	except:
		print("Directory already exists")
	# loop over all dssp files in directory loc_ss
	for filename in os.listdir(loc_dssp):
		# cut of the .dssp from the file name
		name = filename[:-5]
		single_ss(name,loc_pdb,loc_dssp,loc_ss)