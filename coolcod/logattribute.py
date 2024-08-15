
import os
import json
from datetime import datetime

class FileToObject:
    def __init__(self, path, name=None, size=None, cursor=0, senddate=None, createdate=None):
        self.path = path
        self.name = name
        self.size = size
        self.cursor = cursor
        self.senddate = senddate
        self.createdate = createdate

        if name is None:
            self.name = os.path.basename(path)
        if size is None:
            self.size = os.path.getsize(path)
        if createdate is None:
            self.createdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def append_log(file_path, log_path='log.json'):
    file_obj = FileToObject(file_path)
    log_entry = {
        "path": file_obj.path,
        "name": file_obj.name,
        "size": file_obj.size,
        "cursor": file_obj.cursor,
        "senddate": file_obj.senddate.strftime('%Y-%m-%d %H:%M:%S') if file_obj.senddate else None,
        "createdate": file_obj.createdate
    }

    if not os.path.exists(log_path):
        with open(log_path, 'w') as file:
            json.dump([], file)

    with open(log_path, 'r+') as file:
        logs = json.load(file)
        logs.append(log_entry)
        file.seek(0)
        json.dump(logs, file, indent=4)


def get_log(file_path, target_json='log.json'):
    log_checker(file_path, target_json)
    with open(target_json, 'r') as file:
        logs = json.load(file)
        for log in logs:
            if log['path'] == file_path:
                # Extract only relevant keys
                file_data = {"path": log["path"], "size": log["size"],
                             "cursor": log["cursor"], "senddate": log.get("senddate"),
                             "createdate": log["createdate"]}
                return FileToObject(**file_data)
    return None


def update_log(file_path, attribute, new_data, target_json='log.json'):
    log_checker(file_path, target_json)
    with open(target_json, 'r+') as file:
        logs = json.load(file)
        for log in logs:
            if log['path'] == file_path:
                if isinstance(new_data, datetime):
                    new_data = new_data.strftime('%Y-%m-%d %H:%M:%S')
                log[attribute] = new_data
                break
        file.seek(0)
        json.dump(logs, file, indent=4)
        file.truncate()

def log_checker(file_path, target_json='log.json'):
    if json_checker(target_json):
        append_log(file_path, target_json)
    log_found = False
    with open(target_json, 'r') as file:
        logs = json.load(file)
        for log in logs:
            if log['path'] == file_path:
                log_found = True
                break

    if not log_found:
        append_log(file_path, target_json)

def json_checker(target_json='log.json'):
    return os.path.exists(target_json)

file_path = 'C:\\Windows\\System32\\winevt\\Logs\\Microsoft-Windows-WinINet-Config%4ProxyConfigChanged.evtx'

append_log(file_path)
