import xml.etree.ElementTree as ET
import os
import cv2
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import pickle as pkl
from sklearn.model_selection import train_test_split
directory = './DETRAC-Train-Annotations-XML/DETRAC-Train-Annotations-XML/'
directory_list = []
camera_list = sorted(os.listdir(directory))

def get_info(file_name):
    file_info = {'frame_num': [], 'boxes':[]}
    ignore_area = {'file_name':file_name.split('.')[0], 'region':[]}
    doc = ET.parse(directory + file_name)
    root = doc.getroot()
    ignore_region = root.findall("ignored_region")
    for ign in ignore_region:
        for box in ign.findall('box'):
            ignore_area['region'].append({
                'x':box.attrib['left'],
                'y':box.attrib['top'],
                'w':box.attrib['width'],
                'h':box.attrib['height']
            })
    frame_list = []
    frames = root.findall("frame")
    for frame in frames:
        file_info['frame_num'].append(frame.attrib['num'])
        for target in frame.findall("target_list"):
            box_list = []
            for u in target.findall("target"):
                box = u.find('box').attrib
                box_list.append({
                    'x':box['left'],
                    'y':box['top'],
                    'w':box['width'],
                    'h':box['height'],
                    'label':1
                })
            file_info['boxes'].append(box_list)
    return (ignore_area, file_info)

# img_directory = 'DETRAC-train-data/Insight-MVT_Annotation_Train/MVI_20011/img00001.jpg'
# img = cv2.imread(img_directory)
# cv2.rectangle(img, (592,378), (592 + 160, 378 + 162), 2, 2)
# plt.imshow(img)


img_directory = './DETRAC-train-data/Insight-MVT_Annotation_Train/'

def delete_ignore_area(img, img_igarea):
    for box in img_igarea:
        x = int(float(box['x'])+1)
        y = int(float(box['y'])+1)
        w = int(float(box['w']))
        h = int(float(box['h']))
        img[x : x+w , y:y+h] = 0
    return img

def read_data(camera_angle):
    img_list = []
    box_value = []
    angle_number = [str(pixel_num).zfill(5)[-5:] for pixel_num in range(1, len(camera_angle[1]['frame_num'])+1)]
    width, height = 0,0
    for frame_num in angle_number:
        img_file_name = img_directory + camera_angle[0]['file_name'] + '/img' + frame_num + '.jpg'
        img = cv2.imread(img_file_name)
        img = delete_ignore_area(img, camera_angle[0]['region'])
        height, width = img.shape[:2]
        img_list.append(img)
    for step_box in camera_angle[1]['boxes']:
        num_box = []
        for box in step_box:
            x,y,w,h = float(box['x'])-1, float(box['y'])-1, float(box['w'])+1, float(box['h'])+1
            max_x, max_y = x + w, y+h
            box = [1, x/width, y/height, max_x/width, max_y/height]
            num_box.append(box)
        box_value.append(num_box)
    img_list = np.array(img_list)
    box_value = np.array(box_value) 
    return img_list, box_value

camera_list = [get_info(camera) for camera in camera_list]

li = list(range(sum([len(camera[1]['frame_num']) for camera in camera_list])))
print(len(li))
train_idx, test_idx = train_test_split(li, test_size = 0.1)

cnt = 0
for camera in camera_list:
    img, box = read_data(camera)
    print(camera[0]["file_name"])
    print(img.shape, box.shape)
    folder_name = ''

    for i in range(len(img)):
        if (cnt+i) in train_idx:
            folder_name = './train/'
        elif cnt+i in test_idx:
            folder_name = './val/'
        else:
            raise Exception("error")
        cv2.imwrite(folder_name + str(cnt + i) +'.jpg', img[i])
    for i in range(len(box)):
        if cnt+i in train_idx:
            folder_name = './train/'
        else:
            folder_name = './val/'
        with open(folder_name + str(cnt+i) + '.txt', 'w') as fw:
            for box_value in box[i]:
                for value in box_value:
                    print(str(value) + ' ', end = '')
                    fw.write(str(value) + ' ')
                print()
                print()
                fw.write('\n')
    print(cnt,len(img))
    cnt += len(img)