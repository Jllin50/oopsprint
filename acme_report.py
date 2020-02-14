#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
def namegen():   
    ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
    name = sample(ADJECTIVES, 1) + sample(NOUNS, 1)
    # initialize an empty string 
    str1 = ""  
    # traverse in the string   
    str1 += name[0] + " " + name[1]
    # return string   
    return str1  

def generate_products(num_products=30):
    products = []
    for i in range(num_products):
        x = Product(namegen(),randint(5, 100), randint(5, 100), uniform(0, 2.5))
        products.append(x)
    return products
    
ACME CORPORATION OFFICIAL INVENTORY REPORT
Unique product names: 19
Average price: 56.8
Average weight: 54.166666666666664
Average flammability: 1.258097155966675

def inventory_report(products):
    unique = set(products)
    len(unique) = 
    for product in products:
        unique = set([ 'one', 'two', 'two']) 



if __name__ == '__main__':
    inventory_report(generate_products())
