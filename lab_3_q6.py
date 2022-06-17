def sum_all(my_list):
    return sum(my_list)

def product_all(my_list):
    p = 1
    for i in my_list:
        p *= i
    
    return p

def sum_even_indice(my_list):
    s = 0
    for i in range(0, len(my_list), 2):
        s += my_list[i]
    
    return s

def add_to_list(my_list, values):
    my_list.extend(values)