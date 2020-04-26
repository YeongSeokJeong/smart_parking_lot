package com.example.Smart_Parking_lot;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import com.example.Smart_Parking_lot.R;
import com.google.firebase.database.ChildEventListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.ArrayList;

public class ParkingLotActivity extends AppCompatActivity {
    ImageView[] imgCars = new ImageView[43];
    FirebaseDatabase database = FirebaseDatabase.getInstance();
    DatabaseReference myRef = database.getReference("test").child("carData");

//    ListView lv;
    ImageView imgMyCar;
    ImageView imgvSI;
    ProgressBar pbar;
    ProgressBar pgbU;
    ProgressBar pgbA;
    TextView txtP;
    TextView txtPtotal;
    TextView txtPU;
    TextView txtPA;
    TextView txtvMyCar;
    TextView txtvST;
    TextView txtvUP;
    TextView txtvAP;
    /*Spinner spinner;*/

    ArrayList<Car> carList = new ArrayList<Car>();
    ArrayList<String> ll = new ArrayList<String>();
    /*ArrayAdapter<String> spadapter;*/
    CarAdapter mAdapter;

    /*Animation mAnim1;
    Animation mAnim2;
    Animation mAnim3;
    Animation mAnim4;*/

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_parking);

        carFindViewById();

        mAdapter = new CarAdapter(this, 0);
//      lv.setAdapter(mAdapter);
        initFirebaseDatabase();

        /*주차자리 지정
        mAnim1 = AnimationUtils.loadAnimation(getApplicationContext(), R.anim.translate);
        mAnim1.setInterpolator(getApplicationContext(), android.R.anim.accelerate_interpolator);
        mAnim2 = AnimationUtils.loadAnimation(getApplicationContext(), R.anim.translate_2);
        mAnim2.setInterpolator(getApplicationContext(), android.R.anim.accelerate_interpolator);
        mAnim3 = AnimationUtils.loadAnimation(getApplicationContext(), R.anim.alpha);
        mAnim3.setInterpolator(getApplicationContext(), android.R.anim.accelerate_interpolator);
        mAnim4 = AnimationUtils.loadAnimation(getApplicationContext(), R.anim.alpha_2);
        mAnim4.setInterpolator(getApplicationContext(), android.R.anim.accelerate_interpolator);*/

        /*ll.add("선택안함");
        for(int i = 1; i <= 43; i++){
            ll.add(""+i);
        }*/

        /*spadapter = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, ll);
        spadapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);*/
        /*spinner.setAdapter(spadapter);*/

        /*차량위치선택 레이아웃 (지금은 안쓰임)*/
        /*spinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                if(position == 0){
                    txtvMyCar.setText("");
                    imgMyCar.startAnimation(mAnim4);
                    txtvMyCar.startAnimation(mAnim4);
                    imgMyCar.setVisibility(View.INVISIBLE);
                    txtvMyCar.setVisibility(View.INVISIBLE);
                }
                else{
                    imgMyCar.setVisibility(View.VISIBLE);
                    txtvMyCar.setVisibility(View.VISIBLE);
                    txtvMyCar.setText("차량 위치 : " + position);
                    imgMyCar.startAnimation(mAnim1);
                    txtvMyCar.startAnimation(mAnim3);
                }
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {
                imgMyCar.setVisibility(View.INVISIBLE);
                txtvMyCar.setVisibility(View.INVISIBLE);
            }
        });
        imgCars[0].setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(), ""+carList.size(), Toast.LENGTH_SHORT).show();
            }
        });*/
    }



    private void initFirebaseDatabase(){
        myRef.addChildEventListener(new ChildEventListener() {
            @Override
            public void onChildAdded(@NonNull DataSnapshot dataSnapshot, @Nullable String s) {
                Car car = dataSnapshot.getValue(Car.class);
                car.setFireKey(dataSnapshot.getKey());

                imgCars[car.getNumber()].setImageResource(car.getCarEmpty() ? R.drawable.car_g : R.drawable.car_r);

                mAdapter.add(car);
//                lv.smoothScrollToPosition(mAdapter.getCount());
                initAdapterToArray();
            }

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

            @Override
            public void onChildMoved(@NonNull DataSnapshot dataSnapshot, @Nullable String s) {

            }

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

        pgbU.setMax(max);
        pgbU.setProgress(used);
        txtvUP.setText(String.format("%.2f", (100.0 * used / max)) + "%");

        pgbA.setMax(max);
        pgbA.setProgress(empty);
        txtvAP.setText(String.format("%.2f", (100.0 * empty / max)) + "%");

        txtPtotal.setText(""+max);
        txtPU.setText(""+used);
        txtPA.setText(""+empty);
    }

    private void carFindViewById(){
//      lv = (ListView)findViewById(R.id.lv);

        /*imgMyCar = (ImageView)findViewById(R.id.imgvMyCar);*/
        imgvSI = (ImageView)findViewById(R.id.imgvSI);

        pbar = (ProgressBar)findViewById(R.id.pbar);
        /*pgbA = (ProgressBar)findViewById(R.id.pgbA);
        pgbU = (ProgressBar)findViewById(R.id.pgbU);*/

        txtP = (TextView)findViewById(R.id.txtP);
        txtPtotal = (TextView)findViewById(R.id.txtPtotal);
        txtPU = (TextView)findViewById(R.id.txtPU);
        txtPA = (TextView)findViewById(R.id.txtPA);
        /*txtvMyCar = (TextView)findViewById(R.id.txtvMyCar);*/
        txtvST = (TextView)findViewById(R.id.txtvST);
        /*txtvAP = (TextView)findViewById(R.id.txtvAP);
        txtvUP = (TextView)findViewById(R.id.txtvUP);*/

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
        imgCars[32] = (ImageView)findViewById(R.id.imgCar32);
        imgCars[33] = (ImageView)findViewById(R.id.imgCar33);
        imgCars[34] = (ImageView)findViewById(R.id.imgCar34);
        imgCars[35] = (ImageView)findViewById(R.id.imgCar35);
        imgCars[36] = (ImageView)findViewById(R.id.imgCar36);
        imgCars[37] = (ImageView)findViewById(R.id.imgCar37);
        imgCars[38] = (ImageView)findViewById(R.id.imgCar38);
        imgCars[39] = (ImageView)findViewById(R.id.imgCar39);

        imgCars[40] = (ImageView)findViewById(R.id.imgCar40);
        imgCars[41] = (ImageView)findViewById(R.id.imgCar41);
        imgCars[42] = (ImageView)findViewById(R.id.imgCar42);

        /*차량위치선택시 보여지는 목록 위젯*/
        /*spinner = (Spinner)findViewById(R.id.spinner);*/
    }
}
