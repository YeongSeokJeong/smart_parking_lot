import xml.etree.ElementTree as ET
import os
import cv2
import numpy as np
def get_info(file_name):
    file_info = {'file_name':file_name, 'file_num': '', 'boxes':[]}
    ignore_area = {'file_name':file_name, 'region':[]}
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
            
    frames = root.findall("frame")
    for frame in frames:
        file_info['file_num'] = frame.attrib['num']
        for target in frame.findall("target_list"):
            box_list = []
            for u in target.findall("target"):
                box = u.find('box').attrib
                box_list.append({
                    'x':box['left'],
                    'y':box['top'],
                    'w':box['width'],
                    'h':box['height'],
                    'label':0
                })
            file_info['boxes'].append(box_list)
    return (ignore_area, file_info)
# xml 파일에서 bound box와 ignore region의 영역을 읽어옴

def make_black_box(img, img_igarea):
    for box in img_igarea:
        x = int(float(box['x'])+1)
        y = int(float(box['y'])+1)
        w = int(float(box['w'])+1)
        h = int(float(box['h'])+1)
        img[x : x+w , y:y+h] = 0
    return img
# 이미지에서 불필요한 부분을 삭제함

def read_img(img_path):
	img = cv2.imread(img_path)
	return img