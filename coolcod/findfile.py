
import os
import glob

def find_files(start_dir='C:\\', existing_file_path= 'C:\\logRead\\existing_files.txt', extensions=['.evtx', '.etl']):


    print("Mevcut dosya konumlarını okunuyor")
    if os.path.exists(existing_file_path):
        with open(existing_file_path, 'r') as f:
            existing_files = set(f.read().splitlines())
    else:
        existing_files = set()

    print("tum dosyalar bulunuyor")
    all_files = []
    for extension in extensions:
        all_files.extend(glob.glob(os.path.join(start_dir, '**', f'*{extension}'), recursive=True))
    all_files = set(all_files)

    print("yeni dosyalar bulunuyor")
    new_files = all_files - existing_files

    print("yeni kodumlari ekle")
    if new_files:
        with open(existing_file_path, 'a') as f:
            for file in new_files:
                f.write(file + '\n')

    return list(new_files)

start_directory = 'C:\\'
existing_file_path = 'existing_files.txt'
print("ekrana yazdiriliyor")
new_files = find_files(start_directory, existing_file_path)
print("Yeni bulunan dosyalar:")
for file in new_files:
    print(file)
