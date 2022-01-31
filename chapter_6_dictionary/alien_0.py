alien_0 = {
    'color': 'green',
    'points': 5,
}
alien_0['game_id'] = 'SRT-022-0015-01'
alien_0['type'] = 'civilian'
alien_0['planet'] = 'SRT02200015'
alien_0['national'] = 'multuhrintion'
del alien_0['national'] # delete key national
print(alien_0) # Check sucsessfully delete key "national" from dictionary
alien_0['national'] = 'naburian'
alien_0['location'] = 'zortok'
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = ['slow', 'medium', 'fast']

print(alien_0)

print("\nOriginal x-position is " + str(alien_0['x_position']) + ". \nAlien color is " + alien_0['color'])

# Move the alien to the right
# Determine how far to move the alien based on its current speed

if alien_0['speed'] == 'slow':
    x_increment = 1
    alien_0['color'] = 'green'
    alien_0['points'] = 5
elif alien_0['speed'] == 'medium':
    x_increment = 2
    alien_0['color'] = 'yelow'
    alien_0['points'] = 10
else:
    # This must be the faster alien
    x_increment = 3
    alien_0['color'] = 'red'
    alien_0['points'] = 20

# The new position is the current position plus increment

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position is " + str(alien_0['x_position']) + ". \nAlien color is " + alien_0['color'] + "\nAlien earned " + str(alien_0['points']) + " points.")
    
#new_points = alien_0['points']

#print(alien_0)

#print("You just earned " + str(new_points) + " points.")
#print("\nIt's alien is " + alien_0['color'] + " and have " + str(alien_0['points']) + " points.")