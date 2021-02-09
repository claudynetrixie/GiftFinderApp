import requests

headers = {
    'User-Agent': 'Mozilla/5',
    'Referer': 'https://shopee.com.my/search?keyword=lipstick'
}

item = "lipstick"

# sort by keywords: relevancy, sales
sort_by = "sales"

url = 'https://shopee.ph/api/v2/search_items/?by=' + sort_by + '&keyword=' + item + '&limit=10&newest=0&order=desc&page_type=search'  

url = 'https://shopee.ph/api/v2/search_items/?by=relevancy&categoryids=103&limit=10&newest=0&order=desc&page_type=search'


#get image
#https://cf.shopee.ph/file/2a6701992b65b6c87060927a14dec831

r = requests.get(url, headers = headers).json()

# item['price_min'] and ['price_max']
#if same price, price_min = price_max
#if range price, price_min != price_max

for item in r['items']:
    print(item['name'], ' ', float(item['price'])/100000)