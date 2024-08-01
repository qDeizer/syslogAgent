#appendData.py

def append_data(newdata,target_file_path,source_file_path=None):
    """
    Kaynak dosyadan verileri okuyarak hedef dosyaya binary formatında ekler.
    
    :param source_file_path: Okunacak kaynak dosyanın yolu.
    :param target_file_path: Verilerin ekleneceği hedef dosyanın yolu.
    """
    try:
        # # Kaynak dosyayı binary okuma modunda aç
        # with open(source_file_path, 'rb') as source_file:
        #     # Verileri hafızaya al
        #     data = source_file.read()
        
        # Hedef dosyayı binary ekleme modunda aç
        with open(target_file_path, 'ab') as target_file:
            # Verileri hedef dosyaya yaz
            target_file.write(newdata)
        
        print(f"Veriler başarıyla {target_file_path} dosyasına eklendi.")
        
    except FileNotFoundError:
        print(f"{source_file_path} bulunamadı.")
    except IOError as e:
        print(f"Dosya okuma/yazma hatası: {e}")




