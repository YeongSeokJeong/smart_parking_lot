# -*-coding: utf-8-*-
import pickle as pkl
import cv2
import os
import numpy as np
# import matplotlib.pyplot as plt
from os import rename
from cv2_compare import *

def section(start_flag, origin):

    with open('pts.pkl', 'rb') as fr:
        pts_list = pkl.load(fr)
    pts_list[0]

    dir_url = '/home/parking_lot/'
    section_list = ['section1', 'section2', 'section3', 'section4']

    contrast = []
    note = start_flag
    origin = origin

    for sec in section_list:
        url = dir_url + sec
        print(url)
        flist = []
        files = os.listdir(url)
        for f in files:
            url2 = url + '/' + f
            flist.append(url2)
        flist = sorted(flist)
        file = flist[-1]
        print(file)
        if sec == 'section1':
            # sec 1
            pts = pts_list[0]
            image = cv2.imread(file)
            #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            print("file,",file)
            for i in range(len(pts)):
                pts1 = np.float32([pts[i][0], pts[i][1], pts[i][2], pts[i][3]])
                # 좌표의 이동점
                pts2 = np.float32([[0, 0], [0, 150], [150, 0], [150, 150]])
                M = cv2.getPerspectiveTransform(pts1, pts2)
                dst = cv2.warpPerspective(image, M, (150, 150))
                if note == 1:
                    origin.append(dst)
                elif note == 0:
                    contrast.append(dst)
                #cv2.imwrite('/home/parking_lot/all_sec' + '/sec' + str(i) + '/' + str(file[33:48]) + '.jpg', dst)
        elif sec == 'section2':

            pts = pts_list[1]
            image = cv2.imread(file)
            #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            for i in range(len(pts)):
                pts1 = np.float32([pts[i][0], pts[i][1], pts[i][2], pts[i][3]])
                # 좌표의 이동점
                pts2 = np.float32([[0, 0], [0, 150], [150, 0], [150, 150]])
                M = cv2.getPerspectiveTransform(pts1, pts2)
                dst = cv2.warpPerspective(image, M, (150, 150))
                if note == 1:
                    origin.append(dst)
                elif note == 0:
                    contrast.append(dst)
                #cv2.imwrite('/home/parking_lot/all_sec' + '/sec' + str(i + 9) + '/' + str(file[33:48]) + '.jpg', dst)
        elif sec == 'section3':
            pts = pts_list[2]
            image = cv2.imread(file)
            #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            for i in range(len(pts)):
                pts1 = np.float32([pts[i][0], pts[i][1], pts[i][2], pts[i][3]])
                # 좌표의 이동점
                pts2 = np.float32([[0, 0], [0, 150], [150, 0], [150, 150]])
                M = cv2.getPerspectiveTransform(pts1, pts2)
                dst = cv2.warpPerspective(image, M, (150, 150))
                if note == 1:
                    origin.append(dst)
                elif note == 0:
                    contrast.append(dst)
                #cv2.imwrite('/home/parking_lot/all_sec' + '/sec' + str(i + 19) + '/' + str(file[33:48]) + '.jpg', dst)
        else:
            pts = pts_list[3]
            image = cv2.imread(file)
            #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            for i in range(len(pts)):
                pts1 = np.float32([pts[i][0], pts[i][1], pts[i][2], pts[i][3]])
                # 좌표의 이동점
                pts2 = np.float32([[0, 0], [0, 150], [150, 0], [150, 150]])
                M = cv2.getPerspectiveTransform(pts1, pts2)
                dst = cv2.warpPerspective(image, M, (150, 150))
                if note == 1:
                    origin.append(dst)
                elif note == 0:
                    contrast.append(dst)
                #cv2.imwrite('/home/parking_lot/all_sec' + '/sec' + str(i + 21) + '/' + str(file[33:48]) + '.jpg', dst)

        print(len(origin))
        print(len(contrast))
    num = list()
    send_image = []
    send_idx = []
    if note == 0 :
        num = compare(origin, contrast)
        send_image = []
        send_idx = []
        for i, val in enumerate(num):
            if val == True:
                origin[i] = contrast[i]
                send_image.append(contrast[i])
                send_idx.append(i)


    note = 0

    print(num)
    print(send_idx)
    print(len(send_image))
    return send_image, send_idx, note ,origin


#section(start_flag, origin)














