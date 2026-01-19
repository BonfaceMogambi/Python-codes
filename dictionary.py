thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020, # This will overwrite the previous "year" key
  "colors": ["red", "white", "blue"]
}
print(thisdict) # print the dictionary in order of insertion
print(type(thisdict))
print(len(thisdict)) # length of the dictionary


thisdict = dict(name = "John", age = 36, country = "Norway") # Creating a dictionary using the dict() constructor
print(thisdict)