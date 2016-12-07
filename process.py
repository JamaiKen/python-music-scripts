# Author: Kenneth Bailey
# Date: 12/6/16
# Prog: python script to process new illegal downloads

import zipfile as zz
import os 
from tinytag import TinyTag as tt
import sys

# temp extraction folder
tempFolder = "/home/syran/Sandbox/temp/"

# temp storage
albums = []
aartists = []
artists = []
years = []
genres = []
bitrates = []


if str(sys.argv[1]).endswith(".zip"):
	# extract files
	zfile = zz.ZipFile(str(sys.argv[1]))
	zfile.extractall(tempFolder)	
	
	# examine files
	for dirpath, dirs, files in os.walk(tempFolder):
		for file in files:
			if file.endswith((".mp3",".m4a")):
				# get file name
				fname = os.path.join(dirpath,file)

				# get tag info
				tag = tt.get(fname)
				
				# checks
				if tag.album not in albums: albums.append(tag.album)
				if tag.albumartist not in aartists: aartists.append(tag.albumartist)
				if tag.artist not in artists: artists.append(tag.artist)
				if tag.bitrate not in bitrates: bitrates.append(tag.bitrate)
				if tag.genre not in genres: genres.append(tag.genre)
				if tag.year not in years: years.append(tag.year)

	# print info
	if len(albums) == 1: 
		print("Album: %s", % albums[0]
	else if len(albums) == 0:
		print "Album: none listed"
	else:
		print "Multiple Albums!"

	print "\n Album Artist: ".join(str(p) for p in aartists)
	print "\n Artist: ".join(str(p) for p in artists)
	print "\n Year: ".join(str(p) for p in years)
	print "\n Genre: ".join(str(p) for p in genres)
	print "\n Bitrate: ".join(str(p) for p in bitrates) 	
else:
	print "booo"
