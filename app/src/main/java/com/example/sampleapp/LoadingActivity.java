package com.example.sampleapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.util.Log;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.TextView;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

import okhttp3.OkHttpClient;
import okhttp3.logging.HttpLoggingInterceptor;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class LoadingActivity extends AppCompatActivity {
    private static final String TAG = "LoadingActivity";
    private Integer size = 0;
    private String api_url = "https://04qr4ecovh.execute-api.ap-southeast-1.amazonaws.com/dev/";

    private List<CardModel> posts;
    private  List<String> ansList = new ArrayList<String>();

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
            ansList.add(String.valueOf(getIntent().getStringExtra(Integer.toString(i))) );
        }

        textAnim = AnimationUtils.loadAnimation(this, R.anim.top_animation);
        waitingPage = findViewById(R.id.loading_text);
        waitingPage.setAnimation(textAnim);


        //rest functionality
        HttpLoggingInterceptor interceptor = new HttpLoggingInterceptor();
        interceptor.setLevel(HttpLoggingInterceptor.Level.BODY);
        //OkHttpClient client = new OkHttpClient.Builder().addInterceptor(interceptor).build();
        final OkHttpClient client = new OkHttpClient.Builder()
                .addInterceptor(interceptor)
                .connectTimeout(60, TimeUnit.SECONDS)
                .writeTimeout(60, TimeUnit.SECONDS)
                .readTimeout(60, TimeUnit.SECONDS)
                .build();



        Retrofit retrofit = new Retrofit.Builder()
//                .baseUrl("https://jsonplaceholder.typicode.com/")
                .baseUrl(api_url)
                .addConverterFactory(GsonConverterFactory.create())
                .client(client)
                .build();
        JsonPlaceHolderApi jsonPlaceHolderApi = retrofit.create(JsonPlaceHolderApi.class);
//        Call<List<Post>> call = jsonPlaceHolderApi.getPosts();
//        getPosts(call);
        Call<List<CardModel>> call = jsonPlaceHolderApi.getGifts(ansList);
        getGifts(call);

    }


    private void getGifts(Call<List<CardModel>> call){

        Log.d(TAG, "inside getPosts");
        call.enqueue(new Callback<List<CardModel>>() {
            @Override
            public void onResponse(Call<List<CardModel>> call, Response<List<CardModel>> response) {
                if (!response.isSuccessful()) {
//                    textViewResult.setText("Code: " + response.code());
                    Log.d(TAG, "FAILURE parsing");
                    return;
                }

                List <CardModel> gifts= response.body();

                for (CardModel gift : gifts) {
                    String content = "";
                    content += "Name: " + gift.getName() + "\n";
                    content += "Price: " + gift.getPrice() + "\n";
                    content += "Title: " + gift.getUrl() + "\n";
                    content += "Text: " + gift.getImage_url() + "\n\n";
                    Log.d(TAG, content);
                }

                final Intent loadingIntent = new Intent(LoadingActivity.this, GiftActivity.class);
                loadingIntent.putExtra("LIST", (Serializable) gifts);


                final Handler handler = new Handler(Looper.getMainLooper());
                handler.postDelayed(new Runnable() {
                    @Override
                    public void run() {
                        //Do something after 100ms
                        startActivity(loadingIntent);
                    }
                }, 1000);

            }
            @Override
            public void onFailure(Call<List<CardModel>> call, Throwable t) {
//                textViewResult.setText(t.getMessage());
                Log.d(TAG, "FAILURE: " + t.getMessage());
            }
        });

    }

    private void getPosts(Call<List<Post>> call){
        Log.d(TAG, "inside getPosts");
        call.enqueue(new Callback<List<Post>>() {
            @Override
            public void onResponse(Call<List<Post>> call, Response<List<Post>> response) {
                if (!response.isSuccessful()) {
//                    textViewResult.setText("Code: " + response.code());
                    return;
                }
                List<Post> posts = response.body();
                for (Post post : posts) {
                    String content = "";
                    content += "ID: " + post.getId() + "\n";
                    content += "User ID: " + post.getUserId() + "\n";
                    content += "Title: " + post.getTitle() + "\n";
                    content += "Text: " + post.getText() + "\n\n";
                    Log.d(TAG, content);
//                    textViewResultewResult.append(content);
                }
            }
            @Override
            public void onFailure(Call<List<Post>> call, Throwable t) {
//                textViewResult.setText(t.getMessage());
                Log.d(TAG, "FAILURE");
            }
        });

    }

}