# watchfile.py

import os

def watch_file(file_path, taken_size=0):
    """
    Dosya boyutunu kontrol eder ve yeni veri geldiğinde yeni boyutu döndürür.
    
    :param file_path: İzlenecek dosyanın yolu.
    :param taken_size: Mevcut dosya boyutu.
    :return: (yeni_boyut, yeni_veri_var_mi)
    """
    # İlk durumda veya çağrıdan gelen mevcut boyut
    if taken_size == 0:

        current_size = os.path.getsize(file_path)
        return current_size, True
    else:
        previous_size=taken_size


    # Şu anki dosya boyutunu al
    current_size = os.path.getsize(file_path)

    if current_size > previous_size:
        
        return current_size, True
    
    return previous_size, False
