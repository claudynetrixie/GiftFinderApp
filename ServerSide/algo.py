# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 02:03:20 2021

@author: claudyne
"""
import requests

#Gender: Male, Female, Lesbian, Gay
#Age: Baby, Kid, Teen, Adult
#Occasion: Birthday, Christmas, Graduation, Just Because
#Hobbies: Books, Pets, Toys, Video Games
#Cooking, Food, Fashion, Beauty

#Shopee:

#Male
#Men's Apparel(103), Men's Bags & Accesories(2755), Men's Shoes(123)

#Female
#Women's Apparel(102), Women's Accessories(106), Women's Bags(1713), Women's Shoes(531)

#Unisex
#Makeup and Fragrances(15816), Health and Personal Care(), Home Entertainment()
#Home Appliances(), Home & Living(), Sports and Travel(),
#Toys Games and Collectibles(), Motors(), Digital Goods and Vouchers()
#Pet Care(), Gaming()

#Baby
#Babies and Kids()

#Technology
#Mobile and Gadgets(), Mobile Accesories(), Laptops & Computers()
#Camera()


#Age
#Baby: Babies and Kids()


def set_values(option, item_name, category_id):
    url = ""
    headers = {
    'User-Agent': 'Mozilla/5',
    }
    
    #sort by keywords: relevancy, sales
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
        
def start():
    #get input
    #loop
        #set values
        #get items
    #cap to 10 items only
    
    #category
    set_values(0, "", str(103))
    
    #string item
    set_values(1, "lipstick", "")
    
    
    
start()





