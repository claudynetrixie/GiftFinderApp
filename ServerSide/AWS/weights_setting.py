# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 21:51:55 2021

@author: claudyne
"""

output_gifts =10

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

def get_hobbies(hobby1, hobby2, id_list, list_i):
    
#Food: 
#Beauty: 15816
        
    if(hobby1 == "Books" or hobby2 == "Books"):
        id_list.append("13632" + "-" + list_i[1])
        
    if(hobby1 == "Pets" or hobby2 == "Pets"):
        id_list.append("21292")
        
    if(hobby1 == "Toys" or hobby2 == "Toys"):
        
        if(list_i[1] == "Baby"):
            id_list.append("115" + "-" + list_i[1])
    
        elif(list_i[1] == "Kid"):
            id_list.append("17309")
            id_list.append("17328")
            
            if(list_i[0] == "Female"):
                id_list.append("17320")

    if(hobby1 == "Video Games" or hobby2 == "Video Games"):
        id_list.append("20718")
        
    if(hobby1 == "Cooking" or hobby2 == "Cooking"):
        id_list.append("15509")
        
    elif(hobby1 == "Food" or hobby2 == "Food"):
        id_list.append("363")
        id_list.append("21509")
                      
    elif(hobby1 == "Beauty" or hobby2 == "Beauty"):
        id_list.append("15816")
        
    return id_list


    

# def get_unisex():
    

def assign_weights(id_list):  
    #get len of id_list
    #assign weight
    weight_list = []
    
    length= len(id_list)
    
    weight= round((1/length)*output_gifts)
    
    for item in id_list:
        weight_list.append(weight)
        
    if(sum(weight_list) != output_gifts):
        diff = output_gifts - sum(weight_list)        
        ctr = 0
        
        if diff > 0:
            while diff != 0:
                weight_list[ctr] += 1
                ctr = ctr + 1
                diff = diff - 1
        else:
            diff = -diff
            while diff != 0:
                weight_list[ctr] -= 1
                ctr = ctr + 1
                diff = diff - 1
            
        
        
    return weight_list
        
    
    

def get_male(list_i):
    id_list = []
    
    if(list_i[1] =="Baby"):
        id_list.append("113-boy")
        
    elif(list_i[1] == "Kid"):
        id_list.append("113-boy")
    
    elif (list_i[1] == "Teen"):
        id_list.append("103-teen")
        id_list.append("2755")
        id_list.append("123")
    else:
        id_list.append("103")
        id_list.append("123")
        id_list.append("2755")
            
            
    return id_list



def get_female(list_i):
    id_list = []
    
    if(list_i[1] =="Baby"):
        id_list.append("113-girl")
        
    elif(list_i[1] == "Kid"):
        id_list.append("113-girl")
    
    elif (list_i[1] == "Teen"):
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
    
    

def get_ids(list_i):
    if(list_i[0] == "Male"):
        id_list = get_male(list_i)
    elif(list_i[0] == "Female"):
        id_list = get_female(list_i)
        
    id_list = get_hobbies(list_i[3], list_i[4], id_list, list_i)
    weight_list = assign_weights(id_list)
    
    return id_list, weight_list
        
        

# list_i= ['Male', 'Adult', 'Birthday', 'Food', 'Video Games']
# print(list_i)
# id_list, weight_list = get_ids(list_i)
# print(id_list)
# print(weight_list)
