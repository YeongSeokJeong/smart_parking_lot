## 서버 코드 정리

- sec1_server.py : section1에서 촬영된 것을 서버에 전송 

- sec2_server.py : section2에서 촬영된 것을 서버에 전송 

- sec3_server.py : section3에서 촬영된 것을 서버에 전송 

- sec4_server.py : section4에서 촬영된 것을 서버에 전송

- car_model.hdf5 : CNN 기반 주차구역별 주차 여부 판단 모델

- car_model.json : 모델 json 파일 

- car_model.py : 전체적으로 실행시켜주는 코드

- cv2_compare.py : 추출된 주차구역의 직전 프레임과 현제 프레임의 유사도 비교

- pts.pkl : 주차구역 좌표 

- section.py : 각 주차구역 추출 코드 

- firebase_test.py : 주차구역별 주차여부 결과 값 서버에 전송 

- yolo.py : YOLO3 모델 

- darknet.py : daknet에서 제공해주는 소스코드

- car_num_server.py : 불법주차 차량번호 서버로 전송

- car_number_preprocessing.py : 차 번호판 번호 추출 코드

- send_to_firebase.py : 불법주차 관련 결과 값서버에 전송

  