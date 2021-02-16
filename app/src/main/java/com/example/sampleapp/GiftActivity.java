package com.example.sampleapp;

import androidx.appcompat.app.AppCompatActivity;
import androidx.viewpager.widget.ViewPager;


import android.animation.ArgbEvaluator;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
//import android.widget.Adapter;

import com.bumptech.glide.Glide;

import java.util.ArrayList;
import java.util.List;

public class GiftActivity extends AppCompatActivity {

    ViewPager viewPager;
    Adapter adapter;
    List<CardModel> models;
    Integer[] colors = null;
    ArgbEvaluator argbEvaluator = new ArgbEvaluator();
    ArrayList<String> links;
    private List<CardModel> posts;
    private static final String TAG = "GiftActivity";


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_gift);


        Intent i = getIntent();
        posts= (List<CardModel>) i.getSerializableExtra("LIST");
        links = new ArrayList<String>();
        models = new ArrayList<>();

        Log.d(TAG, "INSIDE GIFT ACTIVITY PLS WORK");
        for (CardModel post : posts) {
            String content = "";
//            content += "Name: " + post.getName() + "\n";
//            content += "Price: " + post.getPrice() + "\n";
//            content += "Title: " + post.getUrl() + "\n";
            content += "Image_url: " + post.getImage_url() + "\n\n";
            Log.d(TAG, content);
//            links.add(post.getImage_url());
            models.add(new CardModel(post.getName() , post.getPrice() , post.getUrl(), post.getImage_url()));

        }


        //for url images
//        ImageView imageView = (ImageView) findViewById(R.id.gift1);
//        Glide.with(this).load("https://cf.shopee.ph/file/2a6701992b65b6c87060927a14dec831").into(imageView);

//        links = new ArrayList<String>();
//        links.add("https://scontent.fmnl25-2.fna.fbcdn.net/v/t1.0-9/217889_4178767380881_596859379_n.jpg?_nc_cat=104&ccb=3&_nc_sid=de6eea&_nc_ohc=nZ2_AR7oc2oAX8HZHyX&_nc_ht=scontent.fmnl25-2.fna&oh=1fa49c61b19a3162c4c0e0805031eb4e&oe=604C1668");
//        links.add("https://scontent.fmnl25-1.fna.fbcdn.net/v/t31.0-8/20626324_10155615935122363_7612048478096185863_o.jpg?_nc_cat=108&ccb=3&_nc_sid=8bfeb9&_nc_ohc=GUxxqQEGKL4AX8XtXSv&_nc_ht=scontent.fmnl25-1.fna&oh=f339a6dc9c21ef4adc95e65d9f7c5f4d&oe=604DBB00");
//        links.add("https://scontent.fmnl25-1.fna.fbcdn.net/v/t31.0-8/15418300_10210329941738323_7485999566434432500_o.jpg?_nc_cat=100&ccb=3&_nc_sid=a9b1d2&_nc_ohc=DHbOj4u00R8AX-wscQr&_nc_ht=scontent.fmnl25-1.fna&oh=927b124d52e7bca2bb10c7de296d6a06&oe=604CEEA1");
//        links.add("https://media-exp1.licdn.com/dms/image/C5603AQFIVn5r3eIc_w/profile-displayphoto-shrink_200_200/0/1612900009134?e=1618444800&v=beta&t=fQW1TswWr9vBS7Xs3veObvBbnpBoNQH8TRut8ZTAZO8");



//        models = new ArrayList<>();
//        models.add(new CardModel("Brochure", "Brochure is an informative paper document (often also used for advertising) that can be folded into a template", "", links.get(0)));
//        models.add(new CardModel( "Sticker", "Sticker is a type of label: a piece of printed paper, plastic, vinyl, or other material with pressure sensitive adhesive on one side", "", links.get(1)));
//        models.add(new CardModel("Poster", "Poster is any piece of printed paper designed to be attached to a wall or vertical surface.", "", links.get(2)));
//        models.add(new CardModel( "Namecard", "Business cards are cards bearing business information about a company or individual.", "", links.get(3)));

        adapter = new Adapter(models, this);
        viewPager = findViewById(R.id.viewPager);
        viewPager.setAdapter(adapter);
        viewPager.setPadding(130, 0, 130, 0);
        Integer[] colors_temp = {
                getResources().getColor(R.color.color1),
                getResources().getColor(R.color.color2),
                getResources().getColor(R.color.color3),
                getResources().getColor(R.color.color4)
        };
        colors = colors_temp;

        viewPager.setOnPageChangeListener(new ViewPager.OnPageChangeListener() {
            @Override
            public void onPageScrolled(int position, float positionOffset, int positionOffsetPixels) {
                if (position < (adapter.getCount() -1) && position < (colors.length - 1)) {
                    viewPager.setBackgroundColor(
                            (Integer) argbEvaluator.evaluate(
                                    positionOffset,
                                    colors[position],
                                    colors[position + 1]
                            )
                    );
                }
                else {
                    viewPager.setBackgroundColor(colors[colors.length - 1]);
                }
            }

            @Override
            public void onPageSelected(int position) {
            }
            @Override
            public void onPageScrollStateChanged(int state) {
            }


            });




        }
}