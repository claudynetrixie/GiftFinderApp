# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 02:03:20 2021

@author: claudyne
"""
import requests
from weights_setting import get_ids



def set_values(option, item_name, category_id, num_items, item_list):
    url = ""
    headers = {
    'User-Agent': 'Mozilla/5',
    }
    
    #sort by keywords: relevancy, sales, pop (popular)
    sort_by = "pop"
    
    #option0: search item from category
    #option1: normal item search
    
    if(option == 0):
        url = 'https://shopee.ph/api/v2/search_items/?by='+ sort_by +'&categoryids=' + category_id + '&limit=' + str(num_items) +'&newest=0&order=desc&page_type=search'    
       
    else:
        item = item_name
        url = 'https://shopee.ph/api/v2/search_items/?by=' + sort_by  +'&categoryids=' + category_id + '&keyword=' + item + '&limit=' + str(num_items) +'&newest=0&order=desc&page_type=search'  
    
    print(url)
    item_list = get_items(url, headers, item_list) 
    
    return item_list
    
    
    
    
def get_items(url, headers, item_list):
    r = requests.get(url, headers = headers).json()

    # item['price_min'] and ['price_max']
    #if same price, price_min = price_max
    #if range price, price_min != price_max
    
    for item in r['items']:
        #print(item['name'], ' ', float(item['price'])/100000)
        name = item['name']
        price= float(item['price']/100000)
        shopid = str(item['shopid'])
        itemid = str(item['itemid'])
        image = str(item['image'])
        
        url = "https://shopee.ph/Item-i." + shopid + "." + itemid
        image_url = "https://cf.shopee.ph/file/" + image
        
        i = {'name': name, 
             'price': price,
             'url': url,
             'image_url': image_url
             }
        
        item_list.append(i)
        
        
    #get image url
    #https://cf.shopee.ph/file/2a6701992b65b6c87060927a14dec831
    #urllib.request.urlretrieve(image_url, "local-filename.jpg")
        
    return item_list

        
def start():
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
    print(id_list)
    print(weight_list)
    
    item_list = []
    for item, weight in zip(id_list, weight_list):
        
        str_search = item.split("-")
        
        if(len(str_search) == 1):
            item_list =  set_values(0, "", item, weight, item_list)
        else:
            item_list = set_values(1, str_search[1], str_search[0], weight, item_list)
            
        
    return item_list
    
    
item_list = start()
print(item_list)





