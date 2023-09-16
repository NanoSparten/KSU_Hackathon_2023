import array 
import numpy as np

'''
The goal for our plan
is given a cubic area, choose the best container for those shipment
then the algorithm will place the items in the containers that will optimize the space
the output will be in a form for users to load up the items. 

'''
class max_storage:
    a = np.matrix('0 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 ; 1 1 1 1 0 0 0 0 ; 1 1 1 1 0 0 0 0 ; 1 1 1 1 0 0 0 0 ; 1 1 1 1 0 0 0 0')
    print(a)
"""    def item_list(self, item_list):


    # Sort the list of items by cubic area in descending order and return the sorted list
    def sort_items(item_list):
        sorted_items = []
        sort_check = 0
        change_check = False
        item_count = item_list.length 
        iteration = 0
        # Sort this by cubic area
        while change_check == False and iteration == item_count:

            if(sorted_items[iteration] > sort_check):
                temp = sort_check
                sort_check = sorted_items[iteration]
                sorted_items[iteration] = temp
                change_check = True
                iteration += 1 

        return sorted_items
    
    def sort_weight(item_list):
        sorted_items = []
        heavy_item = 0
        item_count = 0
        iteration = 0

        
    # Given the list of items and storage containers, verify you can fit each items into the containers
    def tetris(item_list, storage_containers):
        container = []
        iteration = 0
        storage_count = item_list.size
        length = storage_containers.length
        height = storage_containers.height
        width = storage_containers.width
        current_capacity_length = length
        current_capacity_height = height
        current_capacity_width = width
        while storage_count != 0:
            # add item, subtract each dimension
            if current_capacity_height >= item_list[iteration] and current_capacity_length >= item_list[iteration] and current_capacity_width >= item_list[iteration]:
                container.append(item_list[iteration]) 
"""
