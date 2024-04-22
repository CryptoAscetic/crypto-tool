import json
import os


def convert(img_size, box):
    x = (box[0] + box[2]) / (2 * img_size[0])
    y = (box[1] + box[3]) / (2 * img_size[1])
    w = (box[2] - box[0]) / img_size[0]
    h = (box[3] - box[1]) / img_size[1]
    x = "%.6f" % x
    y = "%.6f" % y
    w = "%.6f" % w
    h = "%.6f" % h
    return x, y, w, h


def decode_json(json_folder_path, json_name):
    txt_name = r'/home/hfg/Desktop/111/image1/txt/' + json_name.split(".")[0] + '.txt'  # 生成的txt文件存放的路径
    txt_file = open(txt_name, 'w')
    json_path = os.path.join(json_folder_path, json_name)
    data = json.load(open(json_path, 'r', encoding='utf-8'))
    print("----------------", data)
    # print(data["shapes"])
    img_w = data['imageWidth']
    img_h = data['imageHeight']
    path = data["imagePath"]
    imageData = data["imageData"]
    for i in data['shapes']:
        if i['shape_type'] == 'rectangle' and "no" in i['label']:  # 分类的标签
            x1 = float((i['points'][0][0]))
            y1 = float((i['points'][0][1]))
            x2 = float((i['points'][1][0]))
            y2 = float((i['points'][1][1]))
            bb = (x1, y1, x2, y2)
            bbox = convert((img_w, img_h), bb)
            txt_file.write('1' + " " + " ".join([str(a) for a in bbox]) + '\n')
        else:
            x1 = float((i['points'][0][0]))
            y1 = float((i['points'][0][1]))
            x2 = float((i['points'][1][0]))
            y2 = float((i['points'][1][1]))

            bb = (x1, y1, x2, y2)
            bbox = convert((img_w, img_h), bb)
            txt_file.write('0' + " " + " ".join([str(a) for a in bbox]) + '\n')


if __name__ == "__main__":
    json_folder_path = r'/home/hfg/Desktop/111/image1/json/'  # json文件存放的路径
    json_names = os.listdir(json_folder_path)
    for json_name in json_names:
        decode_json(json_folder_path, json_name)
