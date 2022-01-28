#List Method

basket = ['a','b','c','d','e' ]
dasket = ['a','b','c','d','e','a','a','c' ]

print(basket.index('b',0,4))
print(basket.index('c',0,4))

print('d' in basket) 
print('f' in basket)  #false

print(basket.count('a'))

print(dasket.count('a')) #3
print(dasket.count('b')) #1
print(dasket.count('c')) #2

basket.insert(0,'gaga')
print(basket)


#-------------------------------- Exercise ----------------------#

# using this list, 
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# 1. Remove the Banana from the list
basket.remove('Banana')
# 2. Remove "Blueberries" from the list.
basket.pop('Blueberries')
# 3. Put "Kiwi" at the end of the list.
basket.append('Kiwi')
# 4. Add "Apples" at the beginning of the list
basket.insert(0,'Apples')
# 5. Count how many apples in the basket
basket.count('Apples')
# 6. empty the basket
basket.clear()
print(basket)




#Solution:
#1 - basket.remove('Banana')
#2 - basket.pop()
#3 - basket.append('Kiwi')
#4 - basket.insert(0, 'Apples')
#5 - basket.count('Apples')
#6 - basket.clear()






























