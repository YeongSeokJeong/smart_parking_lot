package com.example.Smart_Parking_lot;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.example.Smart_Parking_lot.R;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

public class CarAdapter extends ArrayAdapter<Car> {
    public CarAdapter(@NonNull Context context, int resource) {
        super(context, resource);
    }

    @NonNull
    @Override
    public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
        ViewHolder viewHolder;

        if(convertView == null) {
            LayoutInflater inflater = LayoutInflater.from(getContext());
            convertView = inflater.inflate(R.layout.car_item, null);

            viewHolder = new ViewHolder();
            viewHolder.imgDot = (ImageView) convertView.findViewById(R.id.imgDot);
            viewHolder.txtNum = (TextView) convertView.findViewById(R.id.txtNum);
            viewHolder.txtTime = (TextView)convertView.findViewById(R.id.txtTime);

            convertView.setTag(viewHolder);
        }else {
            viewHolder = (ViewHolder)convertView.getTag();
        }

        Car car = getItem(position);
        viewHolder.txtNum.setText(""+car.getNumber());
        viewHolder.txtTime.setText(car.getTime());
        viewHolder.imgDot.setImageResource(car.getCarEmpty() ? R.drawable.dot_g : R.drawable.dot_r);

        return convertView;
    }
    private class ViewHolder{
        TextView txtNum;
        TextView txtTime;
        ImageView imgDot;
    }
}
