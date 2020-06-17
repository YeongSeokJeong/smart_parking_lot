import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from send_to_firebase import *
from section import *
from time import sleep
import sys, os
import darknet as dn
import pdb
import cv2
import numpy as np
from skimage import measure
from keras.models import model_from_json
from yolo import *
import pickle as pkl
from car_number_preprocessing import *
# import pyrebase

json_file = open("{}.json".format('car_model'), "r") # json 파일을 먼저 로드한 뒤
loaded_model = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model)
loaded_model.load_weights('car_model.hdf5')
loaded_model.compile(loss = "binary_crossentropy",optimizer = 'adam',metrics = ['accuracy'])
net = dn.load_net("yolov3.cfg".encode('utf-8'), 'yolov3.weights'.encode('utf-8'), 0)
meta = dn.load_meta('coco.data'.encode('utf-8'))
sec_center = [[],[],[],[]]
sec_img = [[],[],[],[]]
illegal_car_count = 0


# firebase
cred = credentials.Certificate('capston-design-2020-117e9-6fe0db86d226.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://capston-design-2020-117e9.firebaseio.com'
})

def get_file_list():
    dir_url = '/home/parking_lot/'
    section_list = ['section1', 'section2', 'section3', 'section4']
    f_list = []

    for sec in section_list:
        url = dir_url + sec
        print(url)
        flist = []
        files = os.listdir(url)
        for f in files:
            url2 = url + '/' + f
            flist.append(url2)
        flist = sorted(flist)
        f_list.append(flist[-1])
    return f_list



def f(imgs_list, imgs_idx):
    #print(len(imgs_list))
    #print(imgs_list[0].shape)
    imgs_list = np.array(imgs_list).reshape(-1, 150, 150, 3)
    #print(len(imgs_list))
    #print(imgs_list.shape)
    pred = np.array(loaded_model.predict(imgs_list))
    pred = list(pred.argmax(axis=1))
    firebase_update(imgs_idx, pred)



#section()
start_flag  = 1
start_input_flag = 1
flag_list = [2,3,2,4]
origin = []
with open('pts.pkl', 'rb') as fr:
    pts_list = pkl.load(fr)

while(True) :
    illegal_car_count = 0
    imgs_list, imgs_idx, start_flag, origin = section(start_flag, origin)
    if start_input_flag == 1:
        imgs_idx = list(range(len(origin)))
        f(origin, imgs_idx)
        start_input_flag = 0
    elif len(imgs_list) != 0 :
        f(imgs_list, imgs_idx)
    char_list, char_idx = predict("1234.jpg")
    print(char_list)
    fire_base_carnum(char_list)

    f_list = get_file_list()
    for i in range(len(f_list)):
        sec_center[i], sec_img[i], cnt = check_section(f_list[i], pts_list[i],flag_list[i],
            sec_center[i], sec_img[i], meta, net)
        illegal_car_count += cnt
    print(illegal_car_count)
    fire_base_illegal(illegal_car_count)
    sleep(30)