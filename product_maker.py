class Product:
    def __init__(self, name, length, width, height, weight, hazard):
        self.name = name
        self.length = int(length)
        self.width = int(width)
        self.height = int(height)
        self.weight = int(weight)
        self.hazardous = hazard
        self.volume = int(self.length) * int(self.width) * int(self.height)

    def __str__(self):
        return "\nName: " + self.name + "\nDimensions (L x W x H): " + str(self.length) + "ft x " + str(self.width) \
               + "ft x " + str(self.height) + " ft" + "\nVolume: " + str(self.volume) + " cubic ft" + \
               "\nHazardous: " + str(self.hazardous)


# Method for users to manually input product information
def create_product():
    products = []
    active = True

    print("Enter product details:")
    while active:
        # Prompts to enter product details
        p_name = input("Name: ")
        p_length = input("Length (ft): ")
        p_width = input("Width (ft): ")
        p_height = input("Height (ft): ")
        p_weight = input("Weight (lbs): ")
        p_hazardous = input("Hazardous? (y/n): ")
        if p_hazardous == 'y':
            p_hazardous = True
        elif p_hazardous == 'n':
            p_hazardous = False
        p_quantity = input("Quantity: ")

        # Create product object and add object to product list
        for number in range(int(p_quantity)):
            p1 = Product(p_name, p_length, p_width, p_height, p_weight, p_hazardous)
            products.append(p1)

        # Ask user to add more product or not
        user_input = input("Do you want to add another product? (y/n): ")
        if user_input == 'n':
            break

    return products


# Overloaded method for product creation
def create_product(name, length, width, height, weight, hazard):
    products = []
    p_quantity = input("Quantity for " + name + ": ")

    # Create product object and add object to product list
    for number in range(int(p_quantity)):
        p1 = Product(name, length, width, height, weight, hazard)
        products.append(p1)

    return products
