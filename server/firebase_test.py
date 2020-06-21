import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime


def firebase_update(num,value):
    #Firebase database 인증 및 앱 초기화
    # cred = credentials.Certificate('capston-design-2020-117e9-6fe0db86d226.json')
    # firebase_admin.initialize_app(cred,{
    #     'databaseURL' : 'https://capston-design-2020-117e9.firebaseio.com'
    # })

    ref = db.reference().child('object/carData') #db 위치 지정
    num = num
    value = value
    names = ['slot','carEmpty','number']

    dic={}
    for i in range(len(num)):
        dic[names[0]+str(num[i])] = { names[1] : bool(value[i]),names[2] : num[i]}

    print(dic)
    ref.update(dic) # d여기에 json 내용

def fire_base_carnum(car_char):
    ref = db.reference().child('object/guestData') #db 위치 지정
    now = datetime.now()
    for car_num in car_char:
        ref.push(
            {
            "carNum":car_num,
            "date":now.strftime('%Y:%m:%d'),
            'time':now.strftime('%H:%M:%S')
            })
        # print(car_num)

def fire_base_illegal(car_count):
    ref = db.reference().child('object/cntIllegal')
    ref.update(
        {
        "value":str(car_count)
        })