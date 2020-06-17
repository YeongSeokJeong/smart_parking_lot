import sys, os
import darknet as dn
import pdb
import cv2
import numpy as np
from skimage import measure
import pickle as pkl
def dark_box(img, pts):
	side_point = pts[0][0], pts[0][1], pts[-1][2], pts[-1][3]
	min_x, min_y = min(side_point[0][1], side_point[1][1]), min(side_point[0][0], side_point[1][0])
	max_x, max_y = max(side_point[2][1],side_point[3][1]), max(side_point[1][0],side_point[2][0])
	cv2.rectangle(img, (min_y, min_x), (max_y, max_x), (0,0,0), -1)
	return img

def make_dark_box(img, pts, side_flag):
	up_side = pts[:side_flag]
	if len(pts)-side_flag == 0:
		dark_box(img, up_side)
	else:
		down_side = [pts[side_flag],pts[-1]]
		img = dark_box(img, up_side)
		img = dark_box(img, down_side)
	return img

def dist(center_0, center_1):
	return np.sqrt((center_0[0]-center_0[0])**2 +  (center_0[0]-center_0[0])**2)

def check_section(file_name,pts,flag_idx, origin_center,origin_box_img,meta,net):
	target_img = cv2.imread(file_name)
	target_img = make_dark_box(target_img, pts, flag_idx)
	cv2.imwrite('./target.jpg', target_img)
	file_name = './target.jpg'
	target_img = cv2.imread(file_name)

	bound_box = dn.detect(net, meta, file_name.encode('utf-8'))
	print('bound_box', bound_box)
	bound_box = np.array(bound_box)
	if len(bound_box) == 0:
		return [], [], 0
	bound_box = bound_box[:,2]
	new_box_img = []
	new_center = [(int(center_x), int(center_y)) for center_x,center_y,width,height in bound_box]
	for box in bound_box:
	    center_x,center_y,width,height = box
	    min_x,min_y = int(center_x - width/2), int(center_y - height/2)
	    max_x, max_y = int(center_x + width/2) , int(center_y+height/2)
	    new_box_img.append(target_img[min_y:max_y, min_x: max_x,::])

	illegal_car_count = 0
	if len(origin_center) == 0:
		return new_center, new_box_img, 0
	else:
		for oc in range(len(origin_center)):
			for nc in range(len(new_center)):
				if dist(origin_center[oc], new_center[nc]) < 5:
					inp = cv2.resize(origin_box_img[oc],dsize = (100,100), interpolation=cv2.INTER_AREA)
					oup = cv2.resize(new_box_img[nc], dsize = (100,100), interpolation=cv2.INTER_AREA)
					s = measure.compare_ssim(inp, oup,  multichannel=True)
					if s > 0.8: 
						illegal_car_count+=1
	return new_center, new_box_img, illegal_car_count
def get_file_list():
    dir_url = '/home/parking_lot/'
    section_list = ['section1']
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
        f_list.append(flist[0])
    return f_list

# net = dn.load_net("yolov3.cfg".encode('utf-8'), 'yolov3.weights'.encode('utf-8'), 0)
# meta = dn.load_meta('coco.data'.encode('utf-8'))

# with open('pts.pkl', 'rb') as fr:
#     pts_list = pkl.load(fr)
# pts_list = pts_list[0]
# f_list = get_file_list()
# sec_center = []
# sec_img =[]
# while True:
#     f_list = get_file_list()[0]
#     print(f_list)
#     sec_center, sec_img, cnt = check_section(f_list, pts_list,
#         sec_center, sec_img, meta, net)
#     print(cnt)