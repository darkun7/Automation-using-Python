#!/usr/bin/env python
import os
import re
import shutil
target_dir = 'Intermediate Business English'
cwd = os.getcwd()+"\\"+target_dir
os.chdir( cwd )

def createFolder(dirname):
	if not os.path.exists(dirname):
		try:
			os.mkdir(dirname)
		except OSError:
			print("Fail to create directory")

def moveFile():
	pattern = r"(Lesson [0-9]+)"
	folders = []
	
	for file in os.listdir( cwd ):
		result = re.search( pattern, file )
		if result is not None: 
			folders.append( result.group(0) )
	
	# Create Folder based on Regex resilt
	folders = set( folders )
	for folder in folders:
		createFolder( os.getcwd()+'\\'+folder )
	
	# Move file to their Folder
	for file in os.listdir( cwd ):
		result = re.search( pattern, file )
		file_dir = cwd+'\\'+file
		if result is not None and os.path.isfile(file_dir): 
			shutil.move(file_dir, cwd+'\\'+result.group(0)+'\\'+file)
			print(file, " moved to ", result.group(0))

moveFile()