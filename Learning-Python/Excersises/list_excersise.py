# Create a list of amazon cart that has various items
amazon_cart = [
    'Laptop',
    'Chair',
    'Game',
    'toy',
    'patch'
]

# print the first to third items
print(amazon_cart[0:3:1])

# List are mutable, show an example
amazon_cart[0] = 'mario'
print(amazon_cart)

# create a new copy of list with list slicing
# [:] is included to copy the current amazon list to new list
new_list = amazon_cart[:]
new_list[0] = 'bike'
print(new_list)
print(amazon_cart)

# LIST METHOD
basket = [300, 1, 2, 3, 4, 5]
basket.append(200)
basket.sort()
basket.sort(reverse=200)
print(basket)
