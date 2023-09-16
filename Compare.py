from Storage_containers import *

sc10 = ship_containers_10ft()
sc20 = ship_containers_20ft()
sc40 = ship_containers_40ft()
box_truck = boxtruck()


def get_container(item_list):
    # Add up total_volume of products to be shipped
    total_volume = 0
    for products in item_list:
        total_volume += products.volume

    # Add up total_weight of products to be shipped
    total_weight = 0
    for products in item_list:
        total_weight += products.weight

    # Compare total_volume volume of listed products to container options
    if total_volume < sc10.cubic_feet and total_weight < sc10.weight_capacity:
        return "SC10"
    elif total_volume < sc20.cubic_feet and total_weight < sc20.weight_capacity:
        return "SC20"
    elif total_volume < box_truck.cubic_feet and total_weight < box_truck.weight_capacity:
        return "Box truck"
    elif total_volume < sc40.cubic_feet and total_weight < sc40.weight_capacity:
        return "SC40"
    else:
        return "You're gonna need a bigger container..."


def not_full(item_list):
    # Add up total_volume of products to be shipped
    total_volume = 0
    for products in item_list:
        total_volume += products.volume

    container = get_container(item_list)
    if container == "SC10":
        container = ship_containers_10ft()
    elif container == "SC20":
        container = ship_containers_20ft()
    elif container == "SC40":
        container = ship_containers_40ft()
    elif container == "Box truck":
        container = boxtruck()
    else:
        return

    # Determine if there is more than 1/4 space still available
    if total_volume <= float(3 / 4) * container.cubic_feet:
        return True
