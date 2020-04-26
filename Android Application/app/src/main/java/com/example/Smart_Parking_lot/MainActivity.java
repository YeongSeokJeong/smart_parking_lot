package com.example.Smart_Parking_lot;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;
import android.widget.LinearLayout;
import android.widget.Toast;

import com.example.Smart_Parking_lot.R;

public class MainActivity extends AppCompatActivity {
    Intent intent;
    LinearLayout[] ll = new LinearLayout[4];
    /*ImageButton imgbtnAdd;*/

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //imgbtnAdd = (ImageButton)findViewById(R.id.imgbtnAdd);
        ll[0] = (LinearLayout)findViewById(R.id.ll1);
        ll[1] = (LinearLayout)findViewById(R.id.ll2);
        ll[2] = (LinearLayout)findViewById(R.id.ll3);
        ll[3] = (LinearLayout)findViewById(R.id.ll4);

        ll[0].setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                intent = new Intent(getApplicationContext(), ParkingLotActivity.class);
                startActivity(intent);
            }
        });
        ll[1].setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(), "출시예정", Toast.LENGTH_SHORT).show();
            }
        });
        ll[2].setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(), "출시예정", Toast.LENGTH_SHORT).show();
            }
        });
        ll[3].setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(), "출시예정", Toast.LENGTH_SHORT).show();
            }
        });

        /*imgbtnAdd.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(), "출시예정", Toast.LENGTH_SHORT).show();
            }
        });*/
    }
}
