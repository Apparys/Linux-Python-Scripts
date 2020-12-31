from  os import chdir
from shutil import move
from glob import glob
#<------------------------------------------------------------------------------------------------->


d_path = '/home/{user}/Downloads/'
remove = ("[", "]", "'")
#Intructions for glob, folders where to put the files. It's an example
tri = {
      '*.pdf':'/home/{user}/Documents',
       '*.txt':'/home/{user}/Documents',
       '*.py':'/home/{user}/Python',
       '*.jpg':'/home/{user}/Images',
       '*.png':'/home/{user}/Images',
       '*.odt':'/home/{user}/Documents',
       '*.csv':'/home/{user}/Python/csv',
       }
#<------------------------------------------------------------------------------------------------->


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
                move(d_path + file, '/home/{user}/Fichiers_existants')  


tri_downloads()

