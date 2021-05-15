import os
import shutil

def movefiles(destinationfolder,filename):
    dest = shutil.move(filename, destinationfolder) 
    print("Destination path:", dest) 
    
    
def search(sourceFolder,destinationFolder):
    for root,dirs,files in os.walk(sourceFolder):
        for file in files: 
            if file.endswith('.mkv'):
                sourcefilepath=root+'/'+str(file)
                movefiles(destinationFolder,sourcefilepath)
    
    
if __name__ == '__main__':
    sourceDir='<insert your source path from where you need to move things>'
    destinationdir='<insert your destination path where you need to keep files>'
    search(sourceDir,destinationdir)     
