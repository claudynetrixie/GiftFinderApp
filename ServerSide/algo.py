# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 02:03:20 2021

@author: claudyne
"""
import requests



def set_values(option, item_name, category_id):
    url = ""
    headers = {
    'User-Agent': 'Mozilla/5',
    }
    
    #sort by keywords: relevancy, sales, pop (popular)
    sort_by = "relevancy"
    
    #option0: search item from category
    #option1: normal item search
    
    if(option == 0):
        url = 'https://shopee.ph/api/v2/search_items/?by='+ sort_by +'&categoryids=' + category_id + '&limit=10&newest=0&order=desc&page_type=search'    
       
    else:
        item = item_name
        url = 'https://shopee.ph/api/v2/search_items/?by=' + sort_by + '&keyword=' + item + '&limit=10&newest=0&order=desc&page_type=search'  
    
    print(url)
    get_items(url, headers) 
    
    
    
    
    
def get_items(url, headers):
    r = requests.get(url, headers = headers).json()

    # item['price_min'] and ['price_max']
    #if same price, price_min = price_max
    #if range price, price_min != price_max
    
    for item in r['items']:
        print(item['name'], ' ', float(item['price'])/100000)
        
    #get image url
    #https://cf.shopee.ph/file/2a6701992b65b6c87060927a14dec831
    #urllib.request.urlretrieve(image_url, "local-filename.jpg")

        
def start():
    #get input
    #loop
        #set values
        #get items
    #cap to 10 items only
    
    #category
    set_values(0, "", str(13632))
    
    #string item
    # set_values(1, "lipstick", "")
    
    
    
start()





