import cv2
import socket
import numpy as np
 
## TCP 사용
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
## server ip, port
s.connect(('210.115.229.72', 8010))
 
 
# picamera 이미지 capture
cam = cv2.VideoCapture(0)
 
## 이미지 속성 변경 3 = width, 4 = height
cam.set(3, 1920);
cam.set(4, 1080);
 
## 0~100에서 90의 이미지 품질로 설정 (default = 95)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]
 
while True:
    # 1개 프레임씩 읽기
    ret, frame = cam.read()
    
    # cv2. imencode(ext, img [, params])
    # encode_param의 형식으로 frame을 jpg로 이미지를 인코딩한다.
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    # frame을 String 형태로 변환
    data = numpy.array(frame)
    stringData = data.tostring()
 
    #서버에 데이터 전송
    
    s.sendall((str(len(stringData))).encode().ljust(16) + stringData)
 
cam.release()
