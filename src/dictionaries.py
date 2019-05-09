"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with 
lists!). 

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    }, 
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    }, 
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE

waypoints.append({'lat': 45, 'lon': -125, 'name': 'yet another place'})

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# YOUR CODE HERE

waypoints[0]['name'] = 'not a real place'
waypoints[0]['lon'] = -130

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE

for dictionary in waypoints:
    print(dictionary)

for i in range(0, len(waypoints)):
    print(waypoints[i])

for point in waypoints:
    print('Latitude: ' + str(point['lat']))
    print('Longitude: ' + str(point['lon']))
    print('Name: ' + point['name'])

for point in waypoints:
    for key in point:
        print(key + ': ' + str(point[key]))

for i in waypoints:
    sentence = " %s is located at %d latitude and %d logitude." % (i['name'], i['lat'], i['lon'])
    print(sentence)

# Could we find a dictionary with a specific key value...if we don't know the index?
# Have it return the index of the found dictionary
# Hint: Start with a for loop

for i in range(0, len(waypoints)):
    if waypoints[i]['name'] == 'not a real place':
        print(i)


# Another option is to use a simpler loop on the dictionaries within the list, then return the index using a list method

for item in waypoints:
    if item['name'] == 'not a real place':
        print(waypoints.index(item))

# We could make this more generalized and reusable by turning it into a function

def find_key(value):
    output = 'Not found'
    for item in waypoints:
        if item['name'] == value:
            output = "Found at " + str(waypoints.index(item))
    print(output)

find_key("a third place")
find_key("Not found")

# And taking it a step further, giving it additional parameters for the list and key name

def find_another_key(a_list, key, value):
    output = 'Not found'
    for item in a_list:
        if item[key] == value:
            output = "Found at " + str(waypoints.index(item))
    print(output)

find_another_key(waypoints, 'name', "a third place")
find_another_key(waypoints, 'name', "Not found")
