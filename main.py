#8.6~8.9

animals = {'cats': 'Henry', 'octopi': 'Grumpy', 'emus': 'Lucy'}  #8.6
life = {'animals': ' ', 'plants': ' ', 'other': ' '}

life['animals'] = animals

print(life)

print(list(life))  #8.7

print(life['animals'].items())  #8.8

print(life['animals']['cats'])  #8.9