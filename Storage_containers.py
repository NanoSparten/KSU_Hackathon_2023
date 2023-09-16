# TODO Add storage containers
class Storage_containers:
    def __init__ (self, name, length, height, width, weight_capacity):
        self.name = name
        self.length = length
        self.height = height
        self.width = width
        self.cubic_feet = length * height * width
        self.weight_capacity = weight_capacity

    def __init__ (self, name, length, height, width):
        self.name = name
        self.length = length
        self.height = height
        self.width = width
        self.cubit_feet = length * height * width


    def ship_containers_10ft():
        name = 'Shipping Container 10ft'
        length = 10
        height = 9
        width = 8
        cubic_area = length * height * width
        weight_capacity = 14800
        Storage_containers

    def ship_containers_20ft():
        name = 'Shipping Container 20ft'
        length = 20
        height = 9
        width = 8
        cubic_area = length * height * width
        weight_capacity = 29600
    
    def ship_containers_40ft():
        name = 'Shipping Container 40ft'
        length = 40
        height = 9
        width = 8
        cubic_area = length * height * width
        weight_capacity = 59200
    
    def storage_unit():
        name = 'Storage Unit'
        length = 20
        height = 8
        width = 10
        cubic_area = length * height * width
    
    def pallets():
        name = 'Pallets'
        length = 4
        height = 5
        width = 3
        cubic_area = length * height * width
        weight_capacity = 4600


box_truck = Storage_containers('box_truck', 24, 8, 8, 26000)