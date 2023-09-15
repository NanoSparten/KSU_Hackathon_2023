# Container volumes in cubic ft
box_truck = 1536
SC40 = 2720
SC20 = 1360
SC10 = 660


def get_container(item_list):
    # Add up total volume of products to be shipped
    total = 0
    for products in item_list:
        total += products.volume

    # Compare total volume of listed products to container options
    if total < SC10:
        return "SC10"
    elif total < SC20:
        return "SC20"
    elif total < box_truck:
        return "Box truck"
    elif total < SC40:
        return "SC40"
    else:
        return "No container can fit all this..."
