print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist is just another name pointing to the same object
mylist = shoplist

# remove one item from shoplist
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)

print('Copy by making a full slice')
# Make a copy by doing a full slice
mylist = shoplist[:]
# remove first item
del mylist[0]

print('shoplist is',shoplist)
print('mylist is', mylist)