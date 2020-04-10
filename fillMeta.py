import eyed3
import sys
import os

winRoot=['C:','Users']
nixRoot=['','home']

#Input of working directory and checks if legit
if(len(sys.argv) > 2 ):
    print("too many arguments, only provide one path")
    sys.exit()
if not(sys.argv[1]):
    print('no argument provided')
    sys.exit()

try:
    path=str(sys.argv[1])
    pathHelper=path.split(os.sep)[:2]

    if(os.name=='nt' and pathHelper != winRoot ):
        raise ValueError('The path must not be outside of the Users directory')
    if(os.name=='posix' and pathHelper != nixRoot):
        raise ValueError('The path must not be outside of the home folder')
except:
    print("fail while checking for home/Users directory")

try:
    os.chdir(path)
    print('the starting directory is: '+str(os.getcwd()))
except:
    print('no such directory')
    sys.exit()

#for root,artist, album, song in os.walk(path):
for artist in os.listdir(path):
	for album in os.listdir(path+"/"+str(artist)):
		for title in os.listdir(path+"/"+str(artist)+"/"+str(album)):
			#print(artist)
			#print(album)
			#print(title[0:-4].strip())
			currentTitle = eyed3.load(path+"/"+str(artist)+"/"+str(album)+'/'+str(title))
			if artist == title[:len(artist)]:
				title=title[len(artist):].strip("_-.")
			currentTitle.tag.artist	=	str(artist)
			currentTitle.tag.album	=	str(album)
			currentTitle.tag.title	= 	str(title[0:-4])
			currentTitle.tag.save(version=eyed3.id3.ID3_V2_4)