import socket
import cv2
import numpy as np
import time

#socket에서 수신한 버퍼를 반환하는 함수
def recvall(sock, count):
    # 바이트 문자열
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf
 
HOST=''
PORT=8010
 
#TCP 사용
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')
 
#서버의 IP, 포트번호 지정
s.bind((HOST,PORT))
print('Socket bind complete')
# 클라이언트의 접속 e대기
s.listen(1)
print('Socket now listening')
 
#연결, conn에는 소켓 객체, addr은 소켓에 바인드 된 주소
conn,addr=s.accept()
path = '/home/parking_lot/vid_sec1/'
fname = '[Sec1]> '+ datetime.today().strftime("%Y-%m-%d-%H%M%S") + ".avi"

fcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X') #DIVX 코덱 적용
out = cv2.VideoWriter(path+fname, fcc, 24, (1920, 1080))

start = time.time()
while True:
    # client에서 받은 stringData의 크기 (==(str(len(stringData))).encode().ljust(16))
    length = recvall(conn, 16)
    stringData = recvall(conn, int(length))
    data = np.fromstring(stringData, dtype = 'uint8')
    
    #data를 디코딩
    frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
    cv2.imshow('Section1',frame)
    if time.time() - start > 10:
        start = time.time()
        fname = '[Sec1]> '+ datetime.today().strftime("%Y-%m-%d-%H%M%S") + ".avi"
        out = cv2.VideoWriter(path+fname, fcc, 24, (1920, 1080))
    out.write(frame)
    k = cv.waitkey(1) & 0xff
    if k == 27:
        break
out.release()
cv2.destroyAllWindows()
