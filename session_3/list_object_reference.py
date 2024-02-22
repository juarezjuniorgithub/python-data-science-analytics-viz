print('Simple Assignment')
shop_list = ['apple', 'mango', 'carrot', 'banana']

# my_list is just another name pointing to the same object!
my_list = shop_list

# I purchased the first item, so I remove it from the list
del shop_list[0]
print('shop_list is', shop_list)
print('my_list is', my_list)

# Notice that both shop_list and my_list both print
# the same list without the 'apple' confirming that
# they point to the same object
print('Copy by making a full slice')

# Make a copy by doing a full slice
my_list = shop_list[:]

# Remove first item
del my_list[0]

# Notice that now the two lists are different
print('shop_list is', shop_list)
print('my_list is', my_list)
