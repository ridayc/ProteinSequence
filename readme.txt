Some short remarks of how to create the secondary structure files needed to create a secondary structure trainingset

1. First download the most recent collection of secondary structures based on the protein database from Kabsch and Sanders translation website:

#this is a terminal command which requires wget and time stamps the file you download from the site.
wget https://cdn.rcsb.org/etl/kabschSander/ss.txt.gz -O ${DATE_STAMP}-ss.txt.gz

2. The Python file generate_ss_files contains a generate_files function which takes this file and a directory name and puts each secondary structure into it's own file. This is so we can avoid having to due random access lookups in the ss file. All ss files are put into the directory dir

3. The three generate_training files will create a training file as well as a file stating which files the trainingdata came from and at which location in the sequence.
(comments are still lacking though)