# Create a function that takes in two lists and creates a single dictionary where the first list contains keys and the second values. 
# Assume the lists will be of equal length.
'''
def make_dict(arr1, arr2):
    new_dict = {}
    value=0
    if(len(arr1)>len(arr2)):
        for key in arr1:
            if value == len(arr2):
                new_dict[key]= " "
            else:
                new_dict[key]=arr2[value]
                value+=1
            
        return new_dict
    else:
        for key in arr1:
            if value == len(arr2):
                new_dict[key]= " "
            else:
                new_dict[key]=arr2[value]
                value+=1
'''




name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
def make_dict(arr1,arr2):
    mynewdict = zip(arr1,arr2)
    newestdict = dict(mynewdict)
    return newestdict

print make_dict(name,favorite_animal)