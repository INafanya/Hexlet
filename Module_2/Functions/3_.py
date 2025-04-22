inventory = {}


def update_inventory(inventory_dict, name, quant):
    if inventory_dict.get(name):
        inventory_dict[name] += quant
    else:
        inventory_dict[name] = quant


def get_stock(inventory_dict, name):
    return inventory_dict.get(name, 0)


update_inventory(inventory, "apple", 10)
print(get_stock(inventory, "apple"))  # => 10
update_inventory(inventory, "banana", 5)
print(get_stock(inventory, "banana"))  # => 5
update_inventory(inventory, "banana", 2)
print(get_stock(inventory, "banana"))  # => 7
print(get_stock(inventory, "cherry"))
