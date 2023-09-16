import Storage_containers
class check_dimensions:
    product_dimension = []

    def choose_container(product, container):
        
        container_dimension = []
        squared_container_dimension = 0
        squared_product_dimension = 0

        container_dimension.append(container.length)
        container_dimension.append(container.width)
        container_dimension.append(container.height)

        sorted_container_dimension = sort_dimension(container_dimension)
        squared_container_dimension = square_area(sorted_container_dimension)

        for i in range(len(product)):
            product_dimension = []
            product_dimension.append(product[i][0].length)
            product_dimension.append(product[i][0].width)
            product_dimension.append(product[i][0].height)
            sorted_product_dimension = sort_dimension(product_dimension)
            squared_product_dimension += square_area(sorted_product_dimension)

            print("squared product ",squared_product_dimension)
            print("squared container ", squared_container_dimension)
            
        if squared_product_dimension <= squared_container_dimension:
            print("squared_product_dimension ", squared_product_dimension)
            print("squared_container_dimension ", squared_container_dimension)
            squared_container_dimension = squared_container_dimension - squared_product_dimension
                #update the container and take in another product
            #if sorted_product_dimension[0] <= sorted_container_dimension[0] and sorted_product_dimension[1] <= sorted_container_dimension[1] and sorted_product_dimension[2] <= sorted_container_dimension[2]:
            #    return 
            print("final squared container dimension ",squared_container_dimension)
        

    # Sort the dimension in ascending order
def sort_dimension(item_dimension):
    iteration = 0
    for i in range(2):
        if item_dimension[iteration+1] < item_dimension[iteration]:
            temp_dimension = item_dimension[iteration]
            item_dimension[iteration] = item_dimension[iteration+1]
            item_dimension[iteration+1] = temp_dimension
        iteration += 1
    return item_dimension

# Multiplies the width and height of the smallest dimension
def square_area(area_dimension):
    multiplied_dimension = area_dimension[0] * area_dimension[1]
    print("multiple dimensiton ", multiplied_dimension)
    return multiplied_dimension