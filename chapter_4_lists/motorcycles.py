motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")
motorcycles[0] = 'ducati'
print(motorcycles)
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

motorcycles.append('bmw')
print(motorcycles)
too_expensive = 'bmw'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
moped = []

moped.append('karpatu')
moped.append('voshod')
moped.append('upiter')

print(moped)

moped.insert(1, 'zaika')
print(moped)

del moped[1]
print(moped)

moped.append('cherepaha')
print(moped)

moped.remove('voshod')
print(moped)
