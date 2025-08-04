# Nesting
# A list of dictionaries
alien_0 = {'color' : 'green', 'points' : 10}
alien_1 = {'color' : 'blue', 'points' : 15}
alien_2 = {'color' : 'green', 'points' : 20}

alines = [alien_0, alien_1, alien_2]

print(alines)

# make an empty list for storing aliens
alines = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 10, 'speed' : 'slow'}
    alines.append(new_alien)

# show the first 5 aliens
for alien in alines[:5]:
    print(alien)

# show how many aliens have been created
print("Total number of aliens: "  + str(len(alines)))