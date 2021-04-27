#!/usr/bin/env python3
import os
import shutil

current_dir = input("Enter the Directory's path which you want to organize: ")
#current_dir = first_current_dir.replace("\","\\");

for a in os.listdir(current_dir):
    os.rename(a, a.replace(" ", ""))

def organize_me(op1, op2, fname):
	for filename in os.listdir(current_dir):
		if filename.endswith((op1, op2)) and filename != "organize.py":
			if not os.path.exists(fname):
				os.mkdir(fname)
			shutil.copyfile(filename, fname)
			os.remove(filename)
			print("Done")	

print("Process may take some minutes if there's big size files")
organize_me(".py",".cpp", "Coding")
organize_me(".jpg", ".png", "Images")
organize_me(".mp4", ".mkv", "Videos")
organize_me(".tar.xz", ".zip", "Extracted")
organize_me(".exe", "whl", "Programs")
organize_me(".torrent", ".iso", "Torrents")
organize_me(".html", ".pdf", "Documents")