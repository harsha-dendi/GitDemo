dict={'colour':'Green'}
dict['colour']= 'yellow'
print(dict)

dict={'colour': 'Green', 'points': 5}
del dict['colour']
print(dict)

dict={}
dict['colour']='yellow'
dict['points'] = 5
print(dict)
print(f"the colour of the dictinary is {dict['colour']}")