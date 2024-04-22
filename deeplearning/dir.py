import json
import os

import numpy as np

# 类和索引
CLASSES = ["1", "1"]


def convert(size, box):
    '''
    input:
    size:(width,height);
    box:(x1,x2,y1,y2)
    output:
    (x,y,w,h)
    '''
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


# json -> txt
def json2txt(path_json, path_txt):
    with open(path_json, "r") as path_json:
        jsonx = json.load(path_json)
        width = int(jsonx["imageWidth"])  # 原图的宽
        height = int(jsonx["imageHeight"])  # 原图的高
        with open(path_txt, "w+") as ftxt:
            # 遍历每一个bbox对象
            for shape in jsonx["shapes"]:
                obj_cls = str(shape["label"])  # 获取类别
                cls_id = CLASSES.index(obj_cls)  # 获取类别索引
                points = np.array(shape["points"])  # 获取(x1,y1,x2,y2)
                x1 = int(points[0][0])
                y1 = int(points[0][1])
                x2 = int(points[1][0])
                y2 = int(points[1][1])
                # (左上角,右下角) -> (中心点,宽高) 归一化
                bb = convert((width, height), (x1, x2, y1, y2))
                ftxt.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + "\n")


if __name__ == "__main__":
    # json文件夹
    dir_json = r'/home/hfg/Desktop/数据标注/image1/json/'
    # txt文件夹
    dir_txt = r'/home/hfg/Desktop/数据标注/image1/txt/'
    if not os.path.exists(dir_txt):
        os.makedirs(dir_txt)
    # 得到所有json文件
    list_json = os.listdir(dir_json)
    # 遍历每一个json文件,转成txt文件
    for cnt, json_name in enumerate(list_json):
        print("cnt=%d,name=%s" % (cnt, json_name))
        path_json = dir_json + json_name
        path_txt = dir_txt + json_name.replace(".json", ".txt")
        # (x1,y1,x2,y2)->(x,y,w,h)
        json2txt(path_json, path_txt)
