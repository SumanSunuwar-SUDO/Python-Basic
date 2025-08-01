
# A Simply Dictionary
'''
variable = { "key" : "value"}
'''
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# accessing values in a dictionary
alien_0 = {'color' : 'green'}
print(alien_0['color'])

# adding New Key-Value Pairs
alien_0 = { 'color' : 'green', 'points' : 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an empty dictionary
alien_0 = {}
alien_0['color'] = 'black'
alien_0['points'] = 55
print(alien_0)

# Modifying values in a dictionary
alien_0 = {'color':'red'}
print("The alien is now "+ alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print('The alien is now ' + alien_0['color'] + ".")

# Removing key-value pairs
alien_0 = {'color': 'blue', 'points': 15}
print(alien_0)
del alien_0['points']
print(alien_0)
# Be aware that the deleted key-value pair is removed permanently. 

# A dictionary of similar objects
favorite_languages = {
    'suman' : 'python',
    'anish': 'c',
    'pasang' : 'ruby',
    'sushil' : 'python'
}

print("Suman's favorite language is " + favorite_languages['suman'].title() + ".")