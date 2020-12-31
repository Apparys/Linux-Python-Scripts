from  os import chdir
from shutil import move
from glob import glob
from time import sleep

d_path = '/home/hector/Téléchargements/'
remove = ("[", "]", "'")
#Intructions for glob, folders where to put the files
tri = {
      '*.pdf':'/home/hector/Documents',
       '*.txt':'/home/hector/Documents',
       '*.py':'/home/hector/Python',
       '*.jpg':'/home/hector/Images',
       '*.png':'/home/hector/Images',
       '*.odt':'/home/hector/Documents',
       '*.csv':'/home/hector/Python/csv',
       }

def tri_downloads():
    chdir(d_path)
    for key, path in tri.items():
        for file in glob(key):
            for element in remove:
                file = file.replace(element, "")
            if file != "": 
            #verification : file has the good extension
                chdir(path)
            if file not in glob('*'):
                #verification : file doesn't exist in the folder
                move(d_path + file, path)  
            else:
                move(d_path + file, '/home/hector/Fichiers_existants')  

tri_downloads()

