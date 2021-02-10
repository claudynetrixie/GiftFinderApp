# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 21:51:55 2021

@author: claudyne
"""

#Gender: Male, Female, Lesbian, Gay 
#Age: Baby, Kid, Teen, Adult 
#Occasion: Birthday, Christmas, Graduation, Just Because 
#Hobbies: Books, Pets, Toys, Video Games 
#Cooking, Food, Fashion, Beauty

#Male
#Male-Baby: 113(boy)
#Male-Kid: 113(boy)
#Male-Teen: 103(Teen), 2755, 123
#Male-Adult: 103, 2755, 123

#Female
#Female-Baby: 113(girl),
#Female-Kid: 113(girl),
#Female-Teen: 102(teen), 106, 1713, 531
#Female-Adult: 102, 106, 1713, 531


#Books: 13632 (include kid, teen, adult, baby keyword)
#Pets: 21292 
#Toys: 115 (head category), 
    #Babies: search babies
    #Kids:17309, 17328
    #Female-Kid: 17320
#VideoGames: 24456, 109, 18596, 20718
#Cooking: 15528 (small), 19814(large appliances), 
#Food: 363, 21509
#Beauty: 15816


#Shopee:

#Male
#Men's Apparel(103), Men's Bags & Accesories(2755), Men's Shoes(123)

#Female
#Women's Apparel(102), Women's Accessories(106), Women's Bags(1713), Women's Shoes(531)

#Unisex
#Makeup and Fragrances(15816), Health and Personal Care(107), Home Entertainment(18529)
#Home Appliances(15509), Home & Living(112), Sports and Travel(1029),
#Toys Games and Collectibles(115), Motors(15769), Digital Goods and Vouchers(15580)
#Pet Care(13612), Gaming(20718)

#Baby
#Babies and Kids(113)

#Technology
#Mobile and Gadgets(24456), Mobile Accesories(109), Laptops & Computers(18596)
#Camera(18560)



##############

# def hobbies(hobby1, hobby2, id_list):
    
    


# def get_unisex():
    

def get_male(list):
    id_list = []
    
    if(list[1] =="Baby"):
        id_list.append("113-boy")
        
    elif(list[1] == "Kid"):
        id_list.append("113-boy")
    
    elif (list[1] == "Teen"):
        id_list.append("103-teen")
        id_list.append("2755")
        id_list.append("123")
    else:
        id_list.append("103")
        id_list.append("123")
        id_list.append("2755")
            
    return id_list



def get_female(list):
    id_list = []
    
    if(list[1] =="Baby"):
        id_list.append("113-girl")
        
    elif(list[1] == "Kid"):
        id_list.append("113-girl")
    
    elif (list[1] == "Teen"):
        id_list.append("102-teen")
        id_list.append("106")
        id_list.append("1713")
        id_list.append("531")
    else:
        id_list.append("102")
        id_list.append("106")
        id_list.append("1713")
        id_list.append("531")
            
    return id_list
    
    

def get_ids(list):
    if(list[0] == "Male"):
        ids = get_male(list)
    elif(list[0] == "Female"):
        ids = get_female(list)
        
    return ids
        
        

list= ['Female', 'Baby', 'Birthday', 'Books', 'Food']
id_list = get_ids(list)
print(id_list)
