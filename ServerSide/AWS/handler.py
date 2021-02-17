import json
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from weights_setting import get_ids

# Python 3.7
# selenium==3.14.0
# headless-chromium v1.0.0-55
# chromedriver 2.43

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
    
    
    print(os.listdir('/opt'))
    # # 
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.binary_location = f"/opt/headless-chromium"
    driver = webdriver.Chrome(
        executable_path = f"/opt/chromedriver",
        chrome_options=chrome_options
    )
    
    
    
    
    driver.get(url)
    
    time.sleep(5)
    for i in range(10):
        driver.execute_script("window.scrollBy(0, 350)")
        time.sleep(1)
        
    content=driver.page_source
    soup=BeautifulSoup(content, features="html.parser")
    
  
        
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
        
   
    return item_list




def hello(event, context):
   
    list_i= ['Male', 'Adult', 'Birthday', 'Books', 'Food']
    id_list, weight_list = get_ids(list_i)
  
    item_list = []
    for item, weight in zip(id_list, weight_list):
        
        str_search = item.split("-")
        
        if(len(str_search) == 1):
            item_list =  set_values(0, "", item, weight, item_list)
        else:
            item_list = set_values(1, str_search[1], str_search[0], weight, item_list)
            
    
  
	
    # r = [{'name': 'Korean Iconic Socks Famous Paintings Art Gallery (no tags)', 'price': '₱34', 'url': 'https://shopee.ph/Korean-Iconic-Socks-Famous-Paintings-Art-Gallery-(no-tags)-i.51806616.920705037', 'image_url': 'https://cf.shopee.ph/file/2a6701992b65b6c87060927a14dec831_tn'}, {'name': 'Men Breathable Hole Rubber Shoes', 'price': '₱149', 'url': 'https://shopee.ph/Men-Breathable-Hole-Rubber-Shoes-i.74265370.5818410388', 'image_url': 'https://cf.shopee.ph/file/35df6854e49cff62ed381b2a13d0471c_tn'}, {'name': 'Mumu #7040 Korean Fashion Canvas Sling Shoulder Cross Bag Mens Chest Cross Body Unisex BagFree Gift', 'price': '₱49', 'url': 'https://shopee.ph/Mumu-7040-Korean-Fashion-Canvas-Sling-Shoulder-Cross-Bag-Mens-Chest-Cross-Body-Unisex-Bag-i.19100527.5848477810', 'image_url': 'https://cf.shopee.ph/file/bdfaf260efddab2593a6372d3829b179_tn'}, {'name': 'Mumu Unisex Chest Bag Cross Body Men Ladies Bags Women #7021Free Gift', 'price': '₱67 - ₱74', 'url': 'https://shopee.ph/Mumu-Unisex-Chest-Bag-Cross-Body-Men-Ladies-Bags-Women-7021-i.19100527.3512094961', 'image_url': 'https://cf.shopee.ph/file/a6ff66c41d5f1c93827261c06f8aea36_tn'}, {'name': 'The Encyclopedia of Kitchen Tools (Hardcover) by Elinor Hutton', 'price': '₱1,680', 'url': 'https://shopee.ph/The-Encyclopedia-of-Kitchen-Tools-(Hardcover)-by-Elinor-Hutton-i.157956840.5761810971', 'image_url': 'https://cf.shopee.ph/file/50f293c8de6c63890e9af30f4819bf7f_tn'}, {'name': 'PATRICIA CORNWELL : Scarpetta (Kay Scarpetta #16) [Hardbound/Hardcover]', 'price': '₱298', 'url': 'https://shopee.ph/PATRICIA-CORNWELL-Scarpetta-(Kay-Scarpetta-16)-Hardbound-Hardcover--i.153169057.7557051894', 'image_url': 'https://cf.shopee.ph/file/14731f5121c058ef5769f31dffba8cf6_tn'}, {'name': 'Polland Hopia Bundle of 4', 'price': '₱250', 'url': 'https://shopee.ph/Polland-Hopia-Bundle-of-4-i.30334567.709475287', 'image_url': 'https://cf.shopee.ph/file/ba91ead412ca8cb355c4c2e01c96ed38_tn'}, {'name': 'Cadbury Dairy Milk 165gwholesale', 'price': '₱112', 'url': 'https://shopee.ph/Cadbury-Dairy-Milk-165g-i.71172083.4426204291', 'image_url': 'https://cf.shopee.ph/file/9b2b1817cdbe8d77fe2f24d0925e2fa2_tn'}, {'name': 'GrabFood P150 eGift (Digital GC)', 'price': '₱150', 'url': 'https://shopee.ph/GrabFood-P150-eGift-(Digital-GC)-i.1594791.2054683936', 'image_url': 'https://cf.shopee.ph/file/87944b763b83b2d93bc44cde04bb9939_tn'}, {'name': "McDonald's Regular Coke McFloat (SMS eVoucher)", 'price': '₱32', 'url': "https://shopee.ph/McDonald's-Regular-Coke-McFloat-(SMS-eVoucher)-i.58249676.2392452887", 'image_url': 'https://cf.shopee.ph/file/344089779105e828445f01a122c1eaf0_tn'}]
    

    return item_list

    