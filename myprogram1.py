cab = input("Enter the cabin class in Capital letter: ")

if cab == 'LUX':
    print("Upper-deck cabin with a balcony.")
elif cab == 'A':
    print("Above the car deck, equipped with a window.")
elif cab == 'B':
    print("Windowless cabin above the car deck.")
elif cab == 'C':
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")