package com.example.Smart_Parking_lot;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.TextView;

import com.google.firebase.database.ChildEventListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.ArrayList;

public class ParkingLotActivity extends AppCompatActivity {
    ImageView[] imgCars = new ImageView[43];

    // 데이터를 읽고 쓰기 위한 DatabaseReference의 인스턴스
    FirebaseDatabase database = FirebaseDatabase.getInstance();
    DatabaseReference myRef = database.getReference("test").child("carData");

    // ListView lv;
    ImageView imgvSI;
    ProgressBar pbar;
    TextView txtP;

    TextView txtPtotal; //전체 자리
    TextView txtPU;     //사용중
    TextView txtPA;     //사용가능
    TextView txtvST;    //스마일 상태

    /*TextView txtvUP;    //원형 progress bar
    TextView txtvAP;*/


    ArrayList<Car> carList = new ArrayList<Car>(); //데이터를 담을 자료구조
    ArrayList<String> ll = new ArrayList<String>();
    ArrayAdapter<String> spadapter;
    CarAdapter mAdapter; // 데이터를 연결할 어댑터


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_parking_lot);

        carFindViewById();

        mAdapter = new CarAdapter(this, 0); //데이터를 받기 위한 데이터어댑터 객체 선언
        initFirebaseDatabase();
    }



    private void initFirebaseDatabase(){
        //하위 이벤트를 수신 대기
        myRef.addChildEventListener(new ChildEventListener() { // DB의 값이 변경될때 마다 값을 읽어오도록 함

            //데이터가 추가되었을때
            @Override
            public void onChildAdded(@NonNull DataSnapshot dataSnapshot, @Nullable String s) { //onChildAdded 항목 목록을 검색하거나 항목 목록에 대한 추가를 수신 대기함
                Car car = dataSnapshot.getValue(Car.class);
                car.setFireKey(dataSnapshot.getKey());

                imgCars[car.getNumber()].setImageResource(car.getCarEmpty() ? R.drawable.car_g : R.drawable.car_r); //setImageResource로 자리가 차있는경우와 아닌 경우 이미지 적용

                mAdapter.add(car);
                initAdapterToArray();
            }

            // 데이터가 변화되었을때
            @Override
            public void onChildChanged(@NonNull DataSnapshot dataSnapshot, @Nullable String s) {
                String firebaseKey = dataSnapshot.getKey();
                int count = mAdapter.getCount();
                for(int i = 0; i < count; i++){
                    if(mAdapter.getItem(i).getFireKey().equals(firebaseKey)){
                        mAdapter.remove(mAdapter.getItem(i));
                        onChildAdded(dataSnapshot, s);
                        break;
                    }
                }
                initAdapterToArray();
            }


            // 데이터가 제거되었을때, dataSnapshot에는 삭제된 하위 항목의 데이터가 포함됨
            @Override
            public void onChildRemoved(@NonNull DataSnapshot dataSnapshot) {
                String firebaseKey = dataSnapshot.getKey();
                int count = mAdapter.getCount();
                for (int i = 0; i < count; i++) {
                    if (mAdapter.getItem(i).getFireKey().equals(firebaseKey)) {
                        mAdapter.remove(mAdapter.getItem(i));
                        break;
                    }
                }
                initAdapterToArray();
            }
            // 데이터가 파이어베이스 DB 리스트 위치 변경되었을때
            @Override
            public void onChildMoved(@NonNull DataSnapshot dataSnapshot, @Nullable String s) {

            }

            //DB 처리 중 오류가 발생했을때
            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });
    }

    private void initAdapterToArray(){
        carList.clear();

        int count = mAdapter.getCount();
        for(int i = 0; i < count; i++){
            carList.add(mAdapter.getItem(i));
        }
        parkingInfo();
    }

    private void parkingInfo(){
        int max = carList.size();
        int used = 0;
        int empty = 0;

        for(int i = 0; i < max; i++){
            if(carList.get(i).getCarEmpty()){
                empty++;
            }
        }
        used = max - empty;

        pbar.setMax(max);
        pbar.setProgress(used);
        txtP.setText(String.format("%.2f", (100.0 * used / max)) + "%");

        imgvSI.setImageResource( (((double)used / max) < (1.0/3.0)) ? R.drawable.level1 : (((double)used / max) < (2.0/3.0)) ? R.drawable.level2 : R.drawable.level3 );
        txtvST.setText( (((double)used / max) < (1.0/3.0)) ? "여유" : (((double)used / max) < (2.0/3.0)) ? "보통" : "혼잡" );

        txtPtotal.setText(""+max);
        txtPU.setText(""+used);
        txtPA.setText(""+empty);
    }

    private void carFindViewById(){

        imgvSI = (ImageView)findViewById(R.id.imgvSI);

        pbar = (ProgressBar)findViewById(R.id.pbar);
        txtP = (TextView)findViewById(R.id.txtP);

        txtPtotal = (TextView)findViewById(R.id.txtPtotal);
        txtPU = (TextView)findViewById(R.id.txtPU);
        txtPA = (TextView)findViewById(R.id.txtPA);
        txtvST = (TextView)findViewById(R.id.txtvST);

        imgCars[0] = (ImageView)findViewById(R.id.imgCar0);
        imgCars[1] = (ImageView)findViewById(R.id.imgCar1);
        imgCars[2] = (ImageView)findViewById(R.id.imgCar2);
        imgCars[3] = (ImageView)findViewById(R.id.imgCar3);
        imgCars[4] = (ImageView)findViewById(R.id.imgCar4);
        imgCars[5] = (ImageView)findViewById(R.id.imgCar5);
        imgCars[6] = (ImageView)findViewById(R.id.imgCar6);
        imgCars[7] = (ImageView)findViewById(R.id.imgCar7);
        imgCars[8] = (ImageView)findViewById(R.id.imgCar8);
        imgCars[9] = (ImageView)findViewById(R.id.imgCar9);

        imgCars[10] = (ImageView)findViewById(R.id.imgCar10);
        imgCars[11] = (ImageView)findViewById(R.id.imgCar11);
        imgCars[12] = (ImageView)findViewById(R.id.imgCar12);
        imgCars[13] = (ImageView)findViewById(R.id.imgCar13);
        imgCars[14] = (ImageView)findViewById(R.id.imgCar14);
        imgCars[15] = (ImageView)findViewById(R.id.imgCar15);
        imgCars[16] = (ImageView)findViewById(R.id.imgCar16);
        imgCars[17] = (ImageView)findViewById(R.id.imgCar17);
        imgCars[18] = (ImageView)findViewById(R.id.imgCar18);
        imgCars[19] = (ImageView)findViewById(R.id.imgCar19);

        imgCars[20] = (ImageView)findViewById(R.id.imgCar20);
        imgCars[21] = (ImageView)findViewById(R.id.imgCar21);
        imgCars[22] = (ImageView)findViewById(R.id.imgCar22);
        imgCars[23] = (ImageView)findViewById(R.id.imgCar23);
        imgCars[24] = (ImageView)findViewById(R.id.imgCar24);
        imgCars[25] = (ImageView)findViewById(R.id.imgCar25);
        imgCars[26] = (ImageView)findViewById(R.id.imgCar26);
        imgCars[27] = (ImageView)findViewById(R.id.imgCar27);
        imgCars[28] = (ImageView)findViewById(R.id.imgCar28);
        imgCars[29] = (ImageView)findViewById(R.id.imgCar29);

        imgCars[30] = (ImageView)findViewById(R.id.imgCar30);
        imgCars[31] = (ImageView)findViewById(R.id.imgCar31);



    }
}
