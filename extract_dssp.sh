# gunzip all pdb.gz files in a directory and create the corresponding dssp files
# prepare a directory for the uncompressed files
mkdir uncomp
# prepare a directory for the dssp files
mkdir dssp
#go through all gz files
for f in *.pdb.gz;
do 
	# gunzip the current file and store it in the uncomp folder
	# we use the sed command to be able to use a regular expression to adapt the names of the target files and locations
	# websearch regex capture expression and back references for more information
	gzip -dcq "$f" > $(echo $f | sed -r "s/(.*)\.gz/uncomp\/\1/");
	# do the dssp conversion of the pdb file and store it in the dssp folder
	dssp $(echo $f | sed -r "s/(.*)\.gz/uncomp\/\1/") $(echo $f | sed -r "s/(.*)\.pdb\.gz/dssp\/\1\.dssp/");
done;