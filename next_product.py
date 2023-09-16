# Get next product with user specified weight
def get_weight(user_list, user_input):
    user_list.sort(key=lambda x: x.weight)
    for product in user_list:
        if product.weight <= int(user_input):
            return product.weight


# Get next product with user specified length
def get_length(user_list, user_input):
    user_list.sort(key=lambda x: x.length)
    for product in user_list:
        if product.length <= int(user_input):
            return product.length


# Get next product with user specified width
def get_width(user_list, user_input):
    user_list.sort(key=lambda x: x.width)
    for product in user_list:
        if product.width <= int(user_input):
            return product.width


# Get next product with user specified height
def get_height(user_list, user_input):
    user_list.sort(key=lambda x: x.height)
    for product in user_list:
        if product.height <= int(user_input):
            return product.height
