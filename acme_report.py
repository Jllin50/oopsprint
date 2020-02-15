from random import randint, sample, uniform
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


# Useful to use with random.sample to generate names
def namegen():
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
        x = Product(namegen(), randint(5, 100),
                    randint(5, 100), uniform(0, 2.5))
        products.append(x)
    return products


def inventory_report(products):
    unique = set(products)
    total_weight = 0
    total_price = 0
    total_flammabilty = 0
    for product in products:
        total_weight += product.weight
        total_price += product.price
        total_flammabilty += product.flammability
    avg_weight = total_weight/len(products)
    avg_price = total_price/len(products)
    avg_flammabilty = total_flammabilty/len(products)
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {len(unique)}')
    print(f'Average price: {avg_price}')
    print(f'Average weight: {avg_weight}')
    print(f'Average flammability: {avg_flammabilty}')


if __name__ == '__main__':
    inventory_report(generate_products())
