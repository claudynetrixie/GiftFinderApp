package com.example.sampleapp;

import androidx.appcompat.app.AppCompatActivity;
import androidx.viewpager.widget.ViewPager;

import android.animation.ArgbEvaluator;
import android.os.Bundle;
import android.widget.Adapter;
import android.widget.ImageView;

import com.bumptech.glide.Glide;

public class GiftActivity extends AppCompatActivity {

    ViewPager viewPager;
    Adapter adapter;
    List<Model> models;
    Integer[] colors = null;
    ArgbEvaluator argbEvaluator = new ArgbEvaluator();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_gift_activity);

        ImageView imageView = (ImageView) findViewById(R.id.gift1);

        Glide.with(this).load("https://cf.shopee.ph/file/2a6701992b65b6c87060927a14dec831").into(imageView);
    }
}