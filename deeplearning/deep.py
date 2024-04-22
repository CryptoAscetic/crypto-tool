import json
import os

import numpy as np


def json2txt(path_json, path_txt):
    with open(path_json, 'r', encoding='gb18030') as path_json:
        jsonx = json.load(path_json)
        with open(path_txt, 'w+') as ftxt:
            for shape in jsonx['shapes']:
                xy = np.array(shape['points'])
                label = str(shape['label'])
                if label == '1':
                    label = '1'
                elif label == '2':
                    label = '2'
                elif label == '3':
                    label = '3'
                else:
                    label = '4'
                label += ' '
                strxy = ''
                for m, n in xy:
                    strxy += str(m) + ' ' + str(n) + ' '
                label += strxy
                ftxt.writelines(label + "\n")


dir_json = '/home/hfg/Desktop/数据标注/image3/json/'
dir_txt = '/home/hfg/Desktop/数据标注/image3/txt/'
if not os.path.exists(dir_txt):
    os.makedirs(dir_txt)
list_json = os.listdir(dir_json)
for cnt, json_name in enumerate(list_json):
    print('cnt=%d,name=%s' % (cnt, json_name))
    path_json = dir_json + json_name
    path_txt = dir_txt + json_name.replace('.json', '.txt')
    print(path_json, path_txt)
    json2txt(path_json, path_txt)
