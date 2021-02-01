package com.example.sampleapp;

import androidx.appcompat.app.AppCompatActivity;

import android.animation.Animator;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.animation.DecelerateInterpolator;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toolbar;

import java.util.ArrayList;
import java.util.List;

public class QuestionActivity extends AppCompatActivity {
    private TextView question, noIndicator;
    private LinearLayout optionsContainer;
    private ImageButton nextBtn;
    private int count = 0;
    private List<QuestionModel> list;
    private int position = 0;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_question);
//        Toolbar toolbar = findViewById(R.id.toolbar);
//        setSupportActionBar(toolbar);

        question = findViewById(R.id.question);
        noIndicator = findViewById(R.id.no_indicator);
        optionsContainer = findViewById(R.id.options_container);
        nextBtn = findViewById(R.id.next_btn);

        final List<QuestionModel> list = new ArrayList<>();
        list.add(new QuestionModel("Gift for Him/Her?", "Female", "Male", "Gay", "Lesbian"));
        list.add(new QuestionModel("Age", "Baby", "Kid", "Teen", "Adult"));
        list.add(new QuestionModel("Occassion", "Birthday", "Christmas", "Graduation", "Just Because"));
        list.add(new QuestionModel("Hobbies", "a", "b", "c", "d"));
        list.add(new QuestionModel("Hobbies", "a", "b", "c", "d"));

        for(int i = 0; i < 4; i++){
            optionsContainer.getChildAt(i).setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {

                }
            });
        }


        nextBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                count = 0;
                playAnim(question, 0, list.get(position).getQuestion());

            }
        });
    }

    private void playAnim (final View view, final int value, final String data){
        view.animate().alpha(value).scaleX(value).scaleY(value).setDuration(500).setStartDelay(100)
                .setInterpolator(new DecelerateInterpolator()).setListener(new Animator.AnimatorListener() {
            @Override
            public void onAnimationStart(Animator animator) {
                if(value == 0){
                    String option = "";
                    if(count == 0){
                        option= list.get(position).getOptionA();
                    }
                    else if(count == 1){
                        option= list.get(position).getOptionB();
                    }
                    else if(count == 2){
                        option= list.get(position).getOptionC();
                    }
                    else if (count == 3){
                        option= list.get(position).getOptionD();
                    }

                    playAnim(optionsContainer.getChildAt(count), 1, option);
                    count++;
                }
            }

            @Override
            public void onAnimationEnd(Animator animator) {
                //data change

                if(value == 0 ){
                    ((TextView) view).setText(data);
                    playAnim(view, 1, data);
                }
            }

            @Override
            public void onAnimationCancel(Animator animator) {

            }

            @Override
            public void onAnimationRepeat(Animator animator) {

            }
        });
    }

    private void checkAnswer(){
        
    }
}