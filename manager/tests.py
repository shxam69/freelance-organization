from django.test import TestCase

# Create your tests here.

mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 2000,

}

mydict['color'] = 'red'

# update
mydict.update({'color': 'white'})

# pop
# mydict.pop('year')
# print(mydict)

# popitem
# mydict.popitem()
# print(mydict)

# clear
# mydict.clear()
# print(mydict.keys())
# print(mydict.values())
