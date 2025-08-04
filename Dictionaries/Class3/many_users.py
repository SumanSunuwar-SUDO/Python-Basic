# A Dictionary in a Dictionary
user = {
    "suman" : {
        "first" : "suman",
        "last" : "sunuwar",
        "location" : "kathmandu",
    },
    "anish" : {
        "first" : "anish",
        "last" : "shrestha",
        "location" : "gokarneshwor",
    },
    "pasang" : {
        "first" : "pasang",
        "last" : "don",
        "location" : "besigaun",
    },
}

for name, user_info in user.items():
    print("Username " + name)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull Name :" + full_name)
    print("\tLocation : " + location)

