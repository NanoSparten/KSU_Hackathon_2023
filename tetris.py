from Storage_containers import *
from product_maker import *

oil_filters = create_product("Oil Filter", 4, 4, 4, 100, False)
battery = create_product("Battery", 5, 5, 5, 200, True)

container = ship_containers_40ft()

con_length = container.length
con_width = container.width
con_height = container.height
con_cubic_area = container.cubic_feet

filter_num = len(oil_filters)
battery_num = len(battery)

box_fill_width = con_width / oil_filters[0].width
box_fill_height = con_height / oil_filters[0].height
box_fill_length = int(con_length / oil_filters[0].length)

boxes_per_length = box_fill_width * int(box_fill_height)
print(str(filter_num) + " Oil Filter boxes")
print("Each length will have " + str(boxes_per_length) + " boxes.")
print("Total Oil Filter / Num of Boxes = " + str(filter_num / boxes_per_length))

total_boxes = box_fill_width * int(box_fill_height) * box_fill_length
remaining = total_boxes - filter_num
print(remaining)
