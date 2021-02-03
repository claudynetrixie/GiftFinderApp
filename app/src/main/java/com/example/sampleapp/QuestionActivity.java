package com.example.sampleapp;

import androidx.annotation.NonNull;
import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.animation.Animator;
import android.annotation.SuppressLint;
import android.content.Intent;
import android.content.res.ColorStateList;
import android.graphics.Color;
import android.nfc.Tag;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.animation.DecelerateInterpolator;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.Toolbar;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;

public class QuestionActivity extends AppCompatActivity {

    FirebaseDatabase database = FirebaseDatabase.getInstance();
    DatabaseReference myRef = database.getReference();

    private TextView question, noIndicator;
    private LinearLayout optionsContainer;
    private ImageButton nextBtn;
    private int count = 0;
    private List<QuestionModel> list = new ArrayList<>();
    private int position = 0;

    private static final String TAG = "MyAppTag";



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

//        final List<QuestionModel> list = new ArrayList<>();
        list = new ArrayList<>();
//        list.add(new QuestionModel("Gift for Him/Her?", "Female", "Male", "Gay", "Lesbian"));
//        list.add(new QuestionModel("Age", "Baby", "Kid", "Teen", "Adult"));
//        list.add(new QuestionModel("Occassion", "Birthday", "Christmas", "Graduation", "Just Because"));
//        list.add(new QuestionModel("Hobbies", "a", "b", "c", "d"));
//        list.add(new QuestionModel("Hobbies", "a", "b", "c", "d"));


        myRef.child("Questions").addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                for (DataSnapshot snapshot: dataSnapshot.getChildren()){
                    Log.d(TAG, "IN");
                    list.add(snapshot.getValue(QuestionModel.class));
                    QuestionModel value = snapshot.getValue(QuestionModel.class);
                    Log.d(TAG, "Value is: " + value.getQuestion());
                }

                if(list.size() > 0){
                    for(int i = 0; i < 4; i++){
                        optionsContainer.getChildAt(i).setOnClickListener(new View.OnClickListener() {
                            @RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
                            @Override
                            public void onClick(View v) {
                                checkAnswer((Button)v);
                            }
                        });
                    }

                    playAnim(question, 0, list.get(position).getQuestion());

                    nextBtn.setOnClickListener(new View.OnClickListener() {
                        @RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
                        @Override
                        public void onClick(View v) {
                            nextBtn.setEnabled(false);
                            nextBtn.setAlpha(0.7f);
                            enableOption(true);
                            position++;
                            if(position == list.size()){
                                //score activity
                                return;
                            }
                            count = 0;
                            playAnim(question, 0, list.get(position).getQuestion());

                        }
                    });

                }
                else{
                    finish();
                    Toast.makeText(QuestionActivity.this, "no questions left", Toast.LENGTH_SHORT);
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                Toast.makeText(QuestionActivity.this, error.getMessage(), Toast.LENGTH_SHORT);
            }
        });



    }

    private void playAnim (final View view, final int value, final String data){
        view.animate().alpha(value).scaleX(value).scaleY(value).setDuration(500).setStartDelay(100)
                .setInterpolator(new DecelerateInterpolator()).setListener(new Animator.AnimatorListener() {
            @Override
            public void onAnimationStart(Animator animator) {
                if(value == 0 && count<4){
                    String option = "";
                    Log.d(TAG, String.valueOf(value));

                    Log.d(TAG, "Play Anim");

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

                    playAnim(optionsContainer.getChildAt(count), 0, option);
                    count++;
                }
            }

            @Override
            public void onAnimationEnd(Animator animator) {
                //data change

                if(value == 0 ){
                    try{
                        ((TextView) view).setText(data);
                        noIndicator.setText(position+1 + "/" + list.size());

                    }catch(ClassCastException ex){
                        ((Button) view).setText(data);
                    }
//                    ((TextView) view).setText(data);
                    view.setTag(data);
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

    @RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
    private void checkAnswer(Button selectedOption){
        nextBtn.setEnabled(true);
        nextBtn.setAlpha(1);
        selectedOption.setBackgroundTintList(ColorStateList.valueOf(Color.parseColor("#a83232")));
//        if(selectedOption.getText().toString().equals(list.get(position).getOptionA())){
//            selectedOption.setBackgroundTintList(ColorStateList.valueOf(Color.parseColor("#a83232")));
//        }
//        else{
//
//        }

    }

    @RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
    private void enableOption(boolean enable){
        for (int i=0; i<4; i++){
            optionsContainer.getChildAt(i).setEnabled(enable);
            String val = "";
            if(enable){
                switch(i){
                    case 0: val = "#FFAC8A";
                        break;
                    case 1: val = "#FB9C5C";
                        break;
                    case 2: val = "#F97924";
                        break;
                    case 3: val = "#F96124";
                        break;
                }
                Log.d(TAG, "color change is" + val);
                optionsContainer.getChildAt(i).setBackgroundTintList(ColorStateList.valueOf(Color.parseColor(val)));

            }
        }
    }


}
