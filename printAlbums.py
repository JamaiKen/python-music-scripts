import os
from tinytag import TinyTag as tt

# list for album titles
AlbumList = []

# work
for dirpath, dirs, files in os.walk("/home/syran/Media/Music/Wayne"):
	for file in files:
		if file.endswith(".mp3"):			# only process .mp3 files
			fname = os.path.join(dirpath,file)	# get file path
			tag = tt.get(fname)			# extract file tag info
			if tag.album not in AlbumList:
				AlbumList.append(tag.album)	# add to list

# print list
for album in AlbumList:
	print album							
