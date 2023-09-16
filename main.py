from product_maker import *
from Compare import *

# Products
oil_filters = create_product("Oil Filters", 4, 4, 4, 50, False)
batteries = create_product("Batteries", 4, 3, 4, 500, True)

# Combine lists of products for delivery
delivery = oil_filters + batteries

# Determine the best container to fit delivery and if there's still 1/4 or more of space available
print(get_container(delivery))
if not_full(delivery):
    print("But, there is still more space to fill.")
