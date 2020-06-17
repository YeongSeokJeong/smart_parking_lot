# -*-coding: utf-8-*-

import cv2
import os
import numpy as np
# import matplotlib.pyplot as plt
from os import rename
from cv2_compare import *

def section(start_flag, origin):

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
            pts = [[(423,43),(345,265),(577,37),(527,259)],[(577,37),(527,259),(729,31),(699,253)],
                   [(177,575),(1,999),(385,577),(241,1007)],[(385,577),(241,1007),(593,573),(491,1009)],
                   [(593,573),(491,1009),(805,571),(754,1007)],[(805,571),(754,1007),(1019,567),(1009,1009)],
                   [(1019,567),(1009,1009),(1239,561),(1283,1015)],[(1239,561),(1283,1015),(1465,557),(1571,1021)],
                   [(1465,557),(1571,1021),(1713,555),(1869,1025)]]
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

            pts = [[(503, 19), (491, 187), (917, 27), (925, 195)],
                   [(917, 27), (925, 195), (1325, 35), (1349, 199)], [(1325, 35), (1349, 199), (1717, 39), (1761, 203)],
                   [(171, 481), (19, 965), (401, 489), (293, 975)], [(401, 489), (293, 975), (625, 493), (559, 969)],
                   [(625, 493), (559, 969), (841, 493), (827, 969)], [(841, 493), (827, 969), (1055, 497), (1086, 972)],
                   [(1055, 497), (1086, 972), (1269, 499), (1348, 974)],
                   [(1269, 499), (1348, 974), (1483, 501), (1611, 980)],
                   [(1483, 501), (1611, 980), (1701, 507), (1864, 980)]]
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
            pts = [[(71, 1), (35, 151), (479, 5), (467, 161)], [(479, 5), (467, 161), (891, 7), (861, 173)]]
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
            pts = [[(213, 29), (147, 179), (535, 39), (493, 175)],
                   [(535, 39), (493, 175), (933, 21), (903, 173)], [(933, 21), (903, 173), (1335, 19), (1345, 163)],
                   [(1335, 19), (1345, 163), (1765, 11), (1797, 155)], [(169, 487), (3, 935), (397, 503), (257, 939)],
                   [(397, 503), (257, 939), (611, 501), (513, 947)],
                   [(611, 501), (513, 947), (827, 503), (769, 949)], [(827, 503), (769, 949), (1033, 503), (1035, 955)],
                   [(1033, 503), (1035, 955), (1261, 503), (1305, 963)],
                   [(1261, 503), (1305, 963), (1493, 501), (1585, 967)],
                   [(1493, 501), (1585, 967), (1735, 499), (1855, 977)]]
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














