# Create a function that takes in two lists and creates a single dictionary where the first list contains keys and the second values. 
# Assume the lists will be of equal length.


name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks"]
def make_dict(arr1,arr2):
    newDict = {}
    value =0
    if len(arr1)>len(arr2):
        for val in arr1:
            if value <len(arr2):
                newDict[val]=arr2[value]
            else:
                newDict[val]="none"
            value +=1
    else:
        for val in arr2:
            if value <len(arr1):
                newDict[val]=arr1[value]
            else:
                newDict[val]="none"
            value +=1
    return newDict

print make_dict(name,favorite_animal)