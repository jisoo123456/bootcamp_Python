#7.4~7.7
things = ['mozzarella', 'cinderella', 'salmonella']
things[1] = things[1].title()  #7.5
things[0] = things[0].upper()  #7.6
#7.7
#things.pop()
#things.remove('salmonella')
del things[2]
print(things, type(things))