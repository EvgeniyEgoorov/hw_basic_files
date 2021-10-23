import os
from pprint import pprint


def sorted_catalog(path):
    all_data = []
    for file_name in os.listdir(path):
        if file_name.endswith(".txt"):
            with open(file_name, mode='r', encoding='utf-8') as file:
                line_count = 0
                for line in file:
                    line_count += 1
            with open(file_name, mode='r', encoding='utf-8') as content:
                data = {'file_name': file_name, 'line_count': line_count, 'content': content.read()}
            all_data.append(data)
    sorted_data = sorted(all_data, key=lambda k: k['line_count'])
    for files in sorted_data:
        for values in files.values():
            print(values)


sorted_catalog(os.path.join(os.getcwd()))
