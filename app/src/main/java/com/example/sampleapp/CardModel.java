package com.example.sampleapp;

import android.os.Parcel;
import android.os.Parcelable;

import java.io.Serializable;

public class CardModel implements Serializable {
    private String name;
    private String price;
    private String url;
    private String image_url;

    public CardModel(String name, String price, String url, String image_url) {
        this.name = name;
        this.price = price;
        this.url = url;
        this.image_url = image_url;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getImage_url() {
        return image_url;
    }

    public void setImage_url(String image_url) {
        this.image_url = image_url;
    }



    //    public CardModel(String image, String title, String desc) {
//        this.image_url = image;
//        this.title = title;
//        this.desc = desc;
//    }
//    public String getImage() {
//        return image_url;
//    }
//    public void setImage(String image) {
//        this.image = image;
//    }
//    public String getTitle() {
//        return title;
//    }
//    public void setTitle(String title) {
//        this.title = title;
//    }
//    public String getDesc() {
//        return desc;
//    }
//
//    public void setDesc(String desc) {
//        this.desc = desc;
//    }
}