import sys
import os

#Input of working directory and checks if legit
if(len(sys.argv) > 2 ):
    print("too many arguments, only provide one path under quotation marks")
    sys.exit()
try:
    path=str(sys.argv[1])
except:
    print('no argument provided')

try:
    os.chdir(path)
    print('the starting directory is: '+str(os.getcwd()))
except:
    print('no such directory')

#starting to walk / move / remove

length=len(path.split('/'))

for folder,subfolder,files in os.walk(path):
    #moving process
    for j in files:
        preDest=folder.split('/')
        dest=preDest[:length+1]
        os.rename(os.path.join(folder,j),(os.path.join('/'.join(dest),j)))
print('files in lvl 1 folders moved')
    #delete empty folders
for folder,subfolder,files in os.walk(path):
    for k in subfolder:
        preSub=os.path.join(folder,k).split('/')
        if(len(preSub)>length+1):                   #length +1 because of empty space before root /
            os.rmdir('/'.join(preSub))              #rmdir already checks for empty folder
            print('empty directories removed')

print('program finished')
