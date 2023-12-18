#1. Write a Python program to create a list of given strings individually of the list using
#Python map function.
#Eg.
#Input:
#['Red', 'Blue', 'Black', 'White', 'Pink']
#Output:
#[['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]

color = ['Red', 'Blue', 'Black', 'White', 'Pink'] 
print("Original list: ")
print(color) 

result = list(map(list, color)) 
print(result)