import socket
import os

def send_to_server(data, ip, port):
    try:
        print("Sunucuya bağlanılıyor...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((ip, port))
            print(f"Sunucuya bağlandı: {ip}:{port}")
            sock.sendall(data)
            print("Veri sunucuya başarıyla gönderildi.")
    except Exception as e:
        print(f"Sunucuya gönderirken hata oluştu: {e}")

def save_to_file(data, file_name):
    try:
        print("Veri dosyaya kaydediliyor...")
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'log', file_name)

        with open(file_path, 'ab') as file:  
            file.write(data)
        print(f"Veriler {file_name} dosyasına başarıyla kaydedildi.")
    except Exception as e:
        print(f"Veriyi dosyaya kaydederken hata oluştu: {e}")
