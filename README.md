# GiftFinderApp
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/claudynetrixie/GiftFinderApp">
    <img src="app/src/main/Logo.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">GiftFinder</h3>

  <p align="center">
    Find Gifts for Special Occasions
    <br />
    <a href="https://github.com/claudynetrixie/GiftFinderApp"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#setup">Setup</a>
    </li>
    <li>
      <a href="#screenshots">Screenshots</a>
    </li>
   
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
GiftFinder aims to help users find gifts for their friends and loved ones for special occasions. GiftFinder is composed of an Android application written in Java and a serverless platform for processing and computation using Amazon Web Services (i.e. AWS API Gateway, Lambda).  The Android application serves as the front-end for users who would like to find customized gifts. On the other hand, web scraping in e-commerce sites is performed in the serverless platform using Selenium and BeautifulSoup to look for gifts suitable to the gift receiver.

### Built With
* Java
* XML
* Retrofit
* OkHttp
* Python
* Selenium
* BeautifulSoup
* Amazon Web Services (AWS)
  *  AWS Lambda for computation and processing
  *  AWS API Gateway for API handling



## Setup

First, clone the repo:

`git clone https://github.com/claudynetrixie/GiftFinderApp`

On Android Studio: 
* Open Android Studio and select `File->Open...` or from the Android Launcher select `Import project (Eclipse ADT, Gradle, etc.)` and navigate to the root directory of your project.
* Select the directory  and select the file `build.gradle` in the cloned repo.
* Click 'OK' to open the the project in Android Studio.
* A Gradle sync should start, but you can force a sync and build the 'app' module as needed.


Running the Sample App:
You can either connect an Android device to your development machine or use the Android Emulator.
* Select `Run -> Run 'app'` (or `Debug 'app'`) from the menu bar
* Select the device you wish to run the app on and click 'OK'


## Screenshots

### Homepage and Quiz:
<p float = "left">
<img src="app/src/main/Screenshots/HomePage.png" width="130" align = "center">
<img src="app/src/main/Screenshots/1.png" width="130" align = "center">
<img src="app/src/main/Screenshots/2.png" width="130" align = "center">
<img src="app/src/main/Screenshots/3.png" width="130" align = "center">
<img src="app/src/main/Screenshots/4.png" width="130" align = "center">
<img src="app/src/main/Screenshots/5.png" width="130" align = "center">
</p>

### Results (Gift Recommendations):
<p float = "left">
<img src="app/src/main/Screenshots/R1.png" width="150" align = "center">
<img src="app/src/main/Screenshots/R2.png" width="150" align = "center">
<img src="app/src/main/Screenshots/R3.png" width="150" align = "center">
<img src="app/src/main/Screenshots/R4.png" width="150" align = "center">
<img src="app/src/main/Screenshots/R5.png" width="150" align = "center">
</p>

<p float = "left">
<img src="app/src/main/Screenshots/R6.png" width="150" align = "center">
<img src="app/src/main/Screenshots/R7.png" width="150" align = "center">
<img src="app/src/main/Screenshots/R8.png" width="150" align = "center">
<img src="app/src/main/Screenshots/R9.png" width="150" align = "center">
<img src="app/src/main/Screenshots/R10.png" width="150" align = "center">
</p>
