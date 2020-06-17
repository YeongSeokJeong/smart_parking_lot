package com.example.Smart_Parking_lot;

public class Car {
    private int number; //자리 번호
    private boolean carEmpty; //자리 사용 여부
    private String time; //자리 시간
    private String fireKey; //각각의 자리에 부여된 고유 키값

    public Car() {
    }

    public Car(int number, boolean carEmpty, String time) {
        this.number = number;
        this.carEmpty = carEmpty;
        this.time = time;
    }

    public Car(int number, boolean carEmpty, String time, String fireKey) {
        this.number = number;
        this.carEmpty = carEmpty;
        this.time = time;
        this.fireKey = fireKey;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public boolean getCarEmpty() {
        return carEmpty;
    }

    public void setCarEmpty(boolean carEmpty) {
        this.carEmpty = carEmpty;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public String getFireKey() {
        return fireKey;
    }

    public void setFireKey(String fireKey) {
        this.fireKey = fireKey;
    }

    @Override
    public String toString() {
        return "Car{" +
                "number=" + number +
                ", carEmpty=" + carEmpty +
                ", time='" + time + '\'' +
                ", fireKey='" + fireKey + '\'' +
                '}';
    }
}
