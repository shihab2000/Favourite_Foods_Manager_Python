favourite_foods=[]

while True:
    print("Favourite Foods Manager")
    print("0. Exit")
    print("1. Add Foods.")
    print("2. Remove Foods.")
    print("3. View Favourite all Foods")

    choice=input("Choose an option : ")

    if choice=="0":
        print("Thanks for using Favourite Foods Manager.")
        break;
    elif choice=="1":
        food=input("Enter you favourite food name : ")
        favourite_foods.append(food)
        print("Food added successfully.")
    elif choice=="2":
        food=input("Enter your food name Which you want to remove: ")
        favourite_foods.remove(food)
        print("Food remove successfully")
    elif choice=="3":
        if favourite_foods:
            print("Your Favourite Foods: ")
            for index, food in enumerate(favourite_foods,start=1):
                print(f"{index}.{food}")
        else:
            print("Food List is empty or didn't add yet.")
    else:
        print("Invalid Choice.")