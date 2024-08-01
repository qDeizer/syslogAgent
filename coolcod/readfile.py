import time

def read_file(file_path, cursor_konumu):
    """
    Dosyadan belirtilen konumdan itibaren okuma yapar ve yeni cursor konumunu döndürür.
    
    :param file_path: Okunacak dosyanın yolu.
    :param cursor_konumu: Dosyadan okumaya başlanacak konum.
    :return: (yeni_cursor_konumu, yeni_veri)
    """
    
    # Dosyayı binary modunda aç
    with open(file_path, 'rb') as file:
        # Verilen konuma git
        file.seek(cursor_konumu)
        
        # Konumdan sonraki verileri oku
        yeni_veri = file.read()
        
        # Yeni cursor konumunu al
        yeni_cursor_konumu = file.tell()

    # Byte verisini string'e dönüştür, bilinmeyen karakterleri göz ardı et
        
    return yeni_cursor_konumu, yeni_veri



