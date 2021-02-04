package com.example.sampleapp;

import java.io.Serializable;
import java.util.List;

public class AnswerModel implements Serializable {

    private List<String> ansList;

    public AnswerModel(List<String> ansList) {
        this.ansList = ansList;
    }

    public List<String> getAnsList() {
        return ansList;
    }

    public void setAnsList(List<String> ansList) {
        this.ansList = ansList;
    }

}
