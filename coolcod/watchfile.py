
from . import logattribute as la
import os

def watch_file(file_path):

    log = la.get_log(file_path)
    

    current_size = os.path.getsize(file_path)
    
    if current_size > log.size or log.senddate==None :
        print(f"{file_path}\ntarafindan {current_size-log.size} boyutunda yeni veri geldi ")
        la.update_log(file_path,"size",current_size)
        return  True
    
    return  False
