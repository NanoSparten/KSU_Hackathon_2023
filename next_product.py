from product_maker import *

products = create_product()


# Get next product with user specified weight
def get_weight(user_input):
    products.sort(key=lambda x: x.weight)
    for product in products:
        if product.weight <= int(user_input):
            return product.weight


# Get next product with user specified length
def get_length(user_input):
    products.sort(key=lambda x: x.length)
    for product in products:
        if product.length <= int(user_input):
            return product.length


# Get next product with user specified width
def get_width(user_input):
    products.sort(key=lambda x: x.width)
    for product in products:
        if product.width <= int(user_input):
            return product.width


# Get next product with user specified height
def get_height(user_input):
    products.sort(key=lambda x: x.height)
    for product in products:
        if product.height <= int(user_input):
            return product.height
