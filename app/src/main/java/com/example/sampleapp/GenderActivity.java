package com.example.sampleapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class GenderActivity extends AppCompatActivity {
    private Button genderFemale;
    private Button genderMale;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_gender);


        genderFemale=findViewById(R.id.choice_one);
        genderFemale.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent genderIntent = new Intent(GenderActivity.this, QuestionActivity.class);
                startActivity(genderIntent);

            }
        });

        genderMale=findViewById(R.id.choice_four);
        genderMale.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent genderIntent = new Intent(GenderActivity.this, QuestionActivity.class);
                startActivity(genderIntent);
            }
        });


    }


}