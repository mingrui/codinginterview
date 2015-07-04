# solution 1:
def get_products_of_all_ints_except_at_index(my_list):
    list_length = len(my_list)
    exclude = 0
    product_list = []
    while exclude < list_length:
        product = 1;
    	for index, number in enumerate(my_list):
            if index != exclude:
                product *= number
        product_list.append(product)
        exclude += 1
    
    for number in product_list:
        print number
        
# solution 2:
def efficient_method(my_list):
    product_list = []

    current_product = 1
    product_list.append(current_product)
    for number in my_list[:-1]:
        current_product *= number
        product_list.append(current_product)

    current_product = 1
    reverse_index = len(my_list) - 1
    while reverse_index >= 0:
        product_list[reverse_index] = current_product * product_list[reverse_index]
        current_product *= my_list[reverse_index]
        reverse_index -= 1
        
    for result in product_list:
        print result
        
list_of_int = [3, 1, 2, 0, 6, 4]

#get_products_of_all_ints_except_at_index(list_of_int)
efficient_method(list_of_int)