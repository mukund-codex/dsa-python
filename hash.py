user = {
    "age" : 30,
    "name": "Mukunda",
    "magic": True,
    "scream": lambda: print("ahhhhhhhhhh!")
}

print(user["age"])
print(user["name"])
user["spell"] = "abra kadabra"
print(user["spell"])
user["scream"]()