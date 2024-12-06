import json
import os

name2id = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6}


def convert(img_size, box):
    dw = 1. / (img_size[0])
    dh = 1. / (img_size[1])
    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = abs(box[2] - box[0])
    h = abs(box[3] - box[1])
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def decode_json(json_floder_path, txt_outer_path, json_name, is_convert=True):
    if not json_name.endswith(".json"):
        return
    txt_name = os.path.join(txt_outer_path, json_name[json_name.rfind("/") + 1:-5] + '.txt')

    with open(txt_name, 'w') as f:
        json_path = os.path.join(json_floder_path, json_name)
        data = json.load(open(json_path, 'r', encoding='gb2312', errors='ignore'))
        img_w = data['imageWidth']
        img_h = data['imageHeight']
        isshape_type = data['shapes'][0]['shape_type']
        print(isshape_type)
        for i in data['shapes']:
            label_name = i['label']
            if (i['shape_type'] == 'polygon'):
                x_max = 0
                y_max = 0
                x_min = float("inf")
                y_min = float("inf")
                for lk in range(len(i['points'])):
                    x1 = float(i['points'][lk][0])
                    y1 = float(i['points'][lk][1])
                    if x_max < x1:
                        x_max = x1
                    if y_max < y1:
                        y_max = y1
                    if y_min > y1:
                        y_min = y1
                    if x_min > x1:
                        x_min = x1
                bb = (x_min, y_max, x_max, y_min)
            if (i['shape_type'] == 'rectangle'):
                x1 = float(i['points'][0][0])
                y1 = float(i['points'][0][1])
                x2 = float(i['points'][1][0])
                y2 = float(i['points'][1][1])
                bb = (x1, y1, x2, y2)
            if is_convert:
                bbox = convert((img_w, img_h), bb)
            else:
                bbox = bb
            try:
                f.write(str(name2id[label_name]) + " " + " ".join([str(a) for a in bbox]) + '\n')
            except:
                pass


if __name__ == "__main__":
    json_floder_path = r'/home/hfg/Desktop/111/image6/json/'  # 请将json文件放在该文件夹下
    txt_outer_path = r'/home/hfg/Desktop/111/image6/txt/'
    json_names = os.listdir(json_floder_path)
    print("共有：{}个文件待转化".format(len(json_names)))
    flagcount = 0
    for json_name in json_names:
        decode_json(json_floder_path, txt_outer_path, json_name, is_convert=True)  # 这里设置是否要缩放坐标，如果为False则不用缩放
        flagcount += 1
        print("还剩下{}个文件未转化".format(len(json_names) - flagcount))
    print('转化全部完毕')
