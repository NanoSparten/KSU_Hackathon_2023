class Product:
    def __init__(self, name, length, width, height, weight, hazard):
        self.name = name
        self.length = int(length)/12
        self.width = int(width)/12
        self.height = int(height)/12
        self.weight = int(weight)
        self.hazardous = hazard
        self.volume = int(self.length) * int(self.width) * int(self.height)

    def __str__(self):
        return "\nName: " + self.name + "\nDimensions (L x W x H): " + str(self.length) + "ft x " + str(self.width)\
               + "ft x " + str(self.height) + " ft" + "\nVolume: " + str(self.volume) + " cubic ft" + \
               "\nHazardous: " + str(self.hazardous)


def create_product(name, length, width, height, weight, hazard):
    products = []

    # Prompts to enter product details
    p_name = name
    p_length = length
    p_width = width
    p_height = height
    p_weight = weight
    p_hazardous = hazard
    if p_hazardous == 'y':
        p_hazardous = True
    elif p_hazardous == 'n':
        p_hazardous = False

    # Create product object with product information
    p1 = Product(p_name, p_length, p_width, p_height, p_weight, p_hazardous)

    # Add object to product list
    products.append(p1)

    user_input = input("\nDo you want to add another product? (y/n) ")
    if user_input == 'n':
        active = False

    return products
