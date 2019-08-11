import sys
import os

winRoot=['C:','Users']
nixRoot=['','home']

#Input of working directory and checks if legit
if(len(sys.argv) > 2 ):
    print("too many arguments, only provide one path under quotation marks")
    sys.exit()
if(!sys.argv[1]):
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

#starting to walk / move / remove

length=len(path.split(os.sep))

for folder,subfolder,files in os.walk(path):
    #moving process
    for j in files:
        preDest=folder.split(os.sep)
        dest=preDest[:length+1]
        os.rename(os.path.join(folder,j),(os.path.join(os.sep.join(dest),j)))
print('files in lvl 1 folders moved')
    #delete empty folders
for folder,subfolder,files in os.walk(path):
    for k in subfolder:
        preSub=os.path.join(folder,k).split(os.sep)
        if(len(preSub)>length+1):                      #length +1 because of empty space before root /
            os.rmdir(os.sep.join(preSub))              #rmdir already checks for empty folder
            print('empty directories removed')

print('program finished')
