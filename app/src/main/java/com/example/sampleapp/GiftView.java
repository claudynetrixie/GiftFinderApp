package com.example.sampleapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ImageView;

import com.bumptech.glide.Glide;

public class GiftView extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_gift_view);

        ImageView imageView = (ImageView) findViewById(R.id.gift1);

        Glide.with(this).load("https://cf.shopee.ph/file/2a6701992b65b6c87060927a14dec831").into(imageView);
    }
}