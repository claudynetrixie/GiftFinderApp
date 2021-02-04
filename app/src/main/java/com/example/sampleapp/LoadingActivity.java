package com.example.sampleapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.TextView;

import java.util.Iterator;
import java.util.Set;

public class LoadingActivity extends AppCompatActivity {
    private static final String TAG = "LoadingActivity";
    private Integer size = 0;

    Animation textAnim;
    TextView waitingPage;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_loading);
        size = getIntent().getIntExtra("size", 0);
        Log.d(TAG, "size" + size);

        Integer i;
        for (i = 0; i < size; i++){
            Log.d(TAG, "GOT from " + String.valueOf(i) + ": " +
                    String.valueOf(getIntent().getStringExtra(Integer.toString(i))) );

        }

        textAnim = AnimationUtils.loadAnimation(this, R.anim.top_animation);

        waitingPage = findViewById(R.id.loading_text);

        waitingPage.setAnimation(textAnim);

    }
}