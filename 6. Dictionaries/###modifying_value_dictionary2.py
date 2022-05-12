alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f"Orginal position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else: #then that will be fast
    x_increment = 3

print(f"New position: {alien_0['x_position']}")




