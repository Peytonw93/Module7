from sortedcontainers import SortedDict
import sys


#Start by taking a Dog Breed and its rating from the user in the command line
def your_dog_rate():
    dog = sys.argv[1]
    rate = sys.argv[2]
    try:
        print("\n\n\nYou would rate {} as {}? Neato, check out our dog ratings!\n\n".format(dog,rate))
    except IndexError:
    	print("Hey, we'd love to hear your rating of a dog!\n\n\n")
        
    
your_dog_rate()

#use this to show user options
def menu():
	print("1. Show me the dogs")
	print("2. Look up dog score")
	print("3. Add a dog")
	print("4. My top 3 favorite Dogs")
	print("5. Save the dictionary as a .txt file")
	print("6. Quit\n\n")

#Create a dictionaty of dogs and their ratings
dogs = SortedDict()
dogs['Labrador'] = 'Beautiful'
dogs['Huskey'] = 'Magnificent'
dogs['Grey Hound'] = 'Tall/Good'
dogs['Pitbull'] = 'Very good'
dogs['Dachshund'] = 'Not much dog but still good'
dogs['Chihuahua'] = 'Very bark/Cuddly'

#create a counter for menu choices
menu_choice = 0

#display your menu
menu()

#get the users input for anything other than 4
while menu_choice != 6:
    try:
        # Have the user type one of the options
        menu_choice = int(input("Type in a number (1-6): "))
    # If the user types something other than an integer stop and go back to the menu
    except:
        print("Sorry, we're gonna need an Integer.\n\n\n")

    #Shoe the dogs and their scores
    if menu_choice == 1:
        print("Dog Ratings:\n")
        for x,y in dogs.items():
            print("Dog: {} \tRating: {} \n".format(x,y))

    # Look up a specific dog rating     
    elif menu_choice == 2:
        print("Lookup Dog\n")
        dog_type = input("Which Dog: ")
        if dog_type in dogs:
            print(dogs[dog_type])
        else:
            print("Uh oh, looks like we haven't rated that dog! You should with option 3!\n\n\n")

    #Take user input to add a dog rating
    elif menu_choice == 3:
        print("Rate a dog\n")
        dog_type = input("Dog: ")
        dog= input("Rating: ")
        if dog_type == "":
            print("Please enter something!\n\n\n")
        else:
            dogs[dog_type] = dog

    #For the record these aren't my favorite dogs, its just the first three dogs in the list
    elif menu_choice == 4:
    	print("My top three favorite dogs\n")
    	dog_list = list(dogs.keys())
    	print(dog_list[0:3])
    	
    #I know how to format strings when im just printing them, but I can't fint how to format a Dictionary output?	
    elif menu_choice == 5:
        print("Saved!")
        f = open('Good_Dogs.txt', 'w+')
        f.write(str(dogs ) )
        f.close()

     #all other cases, take them to the menu
    elif menu_choice != 6:
        print_menu()


