# Author: Kenneth Bailey
# Date: 12/6/2016
# Prog: python script to process new downloads

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
trackCount = 0

if str(sys.argv[1]).endswith(".zip"):
	# extract files
	zfile = zz.ZipFile(str(sys.argv[1]))
	zfile.extractall(tempFolder)	
	
	# examine files
	for dirpath, dirs, files in os.walk(tempFolder):
		for file in files:
			if file.endswith((".mp3",".m4a")):
				trackCount += 1
				
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

	# print album info
	if len(albums) == 1: 
		print("Album: %s" % albums[0])
	elif len(albums) == 0:
		print "Album: none listed"
	else:
		print "Multiple Albums!"
	# print album artist info
	if len(aartists) == 1:
		print ("Album Artist: %s" % aartists[0])
	elif len(aartists) == 0:
		print "Album Artist: none listed"
	else:
		print "Multiple Album Artists!"
	# print artist info
	if len(artists) == 1:
		print("Artist: %s" % artists[0])
	elif len(artists) == 0:
		print "Artist: none listed"
	else:
		print "Muliple Artists!"
	# print year info
	if len(years) == 1:
		print("Year: %s" % years[0])
	elif len(years) == 0:
		print "Year: none listed"
	else:
		print "Multiple Years!"
	# print genre info
	if len(genres) == 1:
		print("Genre: %s" % genres[0])
	elif len(genres) == 0:
		print "Genre: none listed"
	else:
		print "Multiple Genres"
	# print track count info
	print("# tracks: %s" % trackCount)
	# print bitrate info
	if len(bitrates) == 1:
		print("Bitrate: %s" % bitrates[0])
	else:
		print "Multiple Bitrates: ",
		for bit in bitrates:
			print bit,			
			
 
else:
	print "Improper arguments! .zip files only!"


