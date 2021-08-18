#There are two rooms A and B
#Clean is 1 and Dirty is 0

def clean():

    location = input("Enter which room it is present in: ")
    status = int(input("\nEnter the satus of the room: "))
    status_other = int(input("\nEnter the status of other room: "))

    if location == "A":
        Room_status = {location: status, "B": status_other}
    else:
        Room_status = {"A": status_other, location: status}

    cost = 0

    print(Room_status["A"])

    if location == "A":
        if Room_status["A"] == 0:
            print("Vaccum is place in room A and the room is dirty!!")
            print("\nCleaning Room A......")
            cost += 1
            print("\nRoom A is cleaned!\nChecking room B>>>>")
            if Room_status["B"] == 0:
                print("Vaccum is place in room B and the room is dirty!!")
                print("\nCleaning Room B......")
                cost += 2
                print("\nRoom B is cleaned!")
                print("Shutting OFF!!")
            else:
                print("Vaccum is place in room B and the room is Clean!!")
                print("Shutting OFF!!")
        if Room_status["A"] == 1:
            print("Vaccum is place in room A and the room is clean!!")
            print("Checking room B>>>>")
            if Room_status["B"] == 0:
                print("Vaccum is place in room B and the room is dirty!!")
                print("\nCleaning Room B......")
                Room_status["B"] = 1
                cost += 2
                print("\nRoom B is cleaned!")
                print("Shutting OFF!!")
            else:
                print("Vaccum is place in room B and the room is Clean!!")
                print("Shutting OFF!!")
    else:
        if Room_status["B"] == 0:
            print("Vaccum is place in room B and the room is dirty!!")
            print("\nCleaning Room B......")
            Room_status["B"] = 1
            cost += 1
            print("\nRoom B is cleaned!\nChecking room A>>>>")
            if Room_status["A"] == 0:
                print("Vaccum is place in room A and the room is dirty!!")
                print("\nCleaning Room A......")
                Room_status["A"] = 1
                cost += 2
                print("\nRoom A is cleaned!")
                print("Shutting OFF!!")
            else:
                print("Vaccum is place in room A and the room is Clean!!")
                print("Shutting OFF!!")
        if Room_status["B"] == 1:
            print("Vaccum is place in room B and the room is clean!!")
            print("Checking room A>>>>")
            if Room_status["A"] == 0:
                print("Vaccum is place in room A and the room is dirty!!")
                print("\nCleaning Room A......")
                Room_status["A"] = 1
                cost += 1
                print("\nRoom A is cleaned!")
                print("Shutting OFF!!")
            else:
                print("Vaccum is place in room A and the room is Clean!!")
                print("Shutting OFF!!")
        Room_status = {"A": 1, "B":1}
    print("The cost of cleaning the room is: ", cost)

clean()