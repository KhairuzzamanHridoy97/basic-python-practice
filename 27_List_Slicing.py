#List_Slicing

amazon_cart = [
'notebooks',
'sunglasses',
'toys',
'grapes'

]
print(amazon_cart[2])









#---------------Exercise ----------------------#

new_list = ['a', 'b', 'c']
print(new_list[1]) #b
print(new_list[-2]) #b
print(new_list[1:3]) #['b','c']
new_list[0] = 'z'
print(new_list) #['z','b','c']

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list) #['z',2,3]
print(bonus) #[1,2,3,5]