# [ ] create, call and test fishstore() function 
name = "Evan Pollard"

def fishstore(fish, price): 
    return "Fish Type: " + fish + " costs $" + price

#Gather User Input
fish_entry = input("input the type of fish: ")
price_entry = input("Enter the price of the fish: ")

report = fishstore(fish_entry, price_entry)

#final print statement
print (" Hello Evan Pollard. " + report) 
# print("Hi", name, "fish costs...")


