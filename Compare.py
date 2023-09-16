from Storage_containers import *

sc10 = ship_containers_10ft()
sc20 = ship_containers_20ft()
sc40 = ship_containers_40ft()
box_truck = boxtruck()


def get_container(item_list):
    # Add up total_volume volume of products to be shipped
    total_volume = 0
    for products in item_list:
        total_volume += products.volume

    total_weight = 0
    for products in item_list:
        total_weight += products.weight

    # Compare total_volume volume of listed products to container options
    if total_volume < sc10.cubic_feet and total_weight < sc10.weight_capacity:
        return "SC10"
    if total_volume < sc20.cubic_feet and total_weight < sc20.weight_capacity:
        return "SC20"
    if total_volume < box_truck.cubic_feet and total_weight < box_truck.weight_capacity:
        return "Box truck"
    if total_volume < sc40.cubic_feet and total_weight < sc40.weight_capacity:
        return "SC40"
    else:
        return "You're gonna need a bigger container..."

