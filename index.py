# Create a function that takes in two lists and creates a single dictionary where the first list contains keys and the second values. 
# Assume the lists will be of equal length.


name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
def make_dict(arr1,arr2):
    mynewdict = zip(arr1,arr2)
    newestdict = dict(mynewdict)
    return newestdict

print make_dict(name,favorite_animal)