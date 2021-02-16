

##################################################################################
#method1
#import requests
#hl
# headers = {
#     'User-Agent': 'Mozilla/5',
#     'Referer': 'https://shopee.com.my/search?keyword=lipstick'
# }

# item = "lipstick"

# # sort by keywords: relevancy, sales
# sort_by = "sales"

# url = 'https://shopee.ph/api/v2/search_items/?by=' + sort_by + '&keyword=' + item + '&limit=10&newest=0&order=desc&page_type=search'  

# url = 'https://shopee.ph/api/v2/search_items/?by=relevancy&categoryids=103&limit=10&newest=0&order=desc&page_type=search'


# #get image
# #https://cf.shopee.ph/file/2a6701992b65b6c87060927a14dec831

# r = requests.get(url, headers = headers).json()

# # item['price_min'] and ['price_max']
# #if same price, price_min = price_max
# #if range price, price_min != price_max

# for item in r['items']:
#     print(item['name'], ' ', float(item['price'])/100000)


# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('start-maximized')
# options.add_argument('disable-infobars')
# options.add_argument('--disable-extensions')
# browserdriver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\\chromedriver_win32\\chromedriver.exe')
# browserdriver.get('https://shopee.com.my/search?keyword=h370m')
# WebDriverWait(browserdriver, 20).until(EC.element_to_be_clickable(("//*[@class="_1NoI8_ _2gr36I"]", "//div[@class='shopee-modal__container']//button[text()='English']"))).click()
# print([my_element.get_attribute('innerHTML') for my_element in WebDriverWait(browserdriver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="_1NoI8_ _2gr36I"]')))])
# print("Program Ended")

# # browserdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# # y = browserdriver.find_element_by_class_name("_39-Tsj")
# # content = browserdriver.find_element_by_tag_name('img')
# h= browserdriver.page_source
# print(browserdriver.page_source)

##################################################################################
#method2

# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urlencode

# keyword = 'Korean Iconic Socks Famous Painting'
# q = str(urlencode({'q': 'shopee ' + keyword}))

# url = 'https://www.google.com/search?q=shopee+' + q + '&tbm=isch'

# # page = open('tower.html', 'r').read()
# page = requests.get(url).text

# soup = BeautifulSoup(page, 'html.parser')

# raw_img = soup.find_all('img')[1]
# link = raw_img.get('src')
# print(link)


# for raw_img in soup.find_all('img'):
#   link = raw_img.get('src')
#   if link:
#     print(link)


##################################################################################
#method3

# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.chrome.options import Options


# products=[]
# prices=[]
# images=[]

# chrome_options = Options()
# #chrome_options.add_argument("--disable-extensions")
# #chrome_options.add_argument("--disable-gpu")
# #chrome_options.add_argument("--no-sandbox") # linux only
# chrome_options.add_argument("--headless")
# # chrome_options.headless = True # also works

# driver = webdriver.Chrome( r'C:\chromedriver_win32\chromedriver.exe', options = chrome_options)
# # driver.get('https://shopee.ph/search?keyword=korean+iconic+socks') #work
# driver.get('https://shopee.ph/search?category=103&page=0&sortBy=relevancy')
# # driver.get('https://shopee.ph/Korean-Iconic-Socks-Famous-Paintings-Art-Gallery-(no-tags)-i.51806616.920705037')

# sleep(5)
# cn = '_1T9dHf' #work
# cn1 = '_1Sxpvs'
# imgs = driver.find_elements_by_class_name(cn)

# # subject = driver.findElement(By.xpath("//div[@class = 'b-datalist__item__subj']")).getText()


# for img in imgs:
#     img_url = img.get_attribute("src")
#     if img_url:
#         print(img_url)



##################################################################################
#method 4


import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
   

products=[]
prices=[]
images=[]

chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works

driver = webdriver.Chrome( r'C:\chromedriver_win32\chromedriver.exe', options = chrome_options)
driver.get('https://shopee.ph/search?category=103&page=0&sortBy=relevancy')

time.sleep(5)
for i in range(10):
    driver.execute_script("window.scrollBy(0, 350)")
    time.sleep(1)
    
content=driver.page_source
soup=BeautifulSoup(content, features="lxml")

for item in soup.select('div[data-sqe="item"]'):
    dataImg=item.img
    name=item.find('div',class_="_1Sxpvs")
    price=item.find('div',class_="QmqjGn")
    
    if(dataImg is not None):
        name = name.get_text()
        img = dataImg.get('src')
        price = price.get_text()
        
        if(price.find('-') != -1):
            price = price
        else:
            p= price.split('₱')
            price =  "₱" + p[len(p) -1]
            
        
        
        # print(name)
        # print(price)
        # print(img)
        products.append(name)
        prices.append(price)
        images.append(img)
    
  

df=pd.DataFrame({'Product Name':products,'Price':prices,'Images': images})
df 

driver.quit()


