# smart_parking_lot



## 개요

2020년도 1학기 빅데이터 캡스톤디자인 프로젝트 통합 관리 페이지

## 지도교수 

김유섭 교수님 

## 팀

- 팀명 : 주차의 민족 (주민)
- 팀원 및 역할
  - 정영석 : 불법 주차 판단 딥러닝 모델 제작 및 데이터 수집 & 보고서 작성 
  - 이연희 : 안드로이드 애플리케이션 개발 & 데이터베이스 서버 구축 & 보고서 작성 
  - 노재영 : 영상 전송 서버 데이터베이스 구축 & 웹 페이지 개발 & 회의록 작성 
  - 손주형 : Raspberry pi 기반 카메라 제작 & Spark 기반 빅데이터 전처리 프로그램 개발 & 회의록 작성 
  - 김도경 : 해당 주차 구역 주차 가능 여부 판단 딥러닝 모델 제작 및 데이터 수집 & git 관리

## 기대효과

- 프로젝트 명 : Smart Paking Lot(스마트 주차장)
- 주제 : 통합적 주차 관리를 위한 IoT와 딥러닝 기반의 스마트 주차장 제작

- 기대효과
  - 효율적 주차 관리 가능
  - 간단한 인프라를 사용한 효율적 주차장 관리 가능
  - 공간에 제한이 없는 주차관리 가능

## 시스템 구조도

![시스템 구조도](https://github.com/YeongSeokJeong/smart_parking_lot/blob/master/img/시스템 구조도.png "시스템 구조도")

## 기능

- 자동적 불법 주차차량 감지
- IoT와 딥러닝 기반 주차 여부 확인
- 주차 제한 구역의 주차 차량 확인(번호판 이용)

## 개발환경 

- python
  - Keras
  - YOLO v3
- Android Studio OS 6.0+
- firebase
- Raspberry Pi 3B
- spark

## 디렉토리 구조

```
minutes				회의록 
model				모델 소스코드 
raspberry_pi		 	raspberry_pi 소스코드 
Android Application		안드로이드 어플 소스코드
image_preprocessing		이미지 전처리 소스코드
img 	기타 사진
```

## 보고서

- 프로젝트 신청서
- 중간보고서
- 결과보고서 

## 회의록

- 매주 금요일 11시 교수님 & 팀원 화상회의 
  - [minutes](https://github.com/YeongSeokJeong/smart_parking_lot/tree/master/minutes)

## 사전 지식

- 이 프로젝트를 이해 및 수정하기 위해서는 다음과 같은 이해가 있으면 도움이 될 것입니다
  - 파이썬 & Keras 문법
  - firebase(DB) 기본 사용 방법 및  SQL 문법
  - Raspberry Pi 관련 지식
  - 서버 구축 관련 지식
  - Android Studio OS 관련 지식

    

    

    
