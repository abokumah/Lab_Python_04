groceries = ['bananas','strawberries','apples','bread']
print groceries

#1.a
groceries.append('champagne')
print groceries

#1.b
groceries.remove('bread')
print groceries

#1.c
dic_fruits = {'apple':'a', 'banana':'b', 'bread':'b', 'strawberries':'s'}
print dic_fruits['apple']
print dic_fruits['strawberries']

#2.a
#I will use dictionaries. This is because it is easy to search,append and remove the items on stock.

#2.b
dic_prices = {'Apples':'7.3', 'Bananas':'5.5', 'Bread':'1.0', 'Carrots':'10.0', 'Champagne':'20.90', 'Strawberries':'32.6'}
print dic_prices['Apples']

#2.c
dic_prices['Strawberries']='63.43'
print dic_prices['Strawberries']

#2.d
dic_prices['chicken']='6.5'
print dic_prices

#3.a
#I will use list. List is used to store sequence of values and it is also a mutable data structure.

#3.b
in_stock = ['Apples','Bananas','Bread', 'Carrots', 'Champagne', 'Strawberries']
print in_stock

#tuples

#3.c
always_in_stock = ['Apples','Bananas','Bread', 'Carrots', 'Champagne', 'Strawberries']
print always_in_stock

#3.d
print "Come to shoprite! We always sell"
for index in always_in_stock:
    print index
