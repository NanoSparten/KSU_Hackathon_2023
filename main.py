from product_maker import *
from Compare import *

# User inputs all products needed for delivery
delivery = create_product()

# Determine the best container to fit delivery
print(get_container(delivery))


