# TODO Add storage containers
def ship_containers_10ft():
    name = 'Shipping Container 10ft'
    length = 10
    height = 9
    width = 8
    cubic_area = length * height * width
    weight_capacity = 14800
    return StorageContainers(name, length, height, width, weight_capacity)


def ship_containers_20ft():
    name = 'Shipping Container 20ft'
    length = 20
    height = 9
    width = 8
    cubic_area = length * height * width
    weight_capacity = 29600
    return StorageContainers(name, length, height, width, weight_capacity)


def ship_containers_40ft():
    name = 'Shipping Container 40ft'
    length = 40
    height = 9
    width = 8
    cubic_area = length * height * width
    weight_capacity = 59200
    return StorageContainers(name, length, height, width, weight_capacity)


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
    return StorageContainers(name, length, height, width, weight_capacity)

class StorageContainers:
    def __init__(self, name, length, height, width, weight_capacity):
        self.name = name
        self.length = length
        self.height = height
        self.width = width
        self.cubic_feet = length * height * width
        self.weight_capacity = weight_capacity


box_truck = StorageContainers('box_truck', 24, 8, 8, 26000)
SC10 = ship_containers_10ft()
SC20 = ship_containers_20ft()
SC40 = ship_containers_40ft()
