# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 02:03:20 2021

@author: claudyne
"""
from weights_setting import get_ids
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options



def set_values(option, item_name, category_id, num_items, item_list):
    url = ""
    
    #sort by keywords: relevancy, sales, pop (popular)
    sort_by = "relevancy"
    
    #option0: search item from category
    #option1: normal item search
    
    

    
    if(option == 0):
        url ='https://shopee.ph/search?category=' + category_id + '&page=0&sortBy=' + sort_by
       
    else:
        item = item_name
        url = 'https://shopee.ph/search?category=' + category_id  +'&keyword=' + item + '&page=0&sortBy=' + sort_by
    
    # print(url)
    item_list = get_items(url, item_list, num_items) 
    
    return item_list
    
    
    
    
def get_items(url, item_list, num_items):
    ctr = 0
    print(url)
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    driver = webdriver.Chrome( r'C:\chromedriver_win32\chromedriver.exe', options = chrome_options)
    driver.get(url)
    
    time.sleep(5)
    for i in range(10):
        driver.execute_script("window.scrollBy(0, 350)")
        time.sleep(1)
        
    content=driver.page_source
    soup=BeautifulSoup(content, features="lxml")
    
    # with open("hello.txt", "w", encoding="utf-8") as f:
    #     f.write(content)
        
    all_items = driver.find_elements_by_xpath('//a[@data-sqe="link"]')
    print('len:', len(all_items))

    all_urls = []
    
    for item in all_items:
        if(ctr < num_items):
            url = item.get_attribute('href')
            all_urls.append(url)
            ctr = ctr + 1
            print(url)
            
    ctr = 0

    for item in soup.select('div[data-sqe="item"]'):
        
        if(ctr < num_items):
            print(ctr)
            
            dataImg=item.img
            name=item.find('div',class_="_1Sxpvs")
            price=item.find('div',class_="QmqjGn")
        
            if(dataImg is not None):
                name = name.get_text()
                image_url = dataImg.get('src')
                price = price.get_text()
                url = all_urls[ctr]
                
                
                if(price.find('-') != -1):
                    price = price
                else:
                    p= price.split('₱')
                    price =  "₱" + p[len(p) -1]
                    
                    
                    
                i = {'name': name, 
                      'price': price,
                      'url': url,
                      'image_url': image_url
                      }
                
                item_list.append(i)
                
            ctr = ctr +1 
        else:
            break
        
        
    #get image url
    #https://cf.shopee.ph/file/2a6701992b65b6c87060927a14dec831
    #urllib.request.urlretrieve(image_url, "local-filename.jpg")
        
    return item_list

        
def start():
    t0 = time.time()
    #get input
    #loop
        #set values
        #get items
    #cap to 10 items only
    
    #category
    # set_values(0, "", str(13632))
    
    #string item
    # set_values(1, "lipstick", "")
    
    list_i= ['Male', 'Adult', 'Birthday', 'Books', 'Food']
    id_list, weight_list = get_ids(list_i)
    # print(id_list)
    # print(weight_list)
    
    # id_list = ['13632-Adult']
    # weight_list = [1]
    
    item_list = []
    for item, weight in zip(id_list, weight_list):
        
        str_search = item.split("-")
        
        if(len(str_search) == 1):
            item_list =  set_values(0, "", item, weight, item_list)
        else:
            item_list = set_values(1, str_search[1], str_search[0], weight, item_list)
            
    t1 = time.time()

    total = t1-t0
    print("total time: " + str(total))
    
    return item_list
    
    
item_list = start()
print(item_list)





