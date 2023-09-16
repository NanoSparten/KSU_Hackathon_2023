from Storage_containers import *


def get_container(item_list):
    sc10 = ship_containers_10ft().cubic_feet
    sc20 = ship_containers_20ft().cubic_feet
    sc40 = ship_containers_40ft().cubic_feet
    box_truck = boxtruck().cubic_feet

    # Add up total volume of products to be shipped
    total = 0
    for products in item_list:
        total += products.volume

    # Compare total volume of listed products to container options
    if total < sc10:
        return "SC10"
    elif total < sc20:
        return "SC20"
    elif total < box_truck:
        return "Box truck"
    elif total < sc40:
        return "SC40"
    else:
        return "Require multiple containers."
