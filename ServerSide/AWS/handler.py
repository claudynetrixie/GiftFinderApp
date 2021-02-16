import json


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
	
    r = [{'name': 'Korean Iconic Socks Famous Paintings Art Gallery (no tags)', 'price': '₱34', 'url': 'https://shopee.ph/Korean-Iconic-Socks-Famous-Paintings-Art-Gallery-(no-tags)-i.51806616.920705037', 'image_url': 'https://cf.shopee.ph/file/2a6701992b65b6c87060927a14dec831_tn'}, {'name': 'Men Breathable Hole Rubber Shoes', 'price': '₱149', 'url': 'https://shopee.ph/Men-Breathable-Hole-Rubber-Shoes-i.74265370.5818410388', 'image_url': 'https://cf.shopee.ph/file/35df6854e49cff62ed381b2a13d0471c_tn'}, {'name': 'Mumu #7040 Korean Fashion Canvas Sling Shoulder Cross Bag Mens Chest Cross Body Unisex BagFree Gift', 'price': '₱49', 'url': 'https://shopee.ph/Mumu-7040-Korean-Fashion-Canvas-Sling-Shoulder-Cross-Bag-Mens-Chest-Cross-Body-Unisex-Bag-i.19100527.5848477810', 'image_url': 'https://cf.shopee.ph/file/bdfaf260efddab2593a6372d3829b179_tn'}, {'name': 'Mumu Unisex Chest Bag Cross Body Men Ladies Bags Women #7021Free Gift', 'price': '₱67 - ₱74', 'url': 'https://shopee.ph/Mumu-Unisex-Chest-Bag-Cross-Body-Men-Ladies-Bags-Women-7021-i.19100527.3512094961', 'image_url': 'https://cf.shopee.ph/file/a6ff66c41d5f1c93827261c06f8aea36_tn'}, {'name': 'The Encyclopedia of Kitchen Tools (Hardcover) by Elinor Hutton', 'price': '₱1,680', 'url': 'https://shopee.ph/The-Encyclopedia-of-Kitchen-Tools-(Hardcover)-by-Elinor-Hutton-i.157956840.5761810971', 'image_url': 'https://cf.shopee.ph/file/50f293c8de6c63890e9af30f4819bf7f_tn'}, {'name': 'PATRICIA CORNWELL : Scarpetta (Kay Scarpetta #16) [Hardbound/Hardcover]', 'price': '₱298', 'url': 'https://shopee.ph/PATRICIA-CORNWELL-Scarpetta-(Kay-Scarpetta-16)-Hardbound-Hardcover--i.153169057.7557051894', 'image_url': 'https://cf.shopee.ph/file/14731f5121c058ef5769f31dffba8cf6_tn'}, {'name': 'Polland Hopia Bundle of 4', 'price': '₱250', 'url': 'https://shopee.ph/Polland-Hopia-Bundle-of-4-i.30334567.709475287', 'image_url': 'https://cf.shopee.ph/file/ba91ead412ca8cb355c4c2e01c96ed38_tn'}, {'name': 'Cadbury Dairy Milk 165gwholesale', 'price': '₱112', 'url': 'https://shopee.ph/Cadbury-Dairy-Milk-165g-i.71172083.4426204291', 'image_url': 'https://cf.shopee.ph/file/9b2b1817cdbe8d77fe2f24d0925e2fa2_tn'}, {'name': 'GrabFood P150 eGift (Digital GC)', 'price': '₱150', 'url': 'https://shopee.ph/GrabFood-P150-eGift-(Digital-GC)-i.1594791.2054683936', 'image_url': 'https://cf.shopee.ph/file/87944b763b83b2d93bc44cde04bb9939_tn'}, {'name': "McDonald's Regular Coke McFloat (SMS eVoucher)", 'price': '₱32', 'url': "https://shopee.ph/McDonald's-Regular-Coke-McFloat-(SMS-eVoucher)-i.58249676.2392452887", 'image_url': 'https://cf.shopee.ph/file/344089779105e828445f01a122c1eaf0_tn'}]
    

    return r

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
