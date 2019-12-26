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
    pathHelper=path.split(os.sep)
    pathHelper=pathHelper[:2]
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
