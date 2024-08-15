
import os
import coolcod.findfile as ff
import coolcod.senddata as sd
import coolcod.watchfile as wf
import coolcod.readfile as rf
import coolcod.appendData as ad
import coolcod.logattribute as la
from datetime import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))

log_dir = os.path.join(base_dir, 'log')
etl_dir = os.path.join(base_dir, 'etlLOG')

os.makedirs(log_dir, exist_ok=True)
os.makedirs(etl_dir, exist_ok=True)

server_ip = "192.168.1.100"
server_port = 5000

ff.existing_file_path()

while True:
    print("Mevcut dosya listesi okunuyor...")
    try:
        with open(os.path.join(log_dir, 'existing_files.txt'), 'r') as file:
            for file_path in file:
                try:
                    file_path = file_path.strip()
                    print(f"Dosya izleniyor: {file_path}")
                    
                    if wf.watch_file(file_path):
                        print(f"Yeni veri tespit edildi: {file_path}")
                        
                        log = la.get_log(file_path)
                        print(f"Log bilgisi alındı: {log}")
                        
                        newcursloc, newdata = rf.read_file(file_path, log.cursor)
                        print(f"Dosyadan yeni veri okundu. Yeni cursor konumu: {newcursloc}")
                        
                        ad.append_data(newdata, os.path.join(etl_dir, log.name), file_path)
                        print(f"Yeni veri ETL dosyasına kaydedildi: {log.name}")
                        
                        la.update_log(file_path, 'cursor', newcursloc)
                        print(f"Log dosyası güncellendi: cursor -> {newcursloc}")
                        
                        la.update_log(file_path, "senddate", datetime.now())
                        print(f"Log dosyası güncellendi: senddate -> {datetime.now()}")

                        print("Veri dosyaya kaydediliyor ve sunucuya gönderiliyor...")
                        sd.save_to_file(newdata, 'etl_log.bin')
                        sd.send_to_server(newdata, server_ip, server_port)
                        print("Veri işleme tamamlandı.")
                        print("Yeni veri bekleniyor...")
                    
                except Exception as e:
                    print(f"Dosya işlenirken hata oluştu{file_path}: {e}")
    except Exception as e:
        print(f"mevcut dosya listesini açarken hata oluştu. {e}")
