# main.py

import time
import coolcod.watchfile as wf
import coolcod.readfile as rf
import coolcod.appendData as af
from datetime import datetime

target_file_path = "C:\\Users\\Taha\\Desktop\\bLog.etl"
source_file_path = "C:\\logtry.etl"
current_size = 0
cursorLoc =0

while True:
    # watch_file fonksiyonunu doğru modülden çağır
    current_size, newDataChecki = wf.watch_file(source_file_path, current_size)
    if newDataChecki:
        print(f"Yeni veri geldi, veri boyutu {current_size}")
        cursorLoc,newdata=rf.read_file(source_file_path,cursorLoc)
        now = datetime.now()
        print(type(newdata))
        print(f"{'*'*30}\n{now}  yeni cursor konumu: {cursorLoc}")
        af.append_data(newdata,target_file_path)
    time.sleep(2)
