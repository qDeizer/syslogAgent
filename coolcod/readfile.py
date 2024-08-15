import time

def read_file(file_path, cursor_konumu):

    
    with open(file_path, 'rb') as file:
        file.seek(cursor_konumu)
        
        yeni_veri = file.read()
        
        yeni_cursor_konumu = file.tell()

        
    return yeni_cursor_konumu, yeni_veri



