package com.example.Smart_Parking_lot;

public class Car {
    private int number;
    private boolean carEmpty;
    private String time;
    private String fireKey;

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
